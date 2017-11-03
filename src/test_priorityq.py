"""Test priorityq.py."""
import pytest


def test_priorityq_iinitialize_empty_que(pq):
    """Test initialize an empty pq."""
    assert pq


def test_priorityq_insert_one_val_w_priority(pq):
    """Test insert one value to pq with priority."""
    pq.insert('hi', 0)
    assert pq._highest == 0


def test_insert_n_values_returns_n_length(pq):
    """Test that the number of values inserted is the que's length."""
    for i in range(20):
        pq.insert(i)
    total_length = 0
    for key in pq._que:
        total_length += len(pq._que[key])
    assert total_length == 20

