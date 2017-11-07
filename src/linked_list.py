"""DATA Structure for linked list."""


class Node(object):
    """Create a class of Node."""

    def __init__(self, data=None, next=None):
        """Create instance of class Node."""
        self.data = data
        self.next = next

    def get_data(self):
        """Set self to data."""
        return self.data

    def get_next(self):
        """Return next of data."""
        return self.next

    def set_next(self, new_next):
        """Set data to next data."""
        self.next = new_next


class LinkedList(object):
    """Create a class of LinkedList."""

    def __init__(self, iterable=None):
        """Create instance of LinkedList."""
        self.head = None
        self._size = 0
        if isinstance(iterable, (tuple, list)):
            for item in iterable:
                self.push(item)
        elif isinstance(iterable, (str, int)):
            self.push(iterable)

    def push(self, val):
        """Create new node and makes it a head."""
        new_node = Node(val)
        new_node.set_next(self.head)
        self.head = new_node
        self._size += 1

    def pop(self):
        """Delete the first node and make next node a head."""
        if self.head is None:
            raise IndexError('This is an empty list. No values to pop.')
        current = self.head
        self.head = current.get_next()
        self._size -= 1
        return current.data

    def size(self):
        """Return the length."""
        return self._size

    def search(self, val):
        """Search the list."""
        current = self.head
        while current:
            if current.get_data() == val:
                return current
            else:
                current = current.get_next()
        return None

    def remove(self, node):
        """Search and removes node of that value, then links adjecent nodes."""
        current = self.head
        prev = None
        while current:
            if current == node:
                if current == self.head:
                    self.head = current.get_next()
                    self._size -= 1
                else:
                    prev.set_next(current.get_next())
                    self._size -= 1
                return current
            prev = current
            current = current.get_next()
        else:
            raise ValueError('Your node does not exist in this linked list.')

    def display(self):
        """Display the data in str looking tuple."""
        if self._size > 0:
            print_list = '('
            current = self.head
            while current:
                if current.get_next():
                    print_list = print_list + str(current.data) + ', '
                else:
                    print_list = print_list + str(current.data) + ')'
                current = current.get_next()
            return print_list
        else:
            return '()'

    def __str__(self):
        """Display of data in str looking tuple."""
        return str(self.display())

    def __len__(self):
        """Display size of list."""
        return self._size
