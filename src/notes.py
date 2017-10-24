"""Tests"""

import pytest

def test_node_has_attributes():
    """A node must have a data and next attribute"""
    from linked_list import Node
    new = Node()
    assert hasattr(new, 'data')
    assert hasattr(new, 'next')


def test_linked_list_has_head():
    """New linked list should have a head"""
    from linked_list import LinkedList
    l = LinkedList()
    assert l.head is None


def test_linked_list_push_adds_new_item():
    """New item should become new head of list"""
    from linked_list import LinkedList
    l = LinkedList()
    l.push('val')
    assert l.head.data == 'val'


def test_linked_list_push_two_values_in_last_is_head():
    """New item should become new head of list"""
    from linked_list import LinkedList
    l = LinkedList()
    l.push('val')
    l.push('val2')
    assert l.head.data == 'val2'


def test_linked_list_push_moves_old_head_to_new_next():
    """New item should become new head of list"""
    from linked_list import LinkedList
    l = LinkedList()
    l.push('val')
    l.push('val2')
    assert l.head.next.data == 'val'


def test_linked_list_pop_removes_head():
    """."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push('val')
    l.pop()
    assert l.head is None


def test_linked_list_pop_returns_removed_head():
    """."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push('val')
    former_head = l.pop()
    assert former_head = 'val'


def test_linked_list_pop_with_multiple_items_in_list():
    """."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push('val')
    l.push('val2')
    former_head = l.pop()
    assert former_head.next = 'val'


def test_linked_list_pop_on_empty_list_returns_exception():
    """."""
    from linked_list import LinkedList
    l = LinkedList()
    with pytest.raises(IndexError):
        l.pop()


def test_linked_list_size_returns_none_on_empty_list():
    """."""
    from linked_list import LinkedList
    l = LinkedList()
    assert l.size() == 0


@pytest.mark.parametetrize('n', range(20))
def test_linked_list_size_returns_list_length():
    """Linked List should calculate its own size."""
    from linked_list import LinkedList
    l = LinkedList()
    for i in range(n):
        l.push(i)
    assert l.size() == n


@pytest.mark.parametetrize('n', range(20))
def test_linked_list_len_uses_length_function():
    """Linked List should successfully interact with the len() in Python."""
    from linked_list import LinkedList
    l = LinkedList()
    for i in range(n):
        l.push(i)
    assert len(l) == n


def test_linked_list_search_empty_returns_none():
    """."""
    from linked_list import LinkedList
    l = LinkedList()
    assert l.search(0) is None


def test_linked_list_search_one_node_list_returns_head():
    """."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push('val')
    assert l.search('val') == l.head


@pytest.mark.parametetrize('n', range(1, 10))
def test_linked_list_search_returns_input_value():
    """."""
    from linked_list import LinkedList
    from random import randint
    l = LinkedList()
    for i in range(1, n + 1):
        l.push('n')
    searching = randint(1, n)
    assert l.search(searching) == searching


def test_linked_list_accepts_iterables():
    """."""
    from linked_list import LinkedList
    the_list = [1, 2, 3, 4, 5]
    l = LinkedList(the_list)
    for item in the_list:
        assert l.search(item).data == item

        
def test_linked_list_accepts_each_iterable_value():
    """."""
    from linked_list import LinkedList
    the_list = [1, 2, 3, 4, 5]
    l = LinkedList(the_list)
    for item in the_list:
        assert l.search(item).data == item

