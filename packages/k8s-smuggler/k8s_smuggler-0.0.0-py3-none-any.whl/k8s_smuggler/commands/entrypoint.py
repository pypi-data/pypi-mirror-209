import logging

import click

from k8s_smuggler.cli.config_file import create_config_dirs, read_config
from k8s_smuggler.cli.runtime import RunningState
from k8s_smuggler.cli.logs import config_main_logger
from k8s_smuggler.cli.signals import setup_signal_handling

from k8s_smuggler.commands.config import config
from k8s_smuggler.commands.migrate import migrate
from k8s_smuggler.commands.version import version

LOG = logging.getLogger(__name__)


def register_cli_commands() -> None:
    cli.add_command(config)
    cli.add_command(migrate)
    cli.add_command(version)


def stop_execution(_signal_name:str, status:RunningState) -> None:
    if not status.is_busy():
        LOG.info("Exiting")
        raise SystemExit()

    if not status.is_halting():
        status.halt()
        LOG.info("Busy, stopping gracefully...")


def verbosity_to_loglevel(verbosity:int) -> int:
    if verbosity == 0:
        return 50
    if verbosity == 1:
        return 40
    if verbosity == 2:
        return 20
    if verbosity == 3:
        return 10
    return 1


@click.group()
@click.option("-v", "--verbose", count=True, type=int,
    help="Verbose output, multiple -v options increase the verbosity")
@click.pass_context
def cli(ctx: click.Context, verbose:int) -> None:
    """Kubernetes Smuggler (https://github.com/DiegoPomares/k8s_smuggler)
    """

    main_logger = "k8s_smuggler"
    if (level := verbosity_to_loglevel(verbose)) == 1:
        main_logger = ""
    config_main_logger(level, main_logger)

    ctx.obj = RunningState(config=None)
    setup_signal_handling(stop_execution, ctx.obj)

    create_config_dirs()
    ctx.obj.config = read_config()
    LOG.info("Configuration: %s", ctx.obj.config)
