# Data-Structures

[![Build Status](https://travis-ci.org/markreynoso/data-structures.svg?branch=bst_traversals)](https://travis-ci.org/markreynoso/data-structures)

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

### Binaary Heap (min-heap) Class Usage

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

### Graph Class (weighted) Usage

```
To create an instance of a Graph() class contained in package, from python:

new = Graph() *you may not call Graph() with any parameters.*

Graph() contains the following methods:
* _nodes() (O1)_ - will return a list of all nodes in the graph.
* _edges() (On2)_ - will return a dictionary of edges in graph with weights.
*_add_node(val) (01)_ - adds a new node to the graph.
*_add_edge(val1, val2, weight) (0n)_ - add a new edge to nodes in the graph.
* _del_node(val) (On2)_ - delete node from graph.
* _del_edge(val1, val2) (On)_ - delete edge between two nodes.
* _has_node(val) (O1)_ - returns true if node exists and false if not.
* _neighbors(val) (On2)_ - return a list of nodes with edges to input node.
* _adjacent(val1, val2) (On)_ - return true if edge exists between two inputs,
 otherwise false.
* _depth_first_traversal(start_val) (Ologn)_ - will return full visited path of traversal completed.
* _breadth_first_traversal(start_val)(Ologn)_ - will return full visited path of traversal completed.

To access any contained methods:
new.nodes()
new.edges()
new.add_node(val)
new.add_edge(val1, val2, weight)
new.del_node(val)
new.del_edge(val1, val2)
new.has_node(val)
new.neighbors(val)
new.adjacent(val1, val2)
new.depth_first_traversal(start_val)
new.breadth_first_traversal(start_val)

```

### Shortest Distance Problem

```
The problem of the traveling salesperson finding the shortest distance between points can be solved in a variety of ways. We have used Dijkstra's Algorith as our first method to a solution. 

_Dijkstra's Algorithm_ (On) - finds the shortest path exploring all edges of a graph from it's starting point. By comparing the distance or weight of the edges from the start to each child as it traverses the graph it is able to calculate the shortest route by saving the parent path which will have the lowest cost from start to finish.

To use this function:
dijkstra(graph, start, end)

```

### Self-Balancing Binary Search Tree

```
Tree will maintain a balance of no more that 1 or -1 and will automatically rebalance on any insert or delete into the tree using the methods described below. 

To create an instance if the binary search tree, Bst(), from python:

new = Bst() *you may not call Bst() no parameters or with an iterable item containing unique integers.*

Bst() contains the following methods:
* _insert(val) (Olog(n))_ - will insert the value ‘val’ in the appropriate position in the tree.
* _search(val) (0log(n))_ - will find a given value in the tree, if not in tree will return none.
* _size() (O(1))_ - will return the size of the tree.
* _depth(root) (0(n))_ - returns the depth of the tree.
* _contains(val) (Olog(n))_ - will return true or false if value is in tree.
*_ balance() (0(n))_ - returns the depth of the left minus the right side of the tree as an integer.
* _in_order() (O(n))_ - returns a generator the entire tree in order of lowest to highest value.
* _pre_order() (0(n)(log(n)))_ - returns a generator of parent followed by children from left side to right side.
* _post_order() (O(n)log(n)))_ - returns a generator of children followed by parent from left side to right side.
*_ breadth_first() (0(n))_ - returns generator of tree ordered from root one level at a time.
*_ delete(val) (0log(n))_ - delete a node with given val.

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
new.delete(val)
```

### Hash Table

```
Using a naive hash and slightly more complex hash with Horner's Rule, HashTable() will store based on the supplied key, which must be a string. By default, HashTable() uses the naive hash method, but can be changed on initialization. 

To create an instance if the hash table, HashTable(), from python:

new = HashTable() *you may initiate the table with any size, must be integer, as the first arguement in the function. You may also pass in an alternative hashing method. A naive hash will be used my defaul, but you may also choose `horner_hash` as the second arguement on initialization, or any hashing function you choose to import. For example: HashTable(100000, horner_hash).*

HashTable() contains the following methods:
* _set(key, val) (O(n))_ - sets a value at a given key (must me string) in the table, if key already has value it will be set to new value.
* _get(key) (0(n))_ - retrieve the value of the item with the given key.
* _ _hash(key) (O(n))_ - hashes key and returns an integer between 0 and the size of the table.

To access any contained methods:
new.set(key, val)
new.get(key)
```

### Trie

```
In order to efficiently store words, Trie() will provide a class by which nodes are only inserted if unshared by anthor word. All words share previous characters when possible. 

To create an instance if the trie, Trie(), from python:

new = Trie() *you may not initiate the trie with any values.*

Trie() contains the following methods:
* _insert(string) (O log(n))_ - inserts a new node for every letter in string (input must be word) if not able to share with another word.
* _contains(string) (0 log(n))_ - returns True if word is in trie and False if not.
* _size() (O(1))_ - retruns the number of words in the trie.
* _remove(string) (O log(n))_ - removes word from trie and raises error if word not in trie.

To access any contained methods:
new.insert(string)
new.contains(string)
new.size()
new.remove(string)
```

### Bubble Sort

```
Bubble sort takes in a list of numbers and uses a bubble sort method to return a sorted list. 

To use bubble_sort, from bubble_sort import bubble_sort.
Pass in a list of numbers bubble_sort(list).

* _bubble_sort(list) (O(n^2))_

```