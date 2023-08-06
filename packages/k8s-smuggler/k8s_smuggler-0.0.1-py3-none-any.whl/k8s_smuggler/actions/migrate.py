import copy
import logging
import json
import os
import re
import uuid
from datetime import datetime
from typing import Any, Dict, List, Tuple

from k8s_smuggler.cli.runtime import CliException, RunningState
from k8s_smuggler.cli.visual import color, echo, stepper
from k8s_smuggler.kubernetes.client import KubernetesClient
from k8s_smuggler.kubernetes.mappings import find_translation_candidate, translate_resource
from k8s_smuggler.kubernetes.sanitization import sanitize_for_copy

LOG = logging.getLogger(__name__)


class MigrateActions:
    def __init__(self, running_state:RunningState) -> None:
        self.running_state = running_state
        self.config = running_state.config
        self.migration_state = {}

    def _generate_migration_id(self) -> str:
        date_format = self.config.migration.timestamp_format
        timestamp = datetime.now().strftime(date_format)
        random = uuid.uuid4().hex
        return f"{timestamp}__{random}"

    # Chapuza: Way to large, we need a state machine
    # pylint: disable=too-many-locals
    def migrate_namespace(self, src_ctx:str, dst_ctx:str, src_namespace:str, dst_namespace:str,
                          force_preferred_gvs:bool, _dry_run:bool, pause:bool):
        # Chapuza: this should be defined outside and provided via argument
        def pause_fn(_step:int) -> None:
            input(color("[Press Enter to continue]", dim=True))
        if not pause:
            pause_fn = None

        next_step = stepper(24, callback=pause_fn)
        migration_id = self._generate_migration_id()
        self.migration_state["id"] = migration_id

        fmt_src_namespace = color(src_namespace, fg="bright_cyan")
        fmt_dst_namespace = color(dst_namespace, fg="bright_cyan", underline=True)
        fmt_migration_id = color(migration_id, fg="magenta")

        src_client = KubernetesClient.new_session(src_ctx)
        dst_client = KubernetesClient.new_session(dst_ctx)

        self._print_migration_info(src_ctx, dst_ctx, fmt_src_namespace, fmt_dst_namespace, fmt_migration_id)

        next_step("Check Kubernetes clusters info")
        self._gather_clusters_info(source=src_client, destination=dst_client)

        next_step("Validate source and destination Namespaces exist")
        echo(color("  <NOT IMPLEMENTED>\n", fg="yellow"))

        next_step("Discover preferred GroupVersions for resource types in source cluster")
        src_gvs_per_category = self._discover_preferred_group_versions(src_client)

        fmt_verbs = color("get", fg="cyan")
        next_step(f"Validate {fmt_verbs} privileges for discovered resource types in source cluster")
        echo(color("  <NOT IMPLEMENTED>\n", fg="yellow"))

        next_step(f"Retrieve resources to migrate from source namespace: {fmt_src_namespace}")
        src_resources = self._retrieve_resources(src_client, src_namespace, src_gvs_per_category)

        next_step(f"Filter out resources from source namespace: {fmt_src_namespace}")
        self._filter_out_resources(src_resources)

        next_step(f"Sanitize resource definitions from source namespace: {fmt_src_namespace}")
        src_resources_sanitized = self._sanitize_resources(src_resources)

        next_step("Discover available GroupVersions for resource types in destination cluster")
        dst_gvs_per_category = self._discover_dst_group_versions(force_preferred_gvs, dst_client)

        next_step("Determine resource GroupVersions interoperability from source -> destination")
        incompatibilities = self._find_gv_incompatibilities(src_gvs_per_category, dst_gvs_per_category)

        next_step("Resolve resource definition incompatibilities")
        dst_compatible_resources = self._fix_incompatibilities(incompatibilities,
                                                               dst_gvs_per_category, src_resources_sanitized)

        next_step("Constrict resource definitions for active resources")
        echo(color("  <NOT IMPLEMENTED>\n", fg="yellow"))

        next_step("(Optional) Add migration metadata to resource definitions")
        dst_resources = dst_compatible_resources  # TODO: This line is temporary
        echo(color("  <NOT IMPLEMENTED>\n", fg="yellow"))

        next_step("Generate final Kubernetes manifests")
        k8s_src_manifest, k8s_dst_manifest = self._generate_k8s_manifests(src_resources_sanitized, dst_resources)

        fmt_verbs = color("get, create", fg="cyan")
        next_step(f"Validate {fmt_verbs} privileges for resource types in destination cluster")
        echo(color("  <NOT IMPLEMENTED>\n", fg="yellow"))

        next_step(f"Validate name collisions for resources in destination namespace: {fmt_dst_namespace}")
        echo(color("  <NOT IMPLEMENTED>\n", fg="yellow"))

        next_step(f"Dry-run create resources in destination namespace: {fmt_dst_namespace}")
        echo(color("  <NOT IMPLEMENTED>\n", fg="yellow"))

        next_step("Back up resource definitions locally")
        self._backup_data(migration_id,
                          src_gvs_per_category, dst_gvs_per_category,
                          src_resources, src_resources_sanitized,
                          dst_compatible_resources,
                          k8s_src_manifest, k8s_dst_manifest)

        next_step(f"Create resources in destination namespace: {fmt_dst_namespace}")
        with self.running_state.prevent_exit():
            self._create_dst_resources(dst_client, dst_namespace, dst_resources)

        next_step(f"Remove constriction of active resources in destination namespace: {fmt_dst_namespace}")
        echo(color("  <NOT IMPLEMENTED>\n", fg="yellow"))

        next_step("Begin workload handover and perform availability validations")
        echo(color("  <NOT IMPLEMENTED>\n", fg="yellow"))

        next_step(f"Constrict active resources in source namespace: {fmt_src_namespace}")
        echo(color("  <NOT IMPLEMENTED>\n", fg="yellow"))

        next_step("Perform final availability validations")
        echo(color("  <NOT IMPLEMENTED>\n", fg="yellow"))

        next_step(f"(Optional) Delete resources in source namespace: {fmt_src_namespace}")
        echo(color("  <NOT IMPLEMENTED>\n", fg="yellow"))

        next_step(f"(Optional) Remove migration metadata to resources in destination namespace: {fmt_dst_namespace}")
        echo(color("  <NOT IMPLEMENTED>\n", fg="yellow"))

    def _create_dst_resources(self, dst_client:KubernetesClient, dst_namespace:str,
                              dst_resources:Dict[str, Dict[str, List[Dict[str, Any]]]]) -> None:

        for resource_category, resources_per_type in dst_resources.items():
            echo(f"  {resource_category.capitalize()} resources:")
            for resource_type, resource_list in resources_per_type.items():
                echo(f"    {resource_type}")
                for definition in resource_list:
                    group_version = definition["apiVersion"]
                    resource_name = definition["metadata"]["name"]
                    echo(f"      {resource_name}: ", nl=False)
                    response = dst_client.create_namespaced_resource(resource_type, group_version, dst_namespace,
                                                                     definition)

                    if error := response.get("error"):
                        echo(color("Error! ", fg="red"), error["message"])
                        continue

                    echo(color("Ok", fg="bright_green"))
            echo()

    def _backup_data(self, migration_id:str,
                            src_gvs_per_category:Dict[str, Any], dst_gvs_per_category:Dict[str, Any],
                            src_resources:Dict[str, Any], src_resources_sanitized:Dict[str, Any],
                            dst_compatible_resources:Dict[str, Any],
                            final_src_manifest:Dict[str, Any], final_dst_manifest:Dict[str, Any]) -> None:
        files = {
            "source_preferred_gvs.json": src_gvs_per_category,
            "source_original_resources.json": src_resources,
            "source_resources_sanitized.json": src_resources_sanitized,
            "destination_available_gvs.json": dst_gvs_per_category,
            "destination_compatible_resources.json": dst_compatible_resources,
            "kubectl_src_restore_manifest.json": final_src_manifest,
            "kubectl_dst_deploy_manifest.json": final_dst_manifest,
        }

        for filename, data in files.items():
            backup_path = self._write_backup_file(migration_id, filename, data)
            fmt_backup_path = color(backup_path, fg="magenta")
            echo(f"  Backup file: {fmt_backup_path}")

        echo()

    def _write_backup_file(self, migration_id:str, filename:str, data:Dict[str, Any]) -> str:
        backup_dir = os.path.join(self.config.backups_dir, migration_id)
        backup_path = os.path.join(backup_dir, filename)
        os.makedirs(backup_dir, exist_ok=True)
        with open(backup_path, "w", encoding="utf-8") as fh:
            json.dump(data, fh, indent=2)

        return backup_path

    def _generate_k8s_manifests(self, src_resources_sanitized:Dict[str, Dict[str, Dict[str, Any]]],
                                dst_resources:Dict[str, Dict[str, List[Dict[str, Any]]]]
                                ) -> Tuple[Dict[str, Dict[str, Dict[str, Any]]], ...]:
        final_src_manifest = self._generate_k8s_manifest(src_resources_sanitized)
        final_dst_manifest = self._generate_k8s_manifest(dst_resources)

        echo("  Done")
        echo()

        return final_src_manifest, final_dst_manifest

    def _generate_k8s_manifest(self, resources_per_category:Dict[str, Dict[str, List[Dict[str, Any]]]]
                               ) -> Dict[str, Any]:
        k8s_manifest = {
            "apiVersion": "v1",
            "kind": "List",
            "items": [],
        }

        for resources_per_type in resources_per_category.values():
            for resource_list in resources_per_type.values():
                k8s_resource_list = copy.deepcopy(resource_list)
                k8s_manifest["items"].extend(k8s_resource_list)

        return k8s_manifest

    def _fix_incompatibilities(self, incompatibilities:Dict[str, Any],
                               dst_gvs_per_category:Dict[str, Dict[str, List[str]]],
                               src_resources_sanitized:Dict[str, Dict[str, List[Dict[str, Any]]]]
                               ) -> Dict[str, Dict[str, List[Dict[str, Any]]]]:
        if not incompatibilities:
            echo("  Skipping, no incompatibilities found!")
            return src_resources_sanitized

        compatible_resources = copy.deepcopy(src_resources_sanitized)
        for resource_category, resources_per_type in compatible_resources.items():
            echo(f"  {resource_category.capitalize()} resources:")
            no_translations = True
            for resource_type, resource_list in resources_per_type.items():
                if resource_type not in incompatibilities:
                    continue

                no_translations = False
                old_gv = resource_list[0]["apiVersion"]
                translation_candidates = dst_gvs_per_category[resource_category][resource_type]
                new_gv = find_translation_candidate(resource_type, old_gv, *translation_candidates)
                if new_gv is None:
                    raise CliException(" ".join(("Error: Cannot find a translation for resources of type",
                                    color(resource_type, underline=True), "from GroupVersion",
                                    color(old_gv, fg="cyan"), "to a version compatible in destination cluster")))

                for incompatible_resource in resource_list:
                    translate_resource(incompatible_resource, resource_type, old_gv, new_gv)
                    incompatible_resource["apiVersion"] = new_gv

                resource_names = [r["metadata"]["name"] for r in resource_list]
                fmt_resource_names = ", ".join(resource_names)
                fmt_old2new_gv = color(f"({old_gv} -> {new_gv})", fg="cyan")
                echo(f"    {resource_type} {fmt_old2new_gv}: {fmt_resource_names}")

            if no_translations:
                echo("    -\n")
            else:
                echo()

        return compatible_resources

    def _find_gv_incompatibilities(self, src_gvs_per_category:Dict[str, Dict[str, str]],
                                   dst_gvs_per_category:Dict[str, Dict[str, List[str]]]) -> Dict[str, str]:
        incompatibilities = {}
        for resource_category, preferred_src_gvs in src_gvs_per_category.items():
            for resource_type, src_group_versions in preferred_src_gvs.items():
                src_group_version = src_group_versions[0]
                if resource_type not in dst_gvs_per_category[resource_category]:
                    raise CliException(" ".join(("Error: Resource type", color(resource_type, underline=True),
                                       color("does not exist", fg="red", bold=True), "in destination cluster")))

                is_src_gv_in_dst = src_group_version in dst_gvs_per_category[resource_category][resource_type]
                if not is_src_gv_in_dst:
                    incompatibilities[resource_type] = src_group_version
                    echo(f"  {resource_type}: {src_group_version} ", color("(incompatible)", fg="red"))
                    continue

                is_src_gv_dst_preferred = src_group_version == dst_gvs_per_category[resource_category][resource_type][0]
                if not is_src_gv_dst_preferred:
                    echo(f"  {resource_type}: {src_group_version} ", color("(not preferred)", fg="bright_yellow"))
                else:
                    echo(f"  {resource_type}: {src_group_version} ", color("(fully compatible)", fg="bright_green"))

        echo()
        return incompatibilities

    def _discover_dst_group_versions(self, force_preferred_gvs:bool, client:KubernetesClient
                                     ) -> Dict[str, Dict[str, List[str]]]:
        if force_preferred_gvs:
            echo("  (only the preferred GroupVersions in destination cluster are allowed for resource creation)\n")
            dst_gvs_per_category = self._discover_preferred_group_versions(client)
        else:
            dst_gvs_per_category = self._discover_available_group_versions(client)

        return dst_gvs_per_category

    def _discover_available_group_versions(self, client:KubernetesClient) -> Dict[str, Dict[str, List[str]]]:
        active_resource_types = self.config.kubernetes.active_resource_whitelist
        active_resource_types += self.config.kubernetes.extra_active_resource_whitelist

        passive_resource_types = self.config.kubernetes.passive_resource_whitelist
        passive_resource_types += self.config.kubernetes.extra_passive_resource_whitelist

        gvs_per_resource = client.discover_resource_gvs()
        resource_gvs = {
            "active": {rt: [gvs_per_resource[rt]["preferred"]] for rt in active_resource_types},
            "passive": {rt: [gvs_per_resource[rt]["preferred"]] for rt in passive_resource_types},
        }

        echo("  (first GroupVersion is ", color("preferred", bold=True, underline=True), ")\n")
        for resource_category, gvs in resource_gvs.items():
            echo(f"  {resource_category.capitalize()} resources:")
            for resource_type, group_versions in gvs.items():
                available_gvs = gvs_per_resource[resource_type]["available"].copy()
                available_gvs.remove(group_versions[0])
                group_versions.extend(available_gvs)

                fmt_preferred_gv = color(group_versions[0], bold=True, underline=True)
                fmt_group_versions = ", ".join([fmt_preferred_gv] + group_versions[1:])
                echo(f"    {resource_type}: {fmt_group_versions}")

            echo()

        return resource_gvs

    def _sanitize_resources(self, resources_per_category:Dict[str, Dict[str, List[Dict[str, Any]]]]
                            ) -> Dict[str, Dict[str, Dict[str, Any]]]:
        sanitized_resources_per_category = copy.deepcopy(resources_per_category)

        for resources_per_type in sanitized_resources_per_category.values():
            for resource_type, resource_collection in resources_per_type.items():
                for resource in resource_collection["items"]:
                    sanitize_for_copy(resource_type, resource)
                    resource["kind"] = KubernetesClient.list_kind_to_item(resource_collection["kind"])
                    resource["apiVersion"] = resource_collection["apiVersion"]

                resources_per_type[resource_type] = resource_collection["items"]

            for resource_type, resource_collection in list(resources_per_type.items()):
                if not resource_collection:
                    resources_per_type.pop(resource_type)

        echo("  Done")
        echo()

        return sanitized_resources_per_category

    # Chapuza: improve filtering mechanism
    def _filter_out_resources(self, resources_per_category:Dict[str, Dict[str, Dict[str, Any]]]):
        exclusion_regex = self.config.kubernetes.resource_name_filter
        end_str = "  -\n"

        echo("  Excluding resources:")
        if not exclusion_regex:
            echo(end_str)
            return

        for resources_per_type in resources_per_category.values():
            for resource_type, resource_list in resources_per_type.items():
                excluded_resources = []
                for resource in resource_list["items"]:
                    resource_name = resource["metadata"]["name"]
                    if re.search(exclusion_regex, resource_name):
                        excluded_resources.append(resource_name)

                if excluded_resources:
                    filtered_resource_list = []
                    for resource in resource_list["items"]:
                        if resource["metadata"]["name"] not in excluded_resources:
                            filtered_resource_list.append(resource)

                    resources_per_type[resource_type]["items"] = filtered_resource_list
                    formatted_filtered_resources = ", ".join(excluded_resources)
                    echo(f"    {resource_type}: {formatted_filtered_resources}")
                    end_str = ""

        echo(end_str)

    def _retrieve_resources(self, client:KubernetesClient, namespace:str,
                            gvs_per_category:Dict[str, Dict[str, List[str]]]
                            ) -> Dict[str, Dict[str, List[Dict[str, Any]]]]:
        resources_per_category:Dict[str, Dict[str, Dict[str, Any]]] = {}

        for category, preferred_gvs in gvs_per_category.items():
            resources_per_category[category] = {}
            for resource_type, group_versions in preferred_gvs.items():
                response = client.get_resource_list(resource_type, group_versions[0], namespace)
                resource_list = response["data"]
                resources_per_category[category][resource_type] = resource_list

        for resource_category, resources_per_type in resources_per_category.items():
            echo(f"  {resource_category.capitalize()} resources:")
            for resource_type, resource_list in resources_per_type.items():
                resource_names = [r["metadata"]["name"] for r in resource_list["items"]]
                fmt_resource_names = ", ".join(resource_names)
                echo(f"    {resource_type}: {fmt_resource_names}")

            echo()

        return resources_per_category

    def _discover_preferred_group_versions(self, client:KubernetesClient) -> Dict[str, Dict[str, List[str]]]:
        active_resource_types = self.config.kubernetes.active_resource_whitelist
        active_resource_types += self.config.kubernetes.extra_active_resource_whitelist

        passive_resource_types = self.config.kubernetes.passive_resource_whitelist
        passive_resource_types += self.config.kubernetes.extra_passive_resource_whitelist

        gvs_per_resource = client.discover_resource_gvs()
        resource_gvs = {
            "active": {rt: [gvs_per_resource[rt]["preferred"]] for rt in active_resource_types},
            "passive": {rt: [gvs_per_resource[rt]["preferred"]] for rt in passive_resource_types},
        }

        for resource_category, preferred_gvs in resource_gvs.items():
            echo(f"  {resource_category.capitalize()} resources:")
            for resource_type, group_versions in preferred_gvs.items():
                echo(f"    {resource_type}: {group_versions[0]}")

            echo()

        return resource_gvs

    def _gather_clusters_info(self, **clients:KubernetesClient):
        for place, client in clients.items():
            self.migration_state[f"{place}_cluster_version"] = client.version
            echo(f"  {place.capitalize()} Kubernetes cluster info:")
            echo(f"    URL: {client.cluster_url}")
            echo(f"    Version: {client.version[0]}.{client.version[1]}")
            echo()

    def _print_migration_info(self, src_ctx:str, dst_ctx:str, src_namespace:str, dst_namespace:str,
                              migration_id:str) -> None:
        echo("Starting migration")
        echo(f"  Source Namespace: {src_namespace}")
        echo(f"  Source context: {src_ctx}")
        echo(f"  Destination Namespace: {dst_namespace}")
        echo(f"  Destination context: {dst_ctx}")
        echo(f"  Migration ID: {migration_id}")
        echo()
