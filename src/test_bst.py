"""Test binary search tree."""
import pytest


def test_initialize_bst_returns_empty_bst(bst):
    """Test initialize empty bst returns empty bst."""
    assert bst.root is None


def test_initialize_bst_iteratble_returns_size_n():
    """Test initialize with iterable returns proper size tree."""
    from bst import Bst
    tree = Bst([2, 6, 3, 7, 8, 1])
    assert tree._size == 6


def test_initialize_bst_iteratble_root_is_first_item():
    """Test initialize with iterable root is first item in."""
    from bst import Bst
    tree = Bst([2, 6, 3, 7, 8, 1])
    assert tree.root.data == 2


def test_size_returns_0_if_bst_is_empty(bst):
    """Test size method returns 0 on empty tree."""
    assert bst.size() == 0


def test_size_returns_appropriate_size_after_iterable():
    """Test size returns proper size when initiated by iterable."""
    from bst import Bst
    tree = Bst([2, 6, 3, 7, 8, 1])
    assert tree.size() == 6


def test_size_returns_10_if_insert_manually_10_items(bst_big):
    """Test if 10 items inserted that size is 10."""
    assert bst_big.size() == 10


def test_insert_10_items_returns_first_in_as_root(bst_big):
    """Test that root is first in if 10 items inserted."""
    assert bst_big.root.data == 50


def test_insert_identicle_values_raise_valueerror(bst):
    """Test insert same values raises value error."""
    bst.insert(1)
    with pytest.raises(ValueError):
        bst.insert(1)


def test_insert_non_int_raises_valueerror(bst):
    """Test insert non number raises value error."""
    with pytest.raises(ValueError):
        bst.insert('howdy')


def test_insert_iterable_raises_valueerror(bst):
    """Test insert iterable raises appropriate error."""
    with pytest.raises(ValueError):
        bst.insert([1, 3, 5, 9])


def test_search_node_on_empty_tree_returns_none(bst):
    """Test search on empty tree returns none."""
    assert bst.search(10) is None


def test_search_node_not_in_tree_returns_none(bst_full):
    """Test search for node not in tree returns none."""
    assert bst_full.search(1) is None


def test_search_for_non_int_returns_non(bst_full):
    """Test search for non number returns none."""
    assert bst_full.search('cake') is None


def test_search_val_in_tree_returns_node(bst_full):
    """Test search for val in tree returns node."""
    bst_full.insert(5)
    assert isinstance(bst_full.search(5), object)


def test_search_val_in_tree_retruns_node_with_data(bst_full):
    """Test search for val in tree returns node with data of val."""
    bst_full.insert(5)
    assert bst_full.search(5).data == 5


def test_depth_returns_int_of_total_depth_of_tree(bst_full):
    """Test depth returns integer of depth of tree."""
    assert bst_full.depth(bst_full.root) == 3


def test_depth_empty_tree_returns_none(bst):
    """Test depth on epmty tree returns None."""
    assert bst.depth(bst.root) == 0


def test_depth_on_large_tree_returns_full_size(bst_big):
    """Test depth on large tree returns actual size."""
    assert bst_big.depth(bst_big.root) == 5


def test_depth_of_tree_with_only_root_is_0(bst):
    """Test if only root in tree that depth is 0."""
    bst.insert(1)
    assert bst.depth(bst.root) == 0


def test_contains_returns_false_if_val_not_in_tree(bst_big):
    """Test contains returns false if val not in tree."""
    assert bst_big.contains(102948686) is False


def test_contains_returns_false_if_non_int_entered(bst_big):
    """"Test contains returns false if non int entered."""
    assert bst_big.contains('pie') is False


def test_contains_returns_true_if_val_in_tree(bst_big):
    """Test contains returns true if val in tree."""
    assert bst_big.contains(40) is True
    assert bst_big.contains(50) is True
    assert bst_big.contains(68) is True


def test_balance_returns_string_if_bst_is_empty(bst):
    """Test balance returns none if bst is empty."""
    assert bst.balance(bst.root) == 'There are no nodes in this tree.'


def test_balance_returns_int(bst_big):
    """Test balancde returns int.."""
    assert isinstance(bst_big.balance(bst_big.root), int)


