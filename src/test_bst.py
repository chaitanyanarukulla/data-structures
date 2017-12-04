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


def test_breadth_first_returns_object(bst_test):
    """Test breadth first returns generator object."""
    b = bst_test.breadth_first()
    assert isinstance(b, object)


def test_breadth_first_is_valid_generator(bst_test):
    """Test breadth first returns valid generator."""
    g = bst_test.breadth_first()
    assert next(g) == 50


def test_breadth_first_on_empty_bst_raises_value_error(bst):
    """Test breadth first search raises value error if bst empty."""
    g = bst.breadth_first()
    with pytest.raises(ValueError):
        next(g)


def test_in_order_returns_object(bst):
    """Test in order returns object."""
    g = bst.in_order()
    assert isinstance(g, object)


def test_in_order_is_valid_generator(bst_test):
    """Test in order returns valid generator."""
    g = bst_test.in_order()
    assert next(g) == 10


def test_in_order_returns_tree_in_ascending_order(bst_test):
    """Test in order returns ordered vals."""
    g = bst_test.in_order()
    output = []
    for i in range(10):
        output.append(next(g))
    assert output == [10, 11, 20, 40, 50, 60, 80, 100, 500, 9999]


def test_in_order_on_empty_bst_raises_value_error(bst):
    """Test in order search raises value error if bst empty."""
    g = bst.in_order()
    with pytest.raises(ValueError):
        next(g)


def test_pre_order_retuns_object(bst):
    """Test pre order returns object."""
    g = bst.pre_order()
    assert isinstance(g, object)


def test_pre_order_returns_valid_generator(bst_test):
    """Test pre order returns valid generator object."""
    g = bst_test.pre_order()
    assert next(g) == 50


def test_pre_order_returns_left_side_of_all_nodes_first(bst_test):
    """Test pre order returns left side of each node first."""
    g = bst_test.pre_order()
    output = []
    for i in range(10):
        output.append(next(g))
    assert output == [50, 40, 20, 11, 10, 60, 100, 80, 500, 9999]


def test_pre_order_returns_proper_order_unabalances(bst_is_full):
    """Test pre order returns proper order from unbalanced tree."""
    g = bst_is_full.pre_order()
    output = []
    for i in range(3):
        output.append(next(g))
    assert output == [20, 100, 100000]


def test_pre_order_on_empty_bst_raises_value_error(bst):
    """Test pre order search raises value error if bst empty."""
    g = bst.pre_order()
    with pytest.raises(ValueError):
        next(g)


def test_post_order_returns_object(bst):
    """Test post order returns object."""
    g = bst.post_order()
    assert isinstance(g, object)


def test_post_order_returns_valid_generator(bst_test):
    """Test post order returns valid generator object."""
    g = bst_test.post_order()
    assert next(g) == 10


def test_post_order_returns_root_last(bst_test):
    """Test post order returns left side then right with root in middle."""
    g = bst_test.post_order()
    output = []
    for i in range(10):
        output.append(next(g))
    assert output[-1] == 50


def test_post_order_returns_proper_order_unbalanced(bst_is_full):
    """Test post order returns proper order on unbalanced tree."""
    g = bst_is_full.post_order()
    output = []
    for i in range(3):
        output.append(next(g))
    assert output == [100000, 100, 20]


def test_post_order_returns_proper_order_on_balanced(bst_test):
    """Test post order returns proper order on balanced tree."""
    g = bst_test.post_order()
    output = []
    for i in range(10):
        output.append(next(g))
    assert output == [10, 11, 20, 40, 80, 9999, 500, 100, 60, 50]


def test_post_order_on_empty_bst_raises_value_error(bst):
    """Test post order search raises value error if bst empty."""
    g = bst.post_order()
    with pytest.raises(ValueError):
        next(g)


def test_delete_empty_tree_returns_none(bst):
    """Test delete on empty tree returns none."""
    assert bst.delete(5) is None


def test_delete_on_tree_with_only_root(bst):
    """Test delete on tree with only root node."""
    bst.insert(5)
    bst.delete(5)
    assert bst.search(5) is None


def test_delete_on_root_in_large_bst(bst_test):
    """Test delete on root node in large bst."""
    bst_test.delete(50)
    output = []
    in_order = bst_test.in_order()
    for i in range(9):
        output.append(next(in_order))
    assert bst_test.search(50) is None
    assert 50 not in output


def test_delete_on_root_unbalanced_left(bst):
    """Test delete when only left nodes."""
    bst.insert(100)
    bst.insert(80)
    bst.insert(60)
    bst.insert(40)
    bst.delete(100)
    assert bst.search(100) is None
    assert bst.size() == 4


def test_delete_two_children_if_next_no_child(bst_test):
    """Test delete node with one child when parent is greater."""
    bst_test.insert(55)
    bst_test.delete(68)
    assert bst_test.search(68) is None


def test_delete_two_children_if_next_has_one_child(bst_test):
    """Test delete node with one child when parent is greater."""
    bst_test.insert(666)
    bst_test.insert(999999)
    bst_test.delete(30)
    assert bst_test.search(30) is None


def test_delete_one_child_parent(bst_test):
    """Test delete node with one child parent."""
    bst_test.delete(40)
    assert bst_test.search(40) is None


def test_delete_muliiple_times(bst_test):
    """Test delete multiple times."""
    bst_test.delete(50)
    bst_test.delete(40)
    bst_test.delete(60)
    bst_test.in_order()
    result = []
    assert 50 not in result
    assert 40 not in result
    assert 60 not in result
    assert bst_test.search(50) is None
    assert bst_test.search(40) is None
    assert bst_test.search(60) is None


def test_delete_last_node_with_no_chirdren(bst_test):
    """Test delete last node with no children."""
    bst_test.delete(9999)
    result = []
    order = bst_test.in_order()
    for i in range(9):
        result.append(next(order))
    assert bst_test.search(9999) is None
    assert 9999 not in result
