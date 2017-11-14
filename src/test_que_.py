"""Testing que_.py for Q class."""

import pytest


def test_create_queue_len_at_0(eq):
    """Check if len returns Q length at 0."""
    assert len(eq) == 0


def test_queue_enqueue_to_top(eq):
    """Test if enqueue adds a value to top of queue."""
    eq.enqueue('test')
    assert eq.peek() == 'test'


def test_queue_size_is_num_enqueued(eq):
    """Test if the size is equal to the num of items enqueued."""
    eq.enqueue('a')
    eq.enqueue('b')
    eq.enqueue('c')
    assert len(eq) == 3


def test_queue_dequeue_removes_last_item_in_queue(eq):
    """Test dequeue removed last item in the queue."""
    eq.enqueue('a')
    eq.enqueue('b')
    eq.enqueue('c')
    assert eq.dequeue() == 'a'


def test_queue_dequeue_removes_item_in_if_only_item(eq):
    """Test dequeue when only one item in queue."""
    eq.enqueue('hooray!')
    assert eq.dequeue() == 'hooray!'


def test_queue_dequeue_raises_indexerror_if_empty(eq):
    """Test if empty queue riases exception on dequeue."""
    with pytest.raises(IndexError):
        eq.dequeue()


def test_queue_peek_return_none_on_empty_queue(eq):
    """Test peeks returns none if queue is empty."""
    assert eq.peek() is None


def test_queue_peek_return_value_single_item_queue(eq):
    """Test if one item in queue, peek will show it."""
    eq.enqueue('hot-dang')
    assert eq.peek() == 'hot-dang'


def test_queue_peek_return_first_item_in_queue(eq):
    """Test if one item in queue, peek will show it."""
    eq.enqueue('a')
    eq.enqueue('b')
    eq.enqueue('c')
    eq.enqueue('z')
    assert eq.peek() == 'a'


def test_queue_size_empty_queue_is_zero(eq):
    """Test size of empty queue is zero."""
    assert eq.size() == 0


def test_queue_use_len_function_in_python_empty_queue(eq):
    """Test that len() can be called on queue."""
    assert len(eq) == 0


def test_queue_use_len_function_in_python_with_values(eq):
    """Test that len() can be called on queue."""
    eq.enqueue('a')
    eq.enqueue('b')
    eq.enqueue('c')
    eq.enqueue('z')
    assert len(eq) == 4
