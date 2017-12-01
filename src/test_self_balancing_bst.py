# """Test self-balancing binary search tree."""


# def test_bst_imbalance_neg_two_now_balanced(bst_full):
#     """Test imbalanced bst becomes balanced."""
#     output = []
#     g = bst_full.breadth_first()
#     for i in range(3):
#         output.append(next(g))
#     assert output == [908543, 3254, 58490543]


# def test_bst_imbalance_pos_two_now_balanced(bst):
#     """Test left imbalanced bst becomes balanced."""
#     bst.insert(10)
#     bst.insert(8)
#     bst.insert(6)
#     assert bst.root.data == 8
#     assert bst.root.right.data == 10
#     assert bst.root.left.data == 6


# def test_bst_insert_6_larger_nodes_stays_balanced(bst):
#     """Test insert 6 increasingly larger nodes stays balanced."""
#     bst.insert(10)
#     bst.insert(15)
#     bst.insert(20)
#     bst.insert(25)
#     bst.insert(30)
#     bst.insert(35)
#     output = []
#     g = bst.breadth_first()
#     for i in range(6):
#         output.append(next(g))
#     assert output == [25, 15, 30, 10, 20, 35]


# def test_bst_insert_7_larger_nodes_stays_balanced(bst):
#     """Test insert 6 increasingly larger nodes stays balanced."""
#     bst.insert(10)
#     bst.insert(15)
#     bst.insert(20)
#     bst.insert(25)
#     bst.insert(30)
#     bst.insert(35)
#     bst.insert(40)
#     output = []
#     g = bst.breadth_first()
#     for i in range(7):
#         output.append(next(g))
#     assert output == [25, 15, 35, 10, 20, 30, 40]


def test_bst_insert_varied_size_stays_balanced(bst):
    """Test insert varying size nodes stays balanced."""
    bst.insert(10)
    bst.insert(15)
    bst.insert(20)
    bst.insert(25)
    bst.insert(30)
    bst.insert(35)
    bst.insert(40)
    bst.insert(5)
    bst.insert(12)
    output = []
    g = bst.breadth_first()
    for i in range(9):
        output.append(next(g))
    assert output == [25, 15, 35, 10, 20, 30, 40, 5, 12]


def test_bst_says_balanced_after_delete(bst):
    """Test bst balance after delete node."""
    bst.insert(10)
    bst.insert(15)
    bst.insert(20)
    bst.insert(25)
    bst.insert(30)
    bst.insert(35)
    bst.insert(40)
    bst.insert(5)
    bst.insert(12)
    bst.delete(20)
    output = []
    g = bst.breadth_first()
    for i in range(8):
        output.append(next(g))
    assert output == [25, 10, 35, 5, 15, 30, 40, 12]


def test_r_l_rotation_sequence(bst):
    """Test simple tree with right-left rotation."""
    bst.insert(10)
    bst.insert(20)
    bst.insert(15)
    assert bst.root.data == 15
    assert bst.root.right.data == 20
    assert bst.root.left.data == 10


def test_l_r_rotation_sequence(bst):
    """Test simple tree with left-right rotation."""
    bst.insert(10)
    bst.insert(2)
    bst.insert(7)
    assert bst.root.data == 7
    assert bst.root.right.data == 10
    assert bst.root.left.data == 2


def test_tree_after_delete_two_nodes(bst):
    bst.insert(10)
    bst.insert(15)
    bst.insert(20)
    bst.insert(25)
    bst.insert(30)
    bst.insert(35)
    bst.insert(40)
    bst.insert(5)
    bst.insert(12)
    bst.delete(20)
    bst.delete(10)
    output = []
    for i in bst.breadth_first():
        print(i)
        output.append(i)
    assert output == [25, 12, 35, 5, 15, 30, 40]


def test_tree_after_delete_three_nodes(bst):
    """Test balance after deleting three nodes."""
    bst.insert(10)
    bst.insert(15)
    bst.insert(20)
    bst.insert(25)
    bst.insert(30)
    bst.insert(35)
    bst.insert(40)
    bst.insert(5)
    bst.insert(12)
    bst.delete(20)
    bst.delete(10)
    bst.delete(12)
    output = []
    for i in bst.breadth_first():
        print(i)
        output.append(i)
    assert output == [25, 15, 35, 5, 30, 40]


def test_tree_after_delete_four_nodes(bst):
    """Test delete after removing four nodes."""
    bst.insert(10)
    bst.insert(15)
    bst.insert(20)
    bst.insert(25)
    bst.insert(30)
    bst.insert(35)
    bst.insert(40)
    bst.insert(5)
    bst.insert(12)
    bst.delete(20)
    bst.delete(10)
    bst.delete(12)
    bst.delete(5)
    output = []
    for i in bst.breadth_first():
        print(i)
        output.append(i)
    assert output == [25, 15, 35, 30, 40]


def test_tree_after_delete_five_nodes(bst):
    """Test delete after removing five nodes."""
    bst.insert(10)
    bst.insert(15)
    bst.insert(20)
    bst.insert(25)
    bst.insert(30)
    bst.insert(35)
    bst.insert(40)
    bst.insert(5)
    bst.insert(12)
    bst.delete(20)
    bst.delete(10)
    bst.delete(12)
    bst.delete(5)
    bst.delete(15)
    output = []
    for i in bst.breadth_first():
        print(i)
        output.append(i)
    assert output == [35, 25, 40, 30]
