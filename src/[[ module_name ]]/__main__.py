"""Commandline interface entry point."""

import importlib.metadata

import click

from .greet import greet


def get_version() -> str:
    """Gets the version.

    Returns:
        str: The version.
    """
    return importlib.metadata.version("[[ project_name ]]")


@click.command(
    help=f"Greets a person by their name. Version {get_version()}",
    context_settings={"help_option_names": ["-h", "--help"]},
)
@click.option(
    "-n",
    "--name",
    default="World",
    help="The name of the person to greet.",
)
@click.version_option(version=get_version())
def cli(name: str) -> None:
    """Commandline interface wrapper.

    Args:
        name (str): The name.
    """
    click.echo(greet(name))


if __name__ == "__main__":
    cli()  # pylint: disable=no-value-for-parameter
