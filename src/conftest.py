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


@pytest.fixture
def bst():
    """Initialize empty bst for tests."""
    from bst import Bst
    return Bst()


@pytest.fixture
def bst_full():
    """Create bst will values for tests."""
    from bst import Bst
    new = Bst()
    new.insert(3254)
    new.insert(908543)
    new.insert(58490543)
    return new


@pytest.fixture
def bst_big():
    """Create bst will values for tests."""
    from bst import Bst
    new = Bst()
    new.insert(50)
    new.insert(40)
    new.insert(68)
    new.insert(10)
    new.insert(110)
    new.insert(1)
    new.insert(500)
    new.insert(18)
    new.insert(80)
    new.insert(5000)
    return new
