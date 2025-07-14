import click


@click.command(help="Use for scafolding script files like route, task, etc")
@click.option("-n", "--name", default="demo-file", help="New file name")
def create() -> None:
    pass
