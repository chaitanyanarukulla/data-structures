"""Test stack.py class constructor."""
import pytest
from stack import Stack


# @pytest.fixture()
# def empty_stack():
#     """Build an empty stack for testing."""
#     s = Stack()
#     return s


def test_create_stack_len_at_0():
    """Check if len returns stack length at 0."""
    s = Stack()
    assert len(s) == 0


LENGTH = [
    (0, 1),
    ([1, 2], 2),
    (['flerg', 'the', 'blerg'], 3),
    ([1, 2, 3, 4, 5, 6, 7], 7)
]


@pytest.mark.parametrize('val, result', LENGTH)
def test_create_stack_len(val, result):
    """Check if len returns stack length."""
    s = Stack(val)
    assert len(s) == result


@pytest.mark.parametrize('val, result', LENGTH)
def test_create_stack_len_is_same_as_num_pushed_values(val, result):
    """Check if len returns stack length."""
    s = Stack(val)
    assert len(s) == result


POP = [
    (5, 5),
    ([1, 2], 2),
    (['flerg', 'the', 'blerg'], 'blerg'),
    ([1, 2, 3, 4, 5, 6, 7], 7)
]


@pytest.mark.parametrize('val, result', POP)
def test_stack_pop_returns_head(val, result):
    """Check if len returns stack length."""
    s = Stack(val)
    assert s.pop() == result


PUSH = [
    ([1, 2], 2),
    (['flerg', 'the', 'blerg'], 3),
    ([1, 2, 3, 4, 5, 6, 7], 7)
]


@pytest.mark.parametrize('val, result', PUSH)
def test_push_val_into_stack(val, result):
    """Check if push function workds."""
    s = Stack()
    for i in val:
        s.push(val)
    assert len(s) == result
