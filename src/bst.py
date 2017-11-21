"""Binary Search Tree."""


class Node(object):
    """Node object for bst."""
    def __init__(self, data, lc=None, rc=None)
        self.data = data
        self.left = lc
        self.right = rc


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
            current = self.root.left
            while current != None:
                if val == current:
                    raise ValueError('This node already exists.')
                if val < current:
                    current = current.left
                if val > current:
                    current = current.right
            if val < current:
                current.left = Node(val)
                self._size += 1
            if val > current:
                current.right = Node(val)
                self._size += 1
        if val > self.root:
            current = self.root.right
            while current != None:
                if val == current:
                    raise ValueError('This node already exists.')
                if val < current:
                    current = current.left
                if val > current:
                    current = current.right
            if val < current:
                current.left = Node(val)
                self._size += 1
            if val > current:
                current.right = Node(val)
                self._size += 1

    def search(self, val):
        """Search bst for val and return node of this val, else none."""
        if val == self.root:
            return self.root
        if val < self.root:
            current = self.root.left
            while current != None:
                if val == current:
                    return current
                if val < current:
                    current = current.left
                if val > current:
                    current = current.right
        if val > self.root:
            current = self.root.right
            while current != None:
                if val == current:
                    return current
                if val < current:
                    current = current.left
                if val > current:
                    current = current.right
        else:
            return None

    def size(self):
        """Returns size of bst."""
        return self._size

    def depth(self, root=self.root):
        """Returns total number of levels in bst."""
        if root is None:
            return 0
        if not root.left and not root.right:
            return 1
        elif root.left and not root.right:
            return depth(root.left) + 1
        elif root.right and not root.left:
            return depth(root.right) + 1
        else:
            return max(depth(root.left), depth(root.right)) + 1

    def contains(self, val):
        """Search for val in tree and return boolean."""
        return self.search(val)

    def balance(self):
        """Returns integer indicating balance of tree."""
        if self.root is None:
            return 'There are no nodes in this tree.'
        return depth(self.root.right) - depth(self.root.left) 




