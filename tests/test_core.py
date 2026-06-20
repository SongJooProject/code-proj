"""Tests for core module."""

from src.core import add, hello


def test_hello():
    """Test hello function."""
    assert hello() == "Hello, World!"


def test_add():
    """Test add function."""
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