def test_balance_returns_int_of_r_minus_l_of_tree(bst_big):
    """Test balance returns int of left minus right sides of tree."""
    assert bst_big.balance(bst_big.root) == -1


def test_balance_returns_int_of_r_minus_l_of_tree_two(bst_full, bst):
    """Test balance returns int of left minus right sides of tree."""
    bst.insert(2)
    bst.insert(1)
    bst.insert(3)
    assert bst.balance(bst.root) == 0
    assert bst_full.balance(bst_full.root) == -2


def test_balance_returns_int_of_r_minus_l_of_tree_three(bst):
    """Test balance returns int of left minus right sides of tree."""
    bst.insert(1)
    bst.insert(2)
    bst.insert(3)
    bst.insert(4)
    bst.insert(5)
    bst.insert(6)
    bst.insert(7)
    assert bst.balance(bst.root) == -6


def test_breadth_first_returns_object(bst_big):
    """Test breadth first returns generator object."""
    b = bst_big.breadth_first()
    assert isinstance(b, object)


def test_breadth_first_is_valid_generator(bst_big):
    """Test breadth first returns valid generator."""
    g = bst_big.breadth_first()
    assert next(g) == 50


def test_breadth_first_return_children_l_to_r(bst_big):
    """Test breadth first returns all children l to r."""
    g = bst_big.breadth_first()
    output = []
    for i in range(10):
        output.append(next(g))
    assert output == [50, 40, 68, 10, 110, 1, 18, 80, 500, 5000]


def test_breadth_first_on_empty_bst_raises_value_error(bst):
    """Test breadth first search raises value error if bst empty."""
    g = bst.breadth_first()
    with pytest.raises(ValueError):
        next(g)


def test_in_order_returns_object(bst):
    """Test in order returns object."""
    g = bst.in_order()
    assert isinstance(g, object)


def test_in_order_is_valid_generator(bst_big):
    """Test in order returns valid generator."""
    g = bst_big.in_order()
    assert next(g) == 1


def test_in_order_returns_tree_in_ascending_order(bst_big):
    """Test in order returns ordered vals."""
    g = bst_big.in_order()
    output = []
    for i in range(10):
        output.append(next(g))
    assert output == [1, 10, 18, 40, 50, 68, 80, 110, 500, 5000]


def test_in_order_on_empty_bst_raises_value_error(bst):
    """Test in order search raises value error if bst empty."""
    g = bst.in_order()
    with pytest.raises(ValueError):
        next(g)


def test_pre_order_retuns_object(bst):
    """Test pre order returns object."""
    g = bst.pre_order()
    assert isinstance(g, object)


def test_pre_order_returns_valid_generator(bst_big):
    """Test pre order returns valid generator object."""
    g = bst_big.pre_order()
    assert next(g) == 50


def test_pre_order_returns_left_side_of_all_nodes_first(bst_big):
    """Test pre order returns left side of each node first."""
    g = bst_big.pre_order()
    output = []
    for i in range(10):
        output.append(next(g))
    assert output == [50, 40, 10, 1, 18, 68, 110, 80, 500, 5000]


def test_pre_order_returns_proper_order_unabalances(bst_full):
    """Test pre order returns proper order from unbalanced tree."""
    g = bst_full.pre_order()
    output = []
    for i in range(3):
        output.append(next(g))
    assert output == [3254, 908543, 58490543]


def test_pre_order_on_empty_bst_raises_value_error(bst):
    """Test pre order search raises value error if bst empty."""
    g = bst.pre_order()
    with pytest.raises(ValueError):
        next(g)


def test_post_order_returns_object(bst):
    """Test post order returns object."""
    g = bst.post_order()
    assert isinstance(g, object)


def test_post_order_returns_valid_generator(bst_big):
    """Test post order returns valid generator object."""
    g = bst_big.post_order()
    assert next(g) == 1


def test_post_order_returns_root_last(bst_big):
    """Test post order returns left side then right with root in middle."""
    g = bst_big.post_order()
    output = []
    for i in range(10):
        output.append(next(g))
    assert output[-1] == 50


