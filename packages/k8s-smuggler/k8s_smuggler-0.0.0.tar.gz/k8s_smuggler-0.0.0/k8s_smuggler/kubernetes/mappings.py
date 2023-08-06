# Chapuza: This module needs a refactor and proper structure

from typing import Any, Callable, Dict, Optional, Tuple


def available_translations_table() -> Dict[str, Dict[Tuple[str, str], Callable[[Dict[str, Any]], None]]]:
    return {
        "ingresses": {
            ("extensions/v1beta1", "networking.k8s.io/v1"): ingress_old2new,
        }
    }


def find_translation_candidate(resource_type:str, group_version:str, *translation_candidates:str) -> Optional[str]:
    translation_table = available_translations_table()
    if resource_type not in translation_table:
        return None

    for candidate in translation_candidates:
        translation = (group_version, candidate)

        if translation in translation_table[resource_type]:
            return candidate

    return None


def translate_resource(incompatible_resource:Dict[str, Any], resource_type:str, group_version:str,
                       target_group_version:str) -> None:
    translation_table = available_translations_table()
    translation = (group_version, target_group_version)
    translation_fn = translation_table[resource_type][translation]
    translation_fn(incompatible_resource)


def get_nested_value(obj:Dict[str, Any], path:str) -> Any:
    for key in path.split("."):
        if isinstance(obj, dict) and key in obj:
            obj = obj[key]
        else:
            return None

    return obj


def ingress_old2new(resource:Dict[str, Any]) -> None:
    if "backend" in resource["spec"]:
        resource["spec"]["defaultBackend"] = resource["spec"].pop("backend")

    if (rules := get_nested_value(resource, "spec.rules")) is None:
        return

    for rule in rules:
        if not (paths := get_nested_value(rule, "http.paths")):
            return

    for path in paths:
        path.setdefault("pathType", "ImplementationSpecific")
        if "serviceName" in path["backend"] and "servicePort" in path["backend"]:
            path["backend"] = {
                "service": {
                    "name": path["backend"]["serviceName"],
                    "port": {
                        "number": path["backend"]["servicePort"],
                    }
                }
            }
