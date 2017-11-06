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

### Linkded List Class Usage

```
To create an instance of a the LinkedList() class contained in package, from python:

new = LinkedList() *you may choose and optional parameter of a single value or an iterable of one of the following: a tuple, a list, or a string.*

LinkedList() contains the following methods:
* _push(val) (O1)_ - will insert the value ‘val’ at the head of the list.
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

Additionally, LinkedList() will interact with these built-in Python functions:

* _len(new)_ - returns the size of the list.
* _print(new)_ - returns what the display() method returns.

```

### Stack Class Usage

```
To create an instance of a Stack() class contained in package, from python:

new = Stack() *you may choose and optional parameter of a single value or an iterable of one of the following: a tuple, a list, or a string.*

Stack() contains the following methods:
* _push(val) (O1)_ - will insert the value ‘val’ at the head of the stack.
* _pop() (O1)_ - will pop the first value off the head of the stack and return it. Raises an exception with an appropriate message if there are no values to return.

To access any contained methods:
new.push(val)
new.pop()

Additionally, Stack() will interact with these built-in Python functions:

* _len(new)_ - returns the size of the list.

```

### Doubly Linked List Class Usage

```
To create an instance of a Dll() class contained in package, from python:

new = Dll() *you may not call Dll() with any parameters.*

Dll() contains the following methods:
* _push(val) (O1)_ - will insert the value ‘val’ at the head of the list.
* _append(val) (O1)_ - will insert the value ‘val’ at the tail of the list.
* _pop() (O1)_ - will pop the first value off the head of the stack and return it. Raises an exception with an appropriate message if there are no values to return.
* _shift() (O1)_ - will remove the last value off the tail of the list and return it. Raises an exception with an appropriate message if there are no values to return.
* _remove(node) (On)_ - will remove the given node from the list, wherever it might be (node must be an item in the list). If the node is not in the list, it will raise an exception with an appropriate message.

To access any contained methods:
new.push(val)
new.append(val)
new.pop()
new.shift()
new.remove()

Additionally, Dll() will interact with these built-in Python functions:

* _len(new)_ - returns the size of the list.

```

### Queue Class Usage

```
To create an instance of a Queue() class contained in package, from python:

new = Queue() *you may not call Queue() with any parameters.*

Queue() contains the following methods:
* _enqueue(val) (O1)_ - will insert the value ‘val’ at the end of the queue.
* _dequeue() (O1)_ - will remove the last value off the front of the queue and return it. Raises an exception with an appropriate message if there are no values to return.
* _peek() (O1)_ - shows the value of the node at the end of the queue.
* _size() (O1)_ - displays the number of node in the queue.

To access any contained methods:
new.enqueue(val)
new.dequeue()
new.peek()
new.size()

Additionally, Queue will interact with these built-in Python functions:

* _len(new)_ - returns the size of the list.

```

### Deque Class Usage

```
To create an instance of a Deque() class contained in package, from python:

new = Deque() *you may not call Deque() with any parameters.*

Deque() contains the following methods:
* _append(val) (O1)_ - will insert the value ‘val’ at the end of the deque.
* _appendleft() (O1)_ - will insert a value to the front of the deque.
*_pop() (01)_ - removes the first val from the end of the deque.
*_popleft() (01)_ - removes the first val from the front of the deque.
* _peek() (O1)_ - shows the value of the item at the end of the deque.
* _peekleft() (O1)_ - shows the value of the item at the font of the deque.
* _size() (O1)_ - displays the number items in the deque.

To access any contained methods:
new.append(val)
new.appendleft(val)
new.pop()
new.popleft()
new.peek()
new.peekleft()
new.size()

```

### Binaary Heap (Binheap) Class Usage

```
To create an instance of a Binheap() class contained in package, from python:

new = Binheap() *you may call Binheap() with any uniqe number or iterable of unique numbers.*

Binheap() contains the following methods:
* _push(val) (Olog(n))_ - will insert the value ‘val’ at the end of the heap.
*_pop() (0log(n))_ - removes the first val from the end of the heap.

To access any contained methods:
new.push(val)
new.pop()

```

### Priorityq (Priorityq) Class Usage

```
To create an instance of a Priorityq() class contained in package, from python:

new = Priorityq() *you may call Priorityq() with any uniqe number or iterable of unique numbers.*

Priorityq() contains the following methods:
*_insert(val,priority) (O1)_ - will insert the value ‘val’ at the end of the heap.
*_pop() (01)_ - removes the higest priority and returns the higest priority.
*_peek() (01)_ - returns the higest priority.

To access any contained methods:
new.insert(val)
new.pop()
new.peek()

```

### Graph Class Usage

```
To create an instance of a Graph() class contained in package, from python:

new = Graph() *you may not call Graph() with any parameters.*

Graph() contains the following methods:
* _nodes() (O1)_ - will return a list of all nodes in the graph.
* _edges() (On2)_ - will return a list of edges in graph.
*_add_node(val) (01)_ - adds a new node to the graph.
*_add_edge(val1, val2) (0n)_ - add a new edge to nodes in the graph.
* _del_node(val) (On2)_ - delete node from graph.
* _del_edge(val1, val2) (On)_ - delete edge between two nodes.
* _has_node(val) (O1)_ - returns true if node exists and false if not.
* _neighbors(val) (On2)_ - return a list of nodes with edges to input node.
* _adjacent(val1, val2) (On)_ - return true if edge exists between two inputs, otherwise false.

To access any contained methods:
new.nodes()
new.edges()
new.add_node(val)
new.add_edge(val1, val2)
new.del_node(val)
new.del_edge(val1, val2)
new.has_node(val)
new.neighbors(val)
new.adjacent(val1, val2)

```