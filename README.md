
# data-structures
### Insert Sort

```
Insert sort takes in a list of numbers and uses an insert sort method to return a sorted list. 

To use insert_sort, from insert_sort import insert_sort.
Pass in a list of numbers insert_sort(list).

* _bubble_sort(list) (O(n^2))_

```

# Data-Structures

Where a variety of data-structures found in python are being explored, such as:
* A simple class LinkedList for building linked lists as well as a subclass Stack to implement a stack.

## Authors

ChaiChaitanya Narukulla and Mark Reynoso created this code base as a project for Python 401 at Code Fellows Seattle. 

### Requirements for testing and development

In order to create a development and testing environment, you will need the following:

```
python2, python3, ipython, pytest, pytest-watch, pytest-cov, tox
```

```
To install environment:

pip install -e .[testing][development]
```

### Usage

```
To create an object instance of a class contained in package, from python:

new = LinkedList() *you may choose and optional parameter of a single value or an iterable of one of the following: a tuple, a list, or a string.*

LinkedList() contains the following methods:
* _push(val) (O1)_ - will insert the value ‘val’ at the head of the list
* _pop() (O1)_ - will pop the first value off the head of the list and return it. Raises an exception with an appropriate message if there are no values to return.
* _size() (01)_ - will return the length of the list.
* _search(val) (On)_ - will return the node containing ‘val’ in the list, if present, else None.
* _remove(node) (On)_ - will remove the given node from the list, wherever it might be (node must be an item in the list). If the node is not in the list, it will raise an exception with an appropriate message.
* _display() (O1)_ - will return a unicode string representing the list as if it were a Python tuple literal: “(12, ‘sam’, 37, ‘tango’)”

To access any contained methods:
new.push(val)
new.pop()
new.size()
new.search(val)
new.remove(node)
new.display()

Additionally, LinkedList will interact with these built-in Python functions:

* _len(new)_ - returns the size of the list.
* _print(new)_ - returns what the display() method returns.


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

