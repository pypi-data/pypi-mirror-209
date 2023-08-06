import logging
from importlib.metadata import version

from k8s_smuggler.cli.runtime import RunningState
from k8s_smuggler.cli.visual import echo

LOG = logging.getLogger(__name__)


class VersionActions:
    def __init__(self, running_state:RunningState) -> None:
        self.running_state = running_state
        self.config = running_state.config

    def _get_current_version(self) -> str:
        pkg_name = self.config.cli.package_name
        return version(pkg_name)

    def print_version(self) -> None:
        current_version = self._get_current_version()
        is_running_from_source = self._is_dev_version(current_version)

        echo("Smuggler version ", self._get_current_version())

        if is_running_from_source:
            echo("⚙️  Running from source")

    @staticmethod
    def _is_dev_version(current_version:str) -> bool:
        major_version_str, _ = current_version.split(".", 1)
        if int(major_version_str) == 0:
            return True

        return False
