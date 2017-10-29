"""Create instances for testing stack.py."""
import pytest


@pytest.fixture
def eq():
    """Initialize an empty queue."""
    from que_ import Queue
    return Queue()
