"""Binary Search Tree."""


class Node(object):
    """Node object for Binary search tree."""

    def __init__(self, data):
        """Initialize a new node."""
        self.data = data
        self.left = None
        self.right = None


class Bst(object):
    """Binary Search Tree class."""

    def __init__(self, iterable=None):
        """Initiate a new instance of binary search tree."""
        self.root = None
        self._size = 0
        if isinstance(iterable, (list, tuple)):
            for item in iterable:
                self.insert(item)

    def insert(self, val):
        """Insert a value into binary search tree."""
        if not isinstance(val, (int, float)):
            raise ValueError('Enter numbers only')
        if self.root is None:
            self.root = Node(val)
            self._size += 1
            return
        elif val == self.root.data:
            raise ValueError('This node already exists.')
        current = self.root
        while current:
            if val == current.data:
                    raise ValueError('This node already exists.')
            elif val < current.data:
                if current.left:
                    current = current.left
                else:
                    current.left = Node(val)
                    self._size += 1
                    break
            elif val > current.data:
                if current.right:
                    current = current.right
                else:
                    current.right = Node(val)
                    self._size += 1
                    break

    def search(self, val):
        """Search bst for val and return node of this val, else none."""
        if self.root is None or not isinstance(val, (int, float)):
            return
        current = self.root
        while current:
            if val == current.data:
                return current
            elif val < current.data:
                current = current.left
            elif val > current.data:
                current = current.right

    def contains(self, val):
        """Search for val in tree and return boolean."""
        if self.search(val) is not None:
            return True
        else:
            return False

    def size(self):
        """Return size of bst."""
        return self._size

    def depth(self, root):
        """Return total number of levels in bst."""
        if root is None:
            return 0
        if not root.left and not root.right:
            return 0
        elif root.left and not root.right:
            return self.depth(root.left) + 1
        elif root.right and not root.left:
            return self.depth(root.right) + 1
        else:
            return max(self.depth(root.left), self.depth(root.right)) + 1

    def balance(self):
        """Return integer indicating balance of tree."""
        if self.root is None:
            return 'There are no nodes in this tree.'
        elif not self.root.left and not self.root.right:
            return 0
        elif self.root.left and not self.root.right:
            return self.depth(self.root.left)
        elif self.root.right and not self.root.left:
            return self.depth(self.root.right)
        else:
            return self.depth(self.root.right) - self.depth(self.root.left)

    def breadth_first(self):
        """Return generator of breadth first search."""
        if self.root is None:
            raise ValueError('There are no nodes in this tree.')
        breadth_first_search = [self.root]
        while breadth_first_search:
            current = breadth_first_search.pop(0)
            if current.left:
                breadth_first_search.append(current.left)
            if current.right:
                breadth_first_search.append(current.right)
            yield current.data

    def in_order(self):
        """Return generator of in order search."""
        if self.root is None:
            raise ValueError('There are no nodes in this tree.')
        current = self.root
        in_order_search = []
        while current or in_order_search:
            if current:
                in_order_search.append(current)
                current = current.left
            else:
                current = in_order_search.pop()
                yield current.data
                current = current.right

    def pre_order(self):
        """Return generator of pre order search."""
        if self.root is None:
            raise ValueError('There are no nodes in this tree.')
        current = self.root
        in_order_search = []
        while current or in_order_search:
            if current:
                yield current.data
                if current.right:
                    in_order_search.append(current.right)
                current = current.left
            else:
                current = in_order_search.pop()

    def post_order(self):
        """Return generator of post order wearch."""
        if self.root is None:
            raise ValueError('There are no nodes in this tree.')
        current = self.root
        child = None
        in_order_search = []
        while current or in_order_search:
            if current:
                in_order_search.append(current)
                current = current.left
            else:
                if in_order_search[-1].right and in_order_search[-1].right is not child:
                    current = in_order_search[-1].right
                else:
                    child = in_order_search.pop()
                    yield child.data

    def delete(self, val):
        """Delete."""
        node, parent = self.root, None

        while node is not None and val != node.data:
            parent = node
            if val > node.data:
                node = node.right
            else:
                node = node.left

        if node is None:
            return None
        # declare replacement
        replacement = None
        # if node has two children
        if node.left is not None and node.right is not None:
            replacement = self._remove_successor(node)
            replacement.left = node.left
            replacement.right = node.right
        # if node has one or no child
        elif node.left is None:
            replacement = node.right
        else:
            replacement = node.left

        # replace node
        if node == self.root:
            self.root = replacement
        elif parent.left == node:
            parent.left = replacement
        else:
            parent.right = replacement

        return node

    def _remove_successor(self, val):
        """If val has child."""
        succ, parent = val.right, val
        while succ.left is not None:
            parent = succ
            succ = succ.left
        if succ == parent.right:
            parent.right = succ.right
        else:
            parent.left = succ.right

        return succ


if __name__ == '__main__':  # pragma: no cover
    import timeit

    insert_time_ub = Bst()
    num = (x for x in range(1000))
    insert_unbalanced = timeit.timeit(
        'insert_time_ub.insert(next(num))',
        setup='from __main__ import insert_time_ub, num',
        number=1000)

    search_time_ub = Bst()
    for i in range(100):
        search_time_ub.insert(i)
    search_unbalanced = timeit.timeit(
        'search_time_ub.search(99)',
        setup='from __main__ import search_time_ub',
        number=1000)

    search_unbalanced_head = timeit.timeit(
        'search_time_ub.search(0)',
        setup='from __main__ import search_time_ub',
        number=1000)

    insert_time_b = Bst()

    def insert_time(val):
        """."""
        if (500 + val) % 2 == 0:
            insert_time_b.insert(500 + val)
        else:
            insert_time_b.insert(500 - val)

    num_b = (x for x in range(1000))
    insert_balanced = timeit.timeit(
        'insert_time(next(num_b))',
        setup='from __main__ import insert_time, num_b',
        number=1000)

    search_time_b = Bst()
    for i in range(1000):
        if (500 + i) % 2 == 0:
            search_time_b.insert(500 + i)
        else:
            search_time_b.insert(500 - i)

    search_balanced_leaf = timeit.timeit(
        'search_time_b.search(999)',
        setup='from __main__ import search_time_b',
        number=1000)

    search_balanced_head = timeit.timeit(
        'search_time_b.search(500)',
        setup='from __main__ import search_time_b',
        number=1000)

    print('The following time relates to worst case insert.')
    print('Insert unbalanced: {}'.format(insert_unbalanced))
    print('Insert balanced: {}'.format(insert_balanced))
    print('\nThe following time relates to worst case search.')
    print('Search unbalanced leaf: {}'.format(search_unbalanced))
    print('Search balanced leaf: {}'.format(search_balanced_leaf))
    print('\nThe following time relates to best base search.')
    print('Search unbalanced head: {}'.format(search_unbalanced_head))
    print('Search balanced head: {}'.format(search_balanced_head))
