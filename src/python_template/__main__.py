"""Commandline interface entry point."""

import importlib.metadata

import click

from .greet import greet


def get_version() -> str:
    """Gets the version.

    Returns:
        str: The version.
    """
    return importlib.metadata.version("python_template")


@click.command(
    help=f"Begrüßt eine Person mit ihrem Namen. Version {get_version()}",
    context_settings={"help_option_names": ["-h", "--help"]},  # Ermöglicht -h für Hilfe
)
@click.option(
    "-n",
    "--name",
    default="Welt",
    help="Der Name der Person, die begrüßt werden soll.",
)
@click.version_option(version=get_version())  # Version hinzufügen
def cli(name: str) -> None:
    """Commandline interface wrapper.

    Args:
        name (str): The name.
    """
    click.echo(greet(name))


if __name__ == "__main__":
    cli()  # pylint: disable=no-value-for-parameter
