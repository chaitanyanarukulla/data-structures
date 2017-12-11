"""Test binheap.py."""
import pytest


def test_initialize_empty_heap(ebh):
    """Test if init binary is empty."""
    assert ebh


def test_push_one_value(ebh):
    """Test size after push one value into heap."""
    ebh.push(9)
    assert ebh._size == 1


def test_push_mulitp_value(ebh):
    """Test size after push multiple values into heap."""
    for i in range(20):
        ebh.push(i)
    assert ebh._size == 20


def test_push_one_non_num(ebh):
    """Test for erron if pushing non numerical value into heap."""
    with pytest.raises(ValueError):
        ebh.push('NOOOOOOOO!!!!!!!!!')


def test_push_iterable():
    """Test if push successfully takes iterable."""
    from binheap import Binheap
    heap = Binheap([1, 2, 3, 4, 5, 6, 7, 8])
    assert heap._size == 8


def test_pop_on_empty_heap_raises_indexerror(ebh):
    """Test for index error trying to pop from empty heap."""
    with pytest.raises(IndexError):
        ebh.pop()


def test_pop_on_heap_with_one_item(ebh):
    """Test pop returns item when only one item in heap."""
    ebh.push(1)
    assert ebh.pop() == 1


def test_pop_twice_on_heap_with_one_item(ebh):
    """Test pop on fully popped heap."""
    ebh.push(1)
    ebh.pop()
    with pytest.raises(IndexError):
        ebh.pop()


def test_pop_returns_sorted_values():
    """Test pop entire bin returns sorted values."""
    from binheap import Binheap
    import random
    rand_nums = list(set([random.randint(0, 1000)
                     for i in range(20)]))
    heap = Binheap(rand_nums)
    # import pdb; pdb.set_trace()
    all_popped = [heap.pop() for i in range(heap._size)]
    assert all_popped == sorted(rand_nums)


def test_pop_returns_sorted_values_limited(ebh):
    """Test pop in controlled environment."""
    ebh.push(23),
    ebh.push(2),
    ebh.push(30),
    ebh.push(50),
    ebh.push(6),
    ebh.push(17),
    ebh.push(29)
    all_popped = [ebh.pop() for i in range(7)]
    assert all_popped == [2, 6, 17, 23, 29, 30, 50]


def test_push_pop_():
    """Test push iterable and pop."""
    from binheap import Binheap
    b = Binheap([5, 546, 7, 3, 54, 376, 87, 432, 432, 543,
                 654, 63, 32, 325, 4, 654, 234, 32, 543, 6, 2,
                 2, 4, 6, 87, 5, 6, 34, 668, 675, 5])
    out = [2, 2, 3, 4, 4, 5, 5, 5, 6, 6, 6, 7, 32, 32, 34, 54,
           63, 87, 87, 234, 325, 376, 432, 432, 543, 543, 546,
           654, 654, 668, 675]
    assert out == [b.pop() for x in out]
