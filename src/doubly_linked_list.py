"""Create a new instance of a doubly linked list."""


class Node(object):
    """Create new instance of Node class."""

    def __init__(self, data=None, prve=None, next=None, tail=None):
        """Initiate new Node with no defined values."""
        self.data = data
        self.next = next
        self.prve = prve

    def get_prve(self):
        """Get previous node."""
        return self.prve

    def get_data(self):
        """Get data of current node."""
        return self.data

    def get_next(self):
        """Get next node."""
        return self.next

    def set_next(self, new_next):
        """Set next node."""
        self.next = new_next

    def set_prve(self, new_prve):
        """Set previous node."""
        self.prve = new_prve


class Dll(object):
    """Create instance of doubly linked link class."""

    def __init__(self):
        """Initialize doubly linked list with no default values."""
        self.head = None
        self.tail = None
        self._size = 0

    def push(self, val):
        """Push value to top of list."""
        new_node = Node(val)
        if self._size < 1:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next(self.head)
            self.head.set_prve(new_node)
            self.head = new_node
        self._size += 1

    def append(self, val):
        """Append value to tail of list."""
        new_node = Node(val)
        if self._size < 1:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_prve(self.tail)
            self.tail.set_next(new_node)
            self.tail = new_node
        self._size += 1

    def pop(self):
        """Remove current head of list."""
        current = self.head
        if self.head is None:
            raise IndexError('This is an empty list. No values to pop.')
        elif self._size == 1:
            self.tail = None
            self.head = None
            self._size -= 1
        elif self._size > 1:
            self.head = current.get_next()
            self.head.set_prve(None)
            self._size -= 1
        return current.data

    def shift(self):
        """Remove current tail of list."""
        current = self.tail
        if self.tail is None:
            raise IndexError('This is an empty list. No values to shift.')
        elif self._size == 1:
            self.tail = None
            self.head = None
            self._size -= 1
        elif self._size > 1:
            self.tail = current.get_prve()
            self.tail.set_next(None)
            self._size -= 1
        return current.data

    def remove(self, val):
        """Remove inputted value."""
        current = self.head
        while current:
            if current.get_data() == val:
                if current == self.head:
                    self.pop()
                    return None
                if current == self.tail:
                    self.shift()
                    return None
                else:
                    npn = current.get_prve()
                    nnn = current.get_next()
                    npn.set_next(nnn)
                    nnn.set_prve(npn)
                    self._size -= 1
                    return None
            current = current.get_next()
        else:
            raise ValueError('Your node does not exist in this linked list.')

    def __len__(self):
        """Display size of list."""
        return self._size
