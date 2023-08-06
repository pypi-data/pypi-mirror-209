from contextlib import contextmanager
from dataclasses import dataclass
from typing import Generator, Optional

from k8s_smuggler.configuration import Configuration


class CliException(Exception):
    pass


@dataclass
class RunningState:
    config: Optional[Configuration]
    halting: bool = False
    busy: bool = False

    def is_busy(self) -> bool:
        return self.busy

    def set_busy(self) -> None:
        self.busy = True

    def unset_busy(self) -> None:
        self.busy = False

    def is_halting(self) -> bool:
        return self.halting

    def halt(self) -> None:
        self.halting = True

    @contextmanager
    def prevent_exit(self) -> Generator["RunningState", None, None]:
        self.set_busy()
        yield self
        self.unset_busy()
