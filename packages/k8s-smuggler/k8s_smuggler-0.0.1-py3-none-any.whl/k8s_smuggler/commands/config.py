import click

from k8s_smuggler.actions.config import ConfigurationActions


@click.group(short_help="Config operations")
def config() -> None:
    """Pipes CLI configuration"""


@config.command(short_help="Show running config")
@click.pass_context
def show(ctx:click.Context) -> None:
    """Show complete config"""

    configuration_actions = ConfigurationActions(ctx.obj)
    configuration_actions.show_configuration()
