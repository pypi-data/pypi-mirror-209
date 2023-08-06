import click


def prompt_yes_no(text:str) -> bool:
    return click.confirm(text)


def always_yes(*_args) -> bool:
    return True
