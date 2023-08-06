import json
import os
from typing import Any, Callable, Optional

import click


def echo(*args:Any, **kwargs:Any) -> None:
    message = "".join(args)

    color_mode = os.environ.get("SMUGGLER_COLOR")
    if color_mode == "always":
        kwargs["color"] = True
    elif color_mode == "never":
        kwargs["color"] = False

    click.echo(message, **kwargs)


def color(*args:str, **kwargs:Any) -> str:
    text = "".join(args)
    return click.style(text, **kwargs)


def print_json(obj:Any) -> None:
    echo(json.dumps(obj, indent=2))


def json_printer(func:Callable):
    def wrapper(*args:Any, **kwargs:Any) -> None:
        output = func(*args, **kwargs)
        print_json(output)

    return wrapper


def stepper(max_steps:int, step_format:str="", callback:Optional[Callable[[int], None]]=None) -> Callable[[str], None]:
    step = iter(range(1, max_steps+1))
    if not step_format:
        step_format = color("[Step {step}/{max_steps}]", fg="blue")
        step_format += " {caption}"

    def wrapper(caption:str="") -> None:
        echo(step_format.format(step=next(step), max_steps=max_steps, caption=caption))
        if callback:
            callback(step)

    return wrapper
