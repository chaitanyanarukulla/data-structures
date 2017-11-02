"""Fixutres for test_binheap.py."""
import pytest


@pytest.fixture
def ebh():
    """Initialize an empty binary heap."""
    from binheap import Binheap
    return Binheap()
