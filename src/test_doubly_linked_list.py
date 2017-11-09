"""Test doubly_linked_list.py."""
import pytest
from doubly_linked_list import Node
from doubly_linked_list import Dll


def test_node_has_attributes():
    """A node must have a data, next, previous attribute."""
    new = Node()
    assert hasattr(new, 'data')
    assert hasattr(new, 'next')
    assert hasattr(new, 'prve')


def test_dll_has_no_head():
    """New Dll should have a head."""
    l = Dll()
    assert l.head is None


def test_dll_has_tail():
    """New Dll should have a head."""
    l = Dll()
    assert l.tail is None


def test_dll_push_adds_new_item():
    """New item should become new head of list."""
    l = Dll()
    l.push('val')
    assert l.head.data == 'val'


def test_dll_push_two_values_in_last_is_head():
    """New item should become new head of list."""
    l = Dll()
    l.push('val')
    l.push('val2')
    assert l.head.data == 'val2'


def test_dll_push_two_values_in_first_is_tail():
    """New item should become new head of list."""
    l = Dll()
    l.push('val')
    l.push('val2')
    assert l.tail.data == 'val'


def test_dll_push_moves_old_head_to_new_next():
    """New item should become new head of list."""
    l = Dll()
    l.push('val')
    l.push('val2')
    assert l.head.next.data == 'val'


def test_dll_push_moves_new_head_to_new_prev():
    """New item should become new head of list."""
    l = Dll()
    l.push('val')
    l.push('val2')
    assert l.tail.prve.data == 'val2'


def test_dll_append_two_values_in_last_is_tail():
    """New item should become new tail of list."""
    l = Dll()
    l.append('val')
    l.append('val2')
    assert l.tail.data == 'val2'


def test_dll_append_two_values_in_first_is_head():
    """Last item should become new head of list."""
    l = Dll()
    l.append('val')
    l.append('val2')
    assert l.head.data == 'val'


def test_dll_append_moves_old_tail_to_new_previous():
    """New item should become new tail of list."""
    l = Dll()
    l.append('val')
    l.append('val2')
    assert l.tail.prve.data == 'val'


def test_dll_append_moves_new_nove_to_tail():
    """New item should become new head of list."""
    l = Dll()
    l.append('val')
    l.append('val2')
    assert l.tail.data == 'val2'


def test_dll_pop_removes_head():
    """Test Dll for pop function and if it removes the head."""
    l = Dll()
    l.push('val')
    l.pop()
    assert l.head is None


def test_dll_shift_removes_tail():
    """Test Dll for pop function and if it removes the tail."""
    l = Dll()
    l.push('val')
    l.shift()
    assert l.tail is None


def test_dll_pop_returns_removed_head():
    """Test Dll for pop function if it returns proper head."""
    l = Dll()
    l.push('val')
    former_head = l.pop()
    assert former_head.data == 'val'


def test_dll_pop_with_multiple_items_in_list():
    """Test Dll for pop with multiple items in list."""
    l = Dll()
    l.push('val')
    l.push('val2')
    former_head = l.pop()
    assert l.head.data == 'val'


def test_dll_shift_returns_removed_tail():
    """Test Dll for pop function if it returns proper head."""
    l = Dll()
    l.push('val')
    former_tail = l.shift()
    assert former_tail.data == 'val'


def test_dll__with_multiple_items_in_list():
    """Test Dll for pop with multiple items in list."""
    l = Dll()
    l.push('val')
    l.push('val2')
    former_head = l.shift()
    assert l.tail.data == 'val2'


def test_dll_pop_on_empty_list_returns_exception():
    """Test Dll for pop on empty list if it returns exception."""
    l = Dll()
    with pytest.raises(IndexError):
        l.pop()


def test_dll_shift_on_empty_list_returns_exception():
    """Test Dll for pop on empty list if it returns exception."""
    l = Dll()
    with pytest.raises(IndexError):
        l.pop()


@pytest.mark.parametrize('n', range(20))
def test_dll_len_uses_length_function(n):
    """Test Dll should successfully interact with the len() in Python."""
    l = Dll()
    for i in range(n):
        l.push(i)
    assert len(l) == n


def test_dll_remove_node_removes_input_value():
    """Test Dll to remove node by value."""
    l = Dll()
    for i in range(10):
        l.push(i)
    assert l.remove(3).data == 3


def test_dll_remove_node_removes_head_value():
    """Test Dll to remove head."""
    l = Dll()
    l.push('val')
    assert l.remove('val').data == 'val'


def test_linked_list_remove_node_raises_valueerror_if_input_not_exist():
    """Test Dll to remove node raises ValueError if input not exist."""
    l = Dll()
    for i in range(10):
        l.append(i)
    with pytest.raises(ValueError):
        l.remove(17)
