import os
from dataclasses import dataclass, field
from typing import Tuple

from k8s_smuggler.lib.base_config import Configurable

_config_dir = os.path.expanduser("~/.k8s_smuggler")
_backups_dir = os.path.join(_config_dir, "backups")


@dataclass
class CLIConfig(Configurable):
    package_name:str = "k8s-smuggler"


@dataclass
class KubernetesConfig(Configurable):
    active_resource_whitelist:Tuple[str, ...] = ("deployments", "statefulsets", "horizontalpodautoscalers", "cronjobs")
    passive_resource_whitelist:Tuple[str, ...] = ("configmaps", "secrets", "services", "ingresses")
    extra_active_resource_whitelist:Tuple[str, ...] = tuple()
    extra_passive_resource_whitelist:Tuple[str, ...] = tuple()
    resource_name_filter:str = r"(^fiaas.*)|(^default-token.*)|(^artifactory-secrets)|(^schip-namespace-configmap)$"


@dataclass
class MigrationConfig(Configurable):
    timestamp_format:str = "%Y-%m-%d_%Hh%Mm%Ss"


@dataclass
class Configuration(Configurable):
    config_dir:str = _config_dir
    backups_dir:str = _backups_dir
    cli:CLIConfig = field(default_factory=CLIConfig)
    kubernetes:KubernetesConfig = field(default_factory=KubernetesConfig)
    migration:MigrationConfig = field(default_factory=MigrationConfig)


CONFIG = Configuration()
