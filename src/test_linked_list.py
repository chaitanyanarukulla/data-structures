"""Tests for linked_list.py."""
import pytest


def test_node_has_attributes():
    """A node must have a data and next attribute."""
    from linked_list import Node
    new = Node()
    assert hasattr(new, 'data')
    assert hasattr(new, 'next')


def test_empty_linked_list_has_no_head():
    """New linked list should have a head."""
    from linked_list import LinkedList
    l = LinkedList()
    assert l.head is None


def test_linked_list_push_adds_new_item():
    """New item should become new head of list."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push('val')
    assert l.head.data == 'val'


def test_linked_list_push_two_values_in_last_is_head():
    """New item should become new head of list."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push('val')
    l.push('val2')
    assert l.head.data == 'val2'


def test_linked_list_push_moves_old_head_to_new_next():
    """New item should become new head of list."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push('val')
    l.push('val2')
    assert l.head.next.data == 'val'


def test_linked_list_pop_removes_head():
    """Test linkedlist for pop function and if it removes the head."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push('val')
    l.pop()
    assert l.head is None


def test_linked_list_pop_returns_removed_head():
    """Test linkedlist for pop function if it returns proper head."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push('val')
    former_head = l.pop()
    assert former_head.data == 'val'


def test_linked_list_pop_with_multiple_items_in_list():
    """Test linkedlist for pop with multiple items in list."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push('val')
    l.push('val2')
    l.pop()
    assert l.head.data == 'val'


def test_linked_list_pop_on_empty_list_returns_exception():
    """Test linkedlist for pop on empty list if it returns exception."""
    from linked_list import LinkedList
    l = LinkedList()
    with pytest.raises(IndexError):
        l.pop()


def test_linked_list_size_returns_none_on_empty_list():
    """Test linkedlist for te size returns none on empty list."""
    from linked_list import LinkedList
    l = LinkedList()
    assert l.size() == 0


@pytest.mark.parametrize('n', range(20))
def test_linked_list_size_returns_list_length(n):
    """Test Linked List should calculate its own size."""
    from linked_list import LinkedList
    l = LinkedList()
    for i in range(n):
        l.push(i)
    assert l.size() == n


@pytest.mark.parametrize('n', range(20))
def test_linked_list_len_uses_length_function(n):
    """Test Linked List should successfully interact with the len()."""
    from linked_list import LinkedList
    l = LinkedList()
    for i in range(n):
        l.push(i)
    assert len(l) == n


def test_linked_list_search_empty_returns_none():
    """Test Linked List for search that empty data returns none."""
    from linked_list import LinkedList
    l = LinkedList()
    assert l.search(0) is None


def test_linked_list_search_one_node_list_returns_head():
    """Test Linked List if it serches node and returns head."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push('val')
    assert l.search('val') == l.head


@pytest.mark.parametrize('n', range(1, 10))
def test_linked_list_search_returns_input_value(n):
    """Test Linked List for search returns input value."""
    from linked_list import LinkedList
    from random import randint
    l = LinkedList()
    for i in range(1, n + 1):
        l.push(i)
    searching = randint(1, n)
    assert l.search(searching).data == searching


def test_linked_list_accepts_iterables():
    """Test Linked List to accepts for iterables."""
    from linked_list import LinkedList
    the_list = [1, 2, 3, 4, 5]
    l = LinkedList(the_list)
    for item in the_list:
        assert l.search(item).data == item


def test_linked_list_accepts_each_iterable_value():
    """Test Linked List if accepts each iterable value."""
    from linked_list import LinkedList
    the_list = [1, 2, 3, 4, 5]
    l = LinkedList(the_list)
    for item in the_list:
        assert l.search(item).data == item


def test_linked_list_remove_removes_input_value():
    """Test Linked List to remove node by value."""
    from linked_list import LinkedList
    the_list = [1, 2, 3, 4, 5]
    l = LinkedList(the_list)
    assert l.remove(l.search(3)).data == 3


def test_linked_list_remove_removes_sets_next_as_head():
    """Test Linked List to remove node removes sets next as head."""
    from linked_list import LinkedList
    the_list = [1, 2, 3, 4, 5]
    l = LinkedList(the_list)
    l.remove(l.search(5))
    assert l.head.data == 4


def test_linked_list_remove_raises_valueerror_if_input_not_exist():
    """Test Linked List to remove node raises ValueError if input not exist."""
    from linked_list import LinkedList
    the_list = [1, 2, 3, 4, 5]
    l = LinkedList(the_list)
    with pytest.raises(ValueError):
        l.remove(7)


def test_linked_list_display_returns_tuple_of_list_values():
    """Test for test linked list display returns tuple of list values."""
    from linked_list import LinkedList
    the_list = [1, 2, 3, 4, 5]
    l = LinkedList(the_list)
    assert l.display() == '(5, 4, 3, 2, 1)'


def test_linked_list_len_returns_list_length():
    """Test linked list for len returns list length."""
    from linked_list import LinkedList
    the_list = [1, 2, 3, 4, 5]
    l = LinkedList(the_list)
    assert len(l) == 5


def test_linked_list_str_calls_display():
    """Test for str calls display."""
    from linked_list import LinkedList
    the_list = [1, 2, 3, 4, 5]
    l = LinkedList(the_list)
    assert str(l) == '(5, 4, 3, 2, 1)'
