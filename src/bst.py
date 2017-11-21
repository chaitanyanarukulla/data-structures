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
    bst_ub = Bst([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
    insert_time_ub = timeit.timeit(bst_ub.insert(17))
    search_time_ub = timeit.timeit(bst_ub.search(16))
    search_time_root_ub = timeit.timeit(bst_ub.search(1))
    bst_b = Bst([10, 14, 7, 12, 8, 16, 6, 11, 4, 15, 5, 18, 2, 17, 3, 19, 2])
    insert_time_b = timeit.timeit(bst_b.insert(20))
    search_time_b = timeit.timeit(bst_b.search(2))
    search_time_root_b = timeit.timeit(bst_b.search(10))
    print('The following times relate to the unbalanced binary search'
          'tree:\n[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16].')
    print('Insert 17: {}'.format(insert_time_ub))
    print('Search 16: {}'.format(search_time_ub))
    print('Search 1: {}'.format(search_time_root_ub))
    print('The following times relate to the unbalanced binary search tree'
          ':\n[10, 14, 7, 12, 8, 16, 6, 11, 4, 15, 5, 18, 2, 17, 3, 19, 2].')
    print('Insert 20: {}'.format(insert_time_b))
    print('Search 19: {}'.format(search_time_b))
    print('Search 10: {}'.format(search_time_root_b))
