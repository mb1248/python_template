"""Unit tests greet."""

import importlib

greet = importlib.import_module("[[ module_name ]].greet").greet


def test_greet() -> None:
    """Test for greet."""
    assert greet("Max") == "Hello, Max!"
