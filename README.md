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
* _push(val)_ - will insert the value ‘val’ at the head of the list
* _pop()_ - will pop the first value off the head of the list and return it. Raises an exception with an appropriate message if there are no values to return.
* _size()_ - will return the length of the list.
* _search(val)_ - will return the node containing ‘val’ in the list, if present, else None.
* _remove(node)_ - will remove the given node from the list, wherever it might be (node must be an item in the list). If the node is not in the list, it will raise an exception with an appropriate message.
* _display()_ - will return a unicode string representing the list as if it were a Python tuple literal: “(12, ‘sam’, 37, ‘tango’)”

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

```
