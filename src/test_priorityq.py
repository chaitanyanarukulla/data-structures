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


def test_priorityq_insert_with_many_priority_returns_higest(pq):
    """Test ipriorityq insert with many priority returns higest pirority."""
    pq.insert('hi', -10)
    pq.insert('one', 1)
    pq.insert('four', 4)
    pq.insert('eight', 8)
    assert pq._highest == -10


def test_priorityq_insert_with_many_priority_returns_lowest(pq):
    """Test ipriorityq insert with many priority returns lowest pirority."""
    pq.insert('hi', -10)
    pq.insert('one', 1)
    pq.insert('four', 4)
    pq.insert('eight', 8)
    assert pq._lowest == 8


def test_priorityq_insert_with_same_priority_returns_list_of_val(pq):
    """Test if inserted with same priority returns list of val in pirority."""
    pq.insert('hi', -10)
    pq.insert('one', -10)
    pq.insert('four', 4)
    pq.insert('eight', 4)
    assert pq._que[-10] == ['hi', 'one']


def test_if_pop_raises_indexerror_on_empty_prorityq(pq):
    """Test if pop reises indexerroe."""
    with pytest.raises(IndexError):
        pq.pop()


def test_priorityq_pop_function_pops(pq):
    """Test ipriorityq if it pops a val."""
    pq.insert('hi', -10)
    pq.insert('one', 1)
    pq.pop()
    pq.pop()
    assert pq._que == {}


def test_priorityq_pop_function_returns_val(pq):
    """Test ipriorityq if it pops and returns the right val."""
    pq.insert('hi', -10)
    pq.insert('one', 1)
    assert pq.pop() == 'hi'


def test_pop_if_more_poped_then_inserted_raises_error(pq):
    """Test if inserted with same priority returns list of val in pirority."""
    pq.insert('hi', -10)
    pq.insert('one', -10)
    pq.insert('four', 4)
    pq.pop()
    pq.pop()
    pq.pop()
    with pytest.raises(IndexError):
        pq.pop()


def test_pop_if_returns_in_prioety_order(pq):
    """Test if inserted with priority returns in priority order."""
    pq.insert('hi', -10)
    pq.insert('one', -1)
    pq.insert('four', 4)
    pop1 = pq.pop()
    pop2 = pq.pop()
    pop3 = pq.pop()
    assert pop1 == 'hi'
    assert pop2 == 'one'
    assert pop3 == 'four'


def test_pop_if_returns_in_prioety_order_pop_in_and_out(pq):
    """Test if inserted val with priority returns in priority order."""
    pq.insert('hi', -10)
    pq.insert('four', 4)
    pq.insert('one', -1)
    pop1 = pq.pop()
    pop2 = pq.pop()
    pq.insert('first', -20)
    pop3 = pq.pop()
    pq.insert('last', 20)
    pop4 = pq.pop()
    assert pop1 == 'hi'
    assert pop2 == 'one'
    assert pop3 == 'first'
    assert pop4 == 'four'


def test_peek_returns_the_higest_priority_val(pq):
    """Test if peek returns the val in line to be poped."""
    pq.insert('hi', -10)
    pq.insert('one', 1)
    pq.insert('four', 4)
    assert pq.peek() == 'hi'


def test_peek_empty_pq_returns_none(pq):
    """Test if peek returns empty list on peek empty pq."""
    with pytest.raises(IndexError):
        pq.peek()


def test_peek_after_insert_and_pop_returns_highest_priority_item(pq):
    """Test peek returns highest priority item after insert and pop used."""
    pq.insert('hi', -10)
    pq.insert('four', 4)
    pq.insert('one', -1)
    pop1 = pq.pop()
    pop2 = pq.pop()
    assert pq.peek() == 'four'
    pq.insert('first', -20)
    assert pq.peek() == 'first'
    pop3 = pq.pop()
    pq.insert('last', 20)
    assert pq.peek() == 'four'


def test_peek_on_priority_with_multiple_values(pq):
    """Test peek shows first item in on a priority with many values."""
    pq.insert('hi', 5)
    pq.insert('howdy', 5)
    pq.insert('hola', 5)
    pq.insert('hey', 5)
    pq.insert('heyo', 5)
    assert pq.peek() == 'hi'
