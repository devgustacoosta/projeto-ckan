import click


@click.group(short_help="almavivasolutions CLI.")
def almavivasolutions():
    """almavivasolutions CLI.
    """
    pass


@almavivasolutions.command()
@click.argument("name", default="almavivasolutions")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [almavivasolutions]
