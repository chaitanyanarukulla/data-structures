"""Test binary search tree."""
import pytest


@pytest.fixture
def bst():
    """Initialize empty binary search tree to test."""
    from bst import Bst
    return Bst()


@pytest.fixture
def bst_is_full():
    """Create binary search tree with values and full."""
    from bst import Bst
    new = Bst()
    new.insert(20)
    new.insert(100)
    new.insert(100000)
    return new


@pytest.fixture
def bst_test():
    """Create bst will values for tests."""
    from bst import Bst
    new = Bst()
    new.insert(50)
    new.insert(40)
    new.insert(60)
    new.insert(20)
    new.insert(100)
    new.insert(11)
    new.insert(500)
    new.insert(10)
    new.insert(80)
    new.insert(9999)
    return new


def test_initialize_bst_returns_empty_binary_search_tree(bst):
    """Test initialize empty binary search tree returns empty."""
    assert bst.root is None


def test_initialize_bst_iteratble_root_is_first_item():
    """Test initialize root is first item in binary search tree."""
    from bst import Bst
    tree = Bst([10, 26, 13, 77, 98, 1])
    assert tree.root.data == 10


def test_initialize_bst_iteratble_returns_size_n():
    """Test initialize with iterable returns proper size tree."""
    from bst import Bst
    tree = Bst([1, 2, 3, 4, 5])
    assert tree._size == 5


def test_size_returns_0_if_bst_is_empty(bst):
    """Test size method returns 0 on empty tree."""
    assert bst.size() == 0


def test_size_returns_10_if_insert_manually_10_items(bst_test):
    """Test if 10 items inserted that size is 10."""
    assert bst_test.size() == 10


def test_insert_10_items_returns_first_in_as_root(bst_test):
    """Test that root is first in if 10 items inserted."""
    assert bst_test.root.data == 50


def test_insert_identicle_values_raise_valueerror(bst):
    """Test insert same values raises value error."""
    bst.insert(1)
    with pytest.raises(ValueError):
        bst.insert(1)


def test_insert_non_int_raises_valueerror(bst):
    """Test insert non number raises value error."""
    with pytest.raises(ValueError):
        bst.insert('not number')


def test_insert_iterable_raises_valueerror(bst):
    """Test insert iterable raises appropriate error."""
    with pytest.raises(ValueError):
        bst.insert([1, 3, 5, 9])


def test_search_node_on_empty_tree_returns_none(bst):
    """Test search on empty tree returns none."""
    assert bst.search(10) is None


def test_search_node_not_in_tree_returns_none(bst_is_full):
    """Test search for node not in tree returns none."""
    assert bst_is_full.search(1) is None


def test_search_val_in_tree_returns_node(bst_is_full):
    """Test search for val in tree returns node."""
    bst_is_full.insert(5)
    assert isinstance(bst_is_full.search(5), object)


def test_search_val_in_tree_retruns_node_with_data(bst_is_full):
    """Test search for val in tree returns node with data of val."""
    bst_is_full.insert(5)
    assert bst_is_full.search(5).data == 5


def test_depth_returns_int_of_total_depth_of_tree(bst_is_full):
    """Test depth returns integer of depth of tree."""
    assert bst_is_full.depth(bst_is_full.root) == 2


def test_depth_empty_tree_returns_none(bst):
    """Test depth on epmty tree returns None."""
    assert bst.depth(bst.root) == 0


def test_depth_on_large_tree_returns_full_size(bst_test):
    """Test depth on large tree returns actual size."""
    assert bst_test.depth(bst_test.root) == 4


def test_depth_of_tree_with_only_root_is_0(bst):
    """Test if only root in tree that depth is 0."""
    bst.insert(1)
    assert bst.depth(bst.root) == 0


def test_contains_returns_false_if_val_not_in_tree(bst_test):
    """Test contains returns false if val not in tree."""
    assert bst_test.contains(102948686) is False


def test_contains_returns_false_if_non_int_entered(bst_test):
    """"Test contains returns false if non int entered."""
    assert bst_test.contains('pie') is False


def test_contains_returns_true_if_val_in_tree(bst_test):
    """Test contains returns true if val in tree."""
    assert bst_test.contains(40) is True
    assert bst_test.contains(50) is True
    assert bst_test.contains(60) is True


def test_balance_returns_int(bst_test):
    """Test balancde returns int.."""
    assert isinstance(bst_test.balance(), int)


def test_balance_returns_int_of_r_minus_l_of_tree(bst_test):
    """Test balance returns int of left minus right sides of tree."""
    assert bst_test.balance() == 0


def test_balance_returns_int_of_r_minus_l_of_tree_three(bst):
    """Test balance returns int of left minus right sides of tree."""
    bst.insert(1)
    bst.insert(2)
    bst.insert(3)
    bst.insert(4)
    assert bst.balance() == 2
