"""Test self-balancing binary search tree."""


def test_bst_full_now_balanced(bst_full):
    """Test imbalanced bst becomes balanced."""
    output = []
    g = bst_full.breadth_first()
    for i in range(3):
        output.append(next(g))
    assert output == [908543, 3254, 58490543]