def test_post_order_returns_proper_order_unbalanced(bst_full):
    """Test post order returns proper order on unbalanced tree."""
    g = bst_full.post_order()
    output = []
    for i in range(3):
        output.append(next(g))
    assert output == [58490543, 908543, 3254]


def test_post_order_returns_proper_order_on_balanced(bst_big):
    """Test post order returns proper order on balanced tree."""
    g = bst_big.post_order()
    output = []
    for i in range(10):
        output.append(next(g))
    assert output == [1, 18, 10, 40, 80, 5000, 500, 110, 68, 50]


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
    assert bst.size() == 0
    assert bst.search(5) is None


def test_delete_on_root_in_large_bst(bst_big):
    """Test delete on root node in large bst."""
    bst_big.delete(50)
    output = []
    b_output = []
    o = bst_big.in_order()
    b = bst_big.breadth_first()
    for i in range(9):
        output.append(next(o))
        b_output.append(next(b))
    assert bst_big.search(50) is None
    assert 50 not in output
    assert b_output == [68, 40, 110, 10, 80, 500, 1, 18, 5000]


def test_delete_on_node_with_no_chirdren(bst_big):
    """Test delete on node with no children."""
    bst_big.delete(5000)
    output = []
    b_output = []
    o = bst_big.in_order()
    b = bst_big.breadth_first()
    for i in range(9):
        output.append(next(o))
        b_output.append(next(b))
    assert bst_big.search(5000) is None
    assert 5000 not in output
    assert b_output == [50, 40, 68, 10, 110, 1, 18, 80, 500]


def test_delete_on_node_with_one_child_right(bst_big):
    """Test delete on node with only one right child."""
    bst_big.delete(500)
    output = []
    b_output = []
    o = bst_big.in_order()
    b = bst_big.breadth_first()
    for i in range(9):
        output.append(next(o))
        b_output.append(next(b))
    assert bst_big.search(500) is None
    assert 500 not in output
    assert b_output == [50, 40, 68, 10, 110, 1, 18, 80, 5000]


def test_delete_on_node_with_two_children(bst_big):
    """Test delete on node with one left child."""
    bst_big.delete(10)
    output = []
    b_output = []
    o = bst_big.in_order()
    b = bst_big.breadth_first()
    for i in range(9):
        output.append(next(o))
        b_output.append(next(b))
    assert bst_big.search(10) is None
    assert 10 not in output
    assert b_output == [50, 40, 68, 18, 110, 1, 80, 500, 5000]


def test_delete_on_root_unbalanced_left(bst):
    """Test delete when only left nodes."""
    bst.insert(100)
    bst.insert(80)
    bst.insert(60)
    bst.insert(40)
    bst.delete(100)
    assert bst.search(100) is None
    assert bst.size() == 3


def test_delete_on_root_on_unbalanced_right(bst):
    """Test unbalanced when only right nodes."""
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)
    bst.insert(100)
    bst.delete(40)
    assert bst.search(40) is None
    assert bst.size() == 3


def test_delete_back_to_back(bst_big):
    """Test delete multiple times."""
    bst_big.delete(110)
    bst_big.delete(18)
    bst_big.delete(50)
    output = []
    o = bst_big.in_order()
    for i in range(7):
        output.append(next(o))
    assert 110 not in output
    assert 18 not in output
    assert 50 not in output
    assert output == [1, 10, 40, 68, 80, 500, 5000]
    assert bst_big.search(110) is None
    assert bst_big.search(18) is None
    assert bst_big.search(50) is None


def test_delete_one_child_parent_greater(bst_big):
    """Test delete node with one child when parent is greater."""
    bst_big.delete(40)
    assert bst_big.search(40) is None


def test_delete_two_children_if_next_has_one_child(bst_big):
    """Test delete node with one child when parent is greater."""
    bst_big.insert(85)
    bst_big.insert(55)
    bst_big.delete(68)
    assert bst_big.search(68) is None


def test_delete_two_children_if_next_no_child(bst_big):
    """Test delete node with one child when parent is greater."""
    bst_big.insert(55)
    bst_big.delete(68)
    assert bst_big.search(68) is None
