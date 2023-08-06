import json
import logging
import re
from collections import defaultdict
from functools import reduce
from typing import Any, Dict, List, Optional, Tuple

from kubernetes import client, config

LOG = logging.getLogger(__name__)


class KubernetesClient:
    @classmethod
    def new_session(cls, context:str):
        api_client = config.new_client_from_config(context=context)
        return cls(api_client)

    def __init__(self, api_client:client.ApiClient) -> None:
        self.client = api_client
        self._version = None

    @staticmethod
    def _version_to_int(version:str) -> int:
        clean_version = re.split(r"-|\+", version, 1)
        return int(clean_version[0])

    @property
    def version(self) -> Tuple[int, int]:
        if self._version is None:
            version_api = client.VersionApi(self.client)
            response = version_api.get_code()
            major = self._version_to_int(response.major)
            minor = self._version_to_int(response.minor)
            self._version = (major, minor)
        return self._version

    @property
    def cluster_url(self) -> str:
        return self.client.configuration.host

    def api_call(self, path:str, method:str, **kwargs:Any) -> Dict[str, Any]:
        kwargs.setdefault("auth_settings", ["BearerToken"])
        kwargs.setdefault("_return_http_data_only", True)
        kwargs.setdefault("_preload_content", False)
        kwargs.setdefault("header_params", {
          "Accept": "application/json",
          "Content-Type": "application/json",
        })

        try:
            response = self.client.call_api(path, method, **kwargs)
            return {
                "status": response.status,
                "data": json.loads(response.data.decode()),
            }
        except client.exceptions.ApiException as ex:
            body = ex.body.decode().strip()
            if "application/json" in ex.headers["Content-Type"]:
                message = json.loads(body)
            else:
                message = body

            LOG.debug("Failed API call: %s %s - [%s] %s", method, path, ex.status, message)
            return {
                "status": ex.status,
                "error": message,
            }


    def discover_resource_gvs(self) -> Dict[str, Dict[str, str|List[str]]]:
        def new_item() -> Dict[str, Dict[str, List]]:
            return {
                "available": [],
                "preferred": [],
            }
        gvs_per_resource = defaultdict(new_item)

        # Discover GVs for core API resources
        response = self.api_call("/api", "GET")
        core_version = response["data"]["versions"][0]  # I don't suppose there will be more than 1 any time soon
        response = self.api_call(f"/api/{core_version}", "GET")
        resource_names = [n["name"] for n in response["data"]["resources"] if "/" not in n["name"]]
        for resource_name in resource_names:
            gvs_per_resource[resource_name]["available"].append(core_version)
            gvs_per_resource[resource_name]["preferred"].append(core_version)

        # Get available versions for every group
        response = self.api_call("/apis", "GET")
        groups = response["data"]["groups"]
        versions_per_group = {}
        for group in groups:
            versions_per_group[group["name"]] = {
                "preferred": group["preferredVersion"]["version"],
                "available": [v["version"] for v in group["versions"]],
            }

        # Discover GVs for non-core API resources
        for group_name, versions in versions_per_group.items():
            for version in versions["available"]:
                response = self.api_call(f"/apis/{group_name}/{version}", "GET")
                resource_names = [n["name"] for n in response["data"]["resources"] if "/" not in n["name"]]
                for resource_name in resource_names:
                    group_version = f"{group_name}/{version}"
                    gvs_per_resource[resource_name]["available"].append(group_version)
                    if version == versions["preferred"]:
                        gvs_per_resource[resource_name]["preferred"].append(group_version)

        # Sanitize gvs_per_resource
        for group_version in gvs_per_resource.values():
            group_version["available"] = list(set(group_version["available"]))
            candidates = group_version["preferred"]
            if not candidates:
                candidates = group_version["available"]
            group_version["preferred"] = reduce(self._select_preferred_gv, candidates)

        return dict(gvs_per_resource)

    @staticmethod
    # Chapuza: Better selection criteria
    def _select_preferred_gv(gv1:str, gv2:str) -> str:
        if gv1 == gv2:
            return gv1

        prerelease_strings = ["beta", "alpha"]
        gv1_priority = next((i + 1 for i, s in enumerate(prerelease_strings) if s in gv1), 0)
        gv2_priority = next((i + 1 for i, s in enumerate(prerelease_strings) if s in gv2), 0)
        if gv1_priority < gv2_priority:
            return gv1
        if gv2_priority < gv1_priority:
            return gv2

        if len(gv2) < len(gv1):
            return gv2
        if len(gv1) < len(gv2):
            return gv1

        return sorted([gv1, gv2])[0]

    def get_resource_list(self, resource_type:str, group_version:str, namespace:Optional[str]=None) -> Dict[str, Any]:
        request_path = self._make_resource_request_path(resource_type, group_version, namespace)
        LOG.debug("Retrieving resources at %s", request_path)
        return self.api_call(request_path, "GET")

    def create_namespaced_resource(self, resource_type:str, group_version:str, namespace:str,
                                   resource_definition:Dict[str, Any]) -> Dict[str, Any]:
        request_path = self._make_resource_request_path(resource_type, group_version, namespace)
        LOG.debug("Creating resource at %s", request_path)
        return self.api_call(request_path, "POST", body=resource_definition)

    @staticmethod
    def _make_resource_request_path(resources_type:str, group_version:str, namespace:Optional[str]=None) -> str:
        request_path = ""

        if "/" not in group_version:
            request_path += f"/api/{group_version}"
        else:
            request_path += f"/apis/{group_version}"

        if namespace:
            request_path += f"/namespaces/{namespace}"

        request_path += f"/{resources_type}"

        return request_path

    @staticmethod
    def list_kind_to_item(list_kind:str) -> str:
        # TODO: check if this is always valid!
        return list_kind.removesuffix("List")
