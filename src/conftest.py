"""Fixutres for test_binheap.py."""
import pytest


@pytest.fixture
def ebh():
    """Initialize an empty binary heap."""
    from binheap import Binheap
    return Binheap()


@pytest.fixture
def pq():
    """Initialize a empty pq."""
    from priorityq import Priorityq
    return Priorityq()


@pytest.fixture
def g():
    """Initialize a empty pq."""
    from graph import Graph
    return Graph()
