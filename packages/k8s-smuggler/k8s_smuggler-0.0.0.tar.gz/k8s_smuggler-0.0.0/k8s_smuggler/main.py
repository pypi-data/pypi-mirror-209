import logging
import sys
import traceback
from typing import NoReturn, Optional

from k8s_smuggler.cli.runtime import CliException
from k8s_smuggler.cli.visual import echo, color
from k8s_smuggler.commands.entrypoint import cli, register_cli_commands

LOG = logging.getLogger(__name__)


def die(ex:Optional[Exception]) -> NoReturn:
    if ex:
        LOG.error(traceback.format_exc())

        exception_msg = "; ".join(str(i) for i in ex.args)
        if isinstance(ex, CliException):
            message = exception_msg

        elif isinstance(ex, FileNotFoundError):
            filename = color(ex.filename, fg="yellow")
            message = f"File not found: {filename}"

        else:
            message = f"Error ({type(ex).__name__}): {exception_msg}"

        echo(message, err=True)

    sys.exit(1)


def main() -> None:
    try:
        register_cli_commands()
        cli()  # pylint: disable=no-value-for-parameter
    except Exception as ex:
        die(ex)
