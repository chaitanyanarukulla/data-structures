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
        if not isinstance(val, int):
            raise ValueError('Sorry, I only take numbers right now.')
        if self.root is None:
            self.root = Node(val)
            self._size += 1
        elif val == self.root.data:
            raise ValueError('This node already exists.')
        elif val < self.root.data:
            if self.root.left:
                current = self.root.left
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
            else:
                if val < self.root.data:
                    self.root.left = Node(val)
                    self._size += 1
                if val > self.root.data:
                    self.root.right = Node(val)
                    self._size += 1
        elif val > self.root.data:
            if self.root.right:
                current = self.root.right
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
            else:
                if val < self.root.data:
                    self.root.left = Node(val)
                    self._size += 1
                if val > self.root.data:
                    self.root.right = Node(val)
                    self._size += 1

    def search(self, val):
        """Search bst for val and return node of this val, else none."""
        if self.root is None or not isinstance(val, int):
            return None
        if val == self.root.data:
            return self.root
        if val < self.root.data:
            if self.root.left:
                current = self.root.left
                while current:
                    if val == current.data:
                        return current
                    elif val < current.data:
                        try:
                            current = current.left
                        except AttributeError:
                            break
                    elif val > current.data:
                        try:
                            current = current.right
                        except AttributeError:
                            break
        if val > self.root.data:
            if self.root.right:
                current = self.root.right
                while current:
                    if val == current.data:
                        return current
                    elif val < current.data:
                        try:
                            current = current.left
                        except AttributeError:
                            break
                    elif val > current.data:
                        try:
                            current = current.right
                        except AttributeError:
                            break
        else:
            return None

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
