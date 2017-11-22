"""Binary Search Tree."""


class Node(object):
    """Node object for bst."""

    def __init__(self, data, lc=None, rc=None):
        """Initialize a new node."""
        self.data = data
        self.left = lc
        self.right = rc


class Bst(object):
    """Binary Search Tree class."""

    def __init__(self, iterable=None):
        """Initiate a new instance of bst."""
        self.root = None
        self._size = 0
        if isinstance(iterable, (list, tuple)):
            for item in iterable:
                self.insert(item)

    def insert(self, val):
        """Insert a value into bst."""
        if not isinstance(val, (int, float)):
            raise ValueError('Sorry, I only take numbers right now.')
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

    def contains(self, val):
        """Search for val in tree and return boolean."""
        if self.search(val) is not None:
            return True
        else:
            return False

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


if __name__ == '__main__':  # pragma: no cover
    import timeit

    insert_time_ub = Bst()
    num = (x for x in range(1000))
    a = timeit.timeit('insert_time_ub.insert(next(num))',
                      setup='from __main__ import insert_time_ub, num',
                      number=1000)
    search_time_ub = Bst()
    for i in range(100):
        search_time_ub.insert(i)
    b = timeit.timeit('search_time_ub.search(99)',
                      setup='from __main__ import search_time_ub',
                      number=1000)
    c = timeit.timeit('search_time_ub.search(0)',
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
    d = timeit.timeit('insert_time(next(num_b))',
                      setup='from __main__ import insert_time, num_b',
                      number=1000)

    search_time_b = Bst()
    for i in range(1000):
        if (500 + i) % 2 == 0:
            search_time_b.insert(500 + i)
        else:
            search_time_b.insert(500 - i)
    e = timeit.timeit('search_time_b.search(999)',
                      setup='from __main__ import search_time_b',
                      number=1000)
    f = timeit.timeit('search_time_b.search(500)',
                      setup='from __main__ import search_time_b',
                      number=1000)

    print('The following time relates to worst case insert.')
    print('Insert unbalanced: {}'.format(a))
    print('Insert balanced: {}'.format(d))
    print('\nThe following time relates to worst case search.')
    print('Search unbalanced leaf: {}'.format(b))
    print('Search balanced leaf: {}'.format(e))
    print('\nThe following time relates to best base search.')
    print('Search unbalanced head: {}'.format(c))
    print('Search balanced head: {}'.format(f))
