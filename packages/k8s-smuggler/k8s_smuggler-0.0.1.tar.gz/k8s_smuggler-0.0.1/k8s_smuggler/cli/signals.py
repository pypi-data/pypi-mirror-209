import logging
import signal

from typing import Any, Callable, Dict, Tuple

LOG = logging.getLogger(__name__)

SignalCallback = Callable[[str, Tuple[Any], Dict[str, Any]], None]


def signal_handler(callback:SignalCallback, *args:Any, **kwargs:Any) -> Callable[[int, Any], None]:
    signals = {v.value: k for k, v in signal.__dict__.items() if k.startswith("SIG") and not k.startswith("SIG_")}

    def wrapper(signal_number:int, _frame:Any) -> None:
        signal_name = signals[signal_number]
        LOG.debug("Caught %s", signal_name)
        callback(signal_name, *args, **kwargs)

    return wrapper


def setup_signal_handling(callback:SignalCallback, *args:Any, **kwargs:Any) -> None:
    exit_handler = signal_handler(callback, *args, **kwargs)
    signal.signal(signal.SIGINT, exit_handler)
    signal.signal(signal.SIGTERM, exit_handler)
