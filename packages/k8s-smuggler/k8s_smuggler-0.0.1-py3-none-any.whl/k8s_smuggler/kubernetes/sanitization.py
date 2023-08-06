from typing import Any, Callable, Dict


def specific_sanitization_table() -> Dict[str, Callable[[Dict[str, Any]], None]]:
    return {
        "services": service_sanitization,
    }


def sanitize_for_copy(resource_type:str, resource:Dict[str, Any]) -> None:
    sanitization_table = specific_sanitization_table()

    metadata_keys = ["name", "uid", "labels", "annotations"]
    _dict_whitelist_keys(resource["metadata"], *metadata_keys)

    unneeded_annotations = [
        "deployment.kubernetes.io/revision",
        "kubectl.kubernetes.io/last-applied-configuration",
    ]
    _dict_blacklist_keys(resource["metadata"]["annotations"], *unneeded_annotations)
    _dict_blacklist_keys(resource, "status")

    if resource_type in sanitization_table:
        sanitization_table[resource_type](resource)


def _dict_whitelist_keys(d:Dict[str, Any], *whitelist:str) -> None:
    for key in list(d.keys()):
        if key not in whitelist:
            d.pop(key, None)


def _dict_blacklist_keys(d:Dict[str, Any], *blacklist:str) -> None:
    for key in list(d.keys()):
        if key in blacklist:
            d.pop(key, None)


def service_sanitization(resource:Dict[str, Any]) -> None:
    resource["spec"].pop("clusterIP", None)
    resource["spec"].pop("clusterIPs", None)
