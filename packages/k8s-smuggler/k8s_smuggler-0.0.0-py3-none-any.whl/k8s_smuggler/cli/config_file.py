import logging
import os

from typing import Any, Dict, Callable, Type, Union

from k8s_smuggler.configuration import CONFIG, Configuration
from k8s_smuggler.lib.base_config import FieldFromFile

LOG = logging.getLogger(__name__)


def set_config(callback:Callable[[Type, Any, str], Any]) -> None:
    from_file_config = CONFIG.get_from_file_params()

    def transverse(obj:Union[Dict, FieldFromFile]):
        if isinstance(obj, dict):
            config = {}
            for k, v in  obj.items():
                config[k] = transverse(v)
            return config

        if isinstance(obj, FieldFromFile):
            return callback(obj.type, obj.default, obj.description)

        raise RuntimeError(f"Unexpected type {type(obj)}")

    config = transverse(from_file_config)
    CONFIG.fill_config(config)


def read_config() -> Configuration:
    CONFIG.fill_config({})
    return CONFIG


def create_config_dirs() -> None:
    os.makedirs(CONFIG.config_dir, exist_ok=True)
    os.makedirs(CONFIG.backups_dir, exist_ok=True)
