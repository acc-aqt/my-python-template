"""Testcases for example_module.py go here."""

from src.example_package import hello_world


def test_my_sum_one_plus_one_is_two():
    """An exemplary testcase for my_sum()."""
    assert hello_world() is None
