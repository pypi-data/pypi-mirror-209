import click

from k8s_smuggler.actions.migrate import MigrateActions
from k8s_smuggler.cli.runtime import CliException
from k8s_smuggler.cli.visual import echo, color

@click.group(short_help="Migration operations")
def migrate():
    """Migrate Kubernetes resources"""

@migrate.command(short_help="Migrate whole namespaces")
@click.option("--from", "src_ctx", type=str, required=True,
    help="Name of the source context (as defined in ~./kube/config)")
@click.option("--to", "dst_ctx", type=str, required=True,
    help="Name of the destination context (as defined in ~./kube/config)")
@click.option("--namespace", "src_namespace", type=str, required=True,
    help="Name of the namespace to migrate")
@click.option("--destination-namespace", "dst_namespace", type=str, default=None,
    help="Name of the namespace in the destination cluster, defaults to the origin namespace")
@click.option("--force-preferred-gvs", is_flag=True,
    help="Force the use of the preferred GroupVersion in the destination cluster")
@click.option("--dry-run", is_flag=True,
    help="Only perform migration related checks")
@click.option("--pause", is_flag=True,
    help="Pause execution at the start of each step")
@click.pass_context
def namespace(ctx:click.Context, src_ctx:str, dst_ctx:str, src_namespace:str, dst_namespace:str,
              force_preferred_gvs:bool, dry_run:bool, pause:bool):
    """Migrate namespaces and their resources

    Using the '--force-preferred-gv' option will force resource definitions in the source cluster
    to be translated to the preferred version in the destination cluster even if the original
    GroupVersion is available.
    """

    if dst_namespace is None:
        dst_namespace = src_namespace
    else:
        echo(color("Warning: ", fg="yellow"), "Source and destination namespaces are different")

    if src_ctx == dst_ctx and src_namespace == dst_ctx:
        raise CliException("Error: both source and destination clusters and namespaces are the same")

    migrate_actions = MigrateActions(ctx.obj)
    migrate_actions.migrate_namespace(src_ctx, dst_ctx, src_namespace, dst_namespace,
                                      force_preferred_gvs, dry_run, pause)
