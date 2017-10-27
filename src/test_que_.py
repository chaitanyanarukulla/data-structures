"""Testing que_.py for Q class."""

import pytest

from que_ import Queue


def test_create_queue_len_at_0():
    """Check if len returns Q length at 0."""
    s = Queue()
    assert len(s) == 0
