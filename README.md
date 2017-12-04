#Binary Search Tree

To create an instance if the binary search tree, Bst(), from python:

new = Bst() *you may not call Bst() no parameters or with an iterable item containing unique integers.*

Bst() contains the following methods:
* _insert(val) (Olog(n))_ - will insert the value ‘val’ in the appropriate position in the tree.
* _search(val) (0log(n))_ - will find a given value in the tree, if not in tree will return none.
* _size() (O(1))_ - will return the size of the tree.
* _depth(root) (0(n))_ - returns the depth of the tree.
* _contains(val) (Olog(n))_ - will return true or false if value is in tree.
*_ balance() (0(n))_ - returns the depth of the left minus the right side of the tree as an integer.
* _in_order() (O(n))_ - returns tree in order of lowest to highest value.
* _pre_order() (0(n)(log(n)))_ - returns  parentnode to childnodes from left to right side.
* _post_order() (O(n)log(n)))_ - returns childnodes to parent from left  to right side.
*_ breadth_first() (0(n))_ - returns generator of tree ordered from root .
*_delete(val) (0log(n))_ -will delete a given value in a tree, if not in tree will return None

To access any contained methods:
new.insert(val)
new.search(val)
new.size()
new.depth(root)
new.contains(val)
new.balance()
new.in_order()
new.pre_order()
new.post_order()
new.breadth_first()
new.delete()