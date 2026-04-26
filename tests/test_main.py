"""Test for __main__."""

import pytest
from click.testing import CliRunner

from python_template.__main__ import cli


@pytest.fixture
def runner() -> CliRunner:
    """Fixture to provide a Click test runner.

    Returns:
        CliRunner: The CliRunner.
    """
    return CliRunner()


def test_greet_default(runner: CliRunner) -> None:
    """Test the CLI with the default name."""
    result = runner.invoke(cli)
    assert result.exit_code == 0
    assert "Hello, World!" in result.output


def test_greet_with_name(runner: CliRunner) -> None:
    """Test the CLI with a specified name."""
    result = runner.invoke(cli, ["--name", "Max"])
    assert result.exit_code == 0
    assert "Hello, Max!" in result.output


def test_help_option(runner: CliRunner) -> None:
    """Test the help option."""
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert "Usage:" in result.output
    assert "Greets a person by their name." in result.output
