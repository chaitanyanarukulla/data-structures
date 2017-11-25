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

To access any contained methods:
new.insert(val)
new.search(val)
new.size()
new.depth(root)
new.contains(val)
new.balance()