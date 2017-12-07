"""Test bubble sort."""
from random import randint

from bubble_sort import bubble_sort


def test_bubble_sort_on_empty_list_returns_empty():
    """Test bubble sort on empty list retruns empty list."""
    test = []
    assert bubble_sort(test) == []


def test_bubble_sort_on_list_of_three():
    """Test bubble sort on list of three retuned sorted."""
    test = [6, 8, 2]
    assert bubble_sort(test) == [2, 6, 8]


def test_bubble_sort_with_sorted_list_no_change():
    """Test bubble sort with sorted list returns no change."""
    test = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert bubble_sort(test) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_bubble_sort_on_reverse_sort_returns_sorted():
    """Test bubble sort with reverse sort returns sorted."""
    test = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert bubble_sort(test) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_bubble_sort_on_list_of_100_rand_int_returns_sorted():
    """Test random list of 100 returns sorted."""
    test = [randint(1, 10000) for x in range(100)]
    assert bubble_sort(test) == sorted(test)


def test_bubble_sort_on_list_of_1000_rand_int_returns_sorted():
    """Test random list of 1000 returns sorted."""
    test = [randint(1, 10000) for x in range(1000)]
    assert bubble_sort(test) == sorted(test)


def test_bubble_sort_of_all_nums_same_returns_same():
    """Test bubble sort if all nums same returns the same."""
    test = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert bubble_sort(test) == test


def test_bubble_sort_with_one_variant_returns_sorted():
    """Test bubble sort with one variant returns sorted."""
    test = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
    assert bubble_sort(test) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
