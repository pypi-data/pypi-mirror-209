from k8s_smuggler.cli.runtime import RunningState
from k8s_smuggler.cli.visual import print_json


class ConfigurationActions:
    def __init__(self, running_state:RunningState) -> None:
        self.running_state = running_state
        self.config = running_state.config

    def show_configuration(self) -> bool:
        running_config = self.config.to_dict()
        print_json(running_config)
