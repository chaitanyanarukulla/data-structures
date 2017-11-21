"""Binary Search Tree."""


class Node(object):
    """Node object for bst."""
    def __init__(self, data, lc=None, rc=None)
        self.data = data
        self.left_child = lc
        self.right_child = rc


class BST(object):
    """Binary Search Tree class."""

    def __init__(self, iterable=None):
        """Initiate a new instance of bst."""
        self._tree = {}
        self.root = None
        self._size = 0
        if isinstance(iterable, (list, tuple)):
            for item in iterable:
                self.insert(item)

    def insert(self, val):
        """Insert a value into bst."""
        if self.root = None:
            self.root = Node(val)
            self._size += 1
        if val == self.root:
            raise ValueError('This node already exists.')
        if val < self.root:
            current = self.root.left_child
            while current != None:
                if val == current:
                    raise ValueError('This node already exists.')
                if val < current:
                    current = current.left_child
                if val > current:
                    current = current.right_child
            if val < current:
                current.left_child = Node(val)
                self._size += 1
            if val > current:
                current.right_child = Node(val)
                self._size += 1
        if val > self.root:
            current = self.root.right_child
            while current != None:
                if val == current:
                    raise ValueError('This node already exists.')
                if val < current:
                    current = current.left_child
                if val > current:
                    current = current.right_child
            if val < current:
                current.left_child = Node(val)
                self._size += 1
            if val > current:
                current.right_child = Node(val)
                self._size += 1

    def search(self, val):
        """Search bst for val and return node of this val, else none."""
        if val == self.root:
            return self.root
        if val < self.root:
            current = self.root.left_child
            while current != None:
                if val == current:
                    return current
                if val < current:
                    current = current.left_child
                if val > current:
                    current = current.right_child
        if val > self.root:
            current = self.root.right_child
            while current != None:
                if val == current:
                    return current
                if val < current:
                    current = current.left_child
                if val > current:
                    current = current.right_child
        else:
            return None

    def size(self):
        """Returns size of bst."""
        return self._size

    def depth(self):
        """Returns total number of levels in bst."""
        right = 0
        left = 0
        depth = 0
        current = self.root
        while current != None:
            if current.left_child:
                current = current.left_child
                left += 1
                