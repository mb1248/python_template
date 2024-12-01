"""Unit tests greet."""

from python_template.greet import greet


def test_greet() -> None:
    """Test for greet."""
    assert greet("Max") == "Hallo, Max!"
