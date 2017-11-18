"""Test deque.py."""
import pytest


def initialize_deque(ed):
    """Test if new empty deque is created."""
    assert ed


def test_append_one_value(ed):
    """Test if append adds value to end of deque."""
    ed.append('val')
    assert ed.peek() == 'val'
    assert ed.size() == 1


def test_append_many_values(ed):
    """Test if append adds value to end of deque."""
    ed.append('val')
    ed.append(3)
    ed.append('thing')
    assert ed.size() == 3


def test_appendleft_one_value(ed):
    """Test if appendleft adds value to font of deque."""
    ed.append('val')
    assert ed.peek() == 'val'
    assert ed.size() == 1


def test_appendleft_many_values(ed):
    """Test if appendleft adds value to front of deque."""
    ed.append('val')
    ed.append(3)
    ed.append('thing')
    assert ed.size() == 3


def test_pop_with_one_item_returns_item(ed):
    """Test is pop returns item of deque with one item."""
    ed.append('one')
    assert ed.pop() == 'one'


def test_pop_with_manys_items_returns_first(ed):
    """Test is pop returns first item of deque with many items."""
    ed.append('one')
    ed.append('two')
    ed.append('buckle_my_shoe')
    assert ed.pop() == 'buckle_my_shoe'


def test_pop_empty_deque_raises_indexerror(ed):
    """Test is pop raises index error on emtpy deque."""
    with pytest.raises(IndexError):
        ed.pop()


def test_pop_all_items_in_deque(ed):
    """Test is pop raises index error if pop too many items."""
    ed.append('one')
    ed.append('two')
    ed.append('buckle_my_shoe')
    ed.pop()
    ed.pop()
    ed.pop()
    with pytest.raises(IndexError):
        ed.pop()


def test_shift_with_one_item_returns_item(ed):
    """Test is pop returns item of deque with one item."""
    ed.append('one')
    assert ed.popleft() == 'one'


def test_shift_with_manys_items_returns_first(ed):
    """Test is shift returns last item of deque with many items."""
    ed.append('one')
    ed.append('two')
    ed.append('buckle_my_shoe')
    assert ed.popleft() == 'one'


def test_shift_empty_deque_raises_indexerror(ed):
    """Test is shift raises index error on emtpy deque."""
    with pytest.raises(IndexError):
        ed.popleft()


def test_shift_all_items_in_deque(ed):
    """Test is shift returns  item of deque with many items."""
    ed.append('one')
    ed.append('two')
    ed.append('buckle_my_shoe')
    ed.popleft()
    ed.popleft()
    ed.popleft()
    with pytest.raises(IndexError):
        ed.popleft()


def test_peek_shows_the_value_to_be_popped(ed):
    """Test if peek shows the next item to be popped."""
    ed.append(1)
    ed.append(2)
    assert ed.peek() == 2


def test_peek_returns_none_if_empty(ed):
    """Test peek returns none on empty deque."""
    assert ed.peek() is None


def test_peek_returns_only_value_if_one_item(ed):
    """Test peek returns only value if one item in deque."""
    ed.append('theone')
    assert ed.peek() is 'theone'


def test_peekleft_shows_the_value_to_be_popped(ed):
    """Test if peek left shows the next item to be popped."""
    ed.append(1)
    ed.append(2)
    assert ed.peekleft() == 1


def test_peekleft_returns_none_if_empty(ed):
    """Test peek left returns none on empty deque."""
    assert ed.peekleft() is None


def test_peekleft_returns_only_value_if_one_item(ed):
    """Test peek left returns only value if one item in deque."""
    ed.append('theone')
    assert ed.peekleft() is 'theone'


def test_size_returns_zero_on_empty_deque(ed):
    """Test size returns 0 on empty deque."""
    assert ed.size() == 0


def test_size_returns_num_items_in_deque(ed):
    """Test size returns total num of itmes in deque."""
    ed.append(1)
    ed.append(2)
    ed.append(3)
    assert ed.size() == 3
