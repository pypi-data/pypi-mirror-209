import click

from k8s_smuggler.actions.version import VersionActions


@click.command(short_help="Print version")
@click.pass_context
def version(ctx:click.Context):
    """Print version and exit"""

    version_actions = VersionActions(ctx.obj)
    version_actions.print_version()
