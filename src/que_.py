"""Create queue class composed from instance of Dll()."""
from doubly_linked_list import Dll


class Queue(object):
    """Simple class from Dll() instance."""

    def __init__(self):
        """Initiate an empty stack."""
        self.func = Dll()

    def enqueue(self, val):
        """Push an item into stack."""
        return self.func.push(val)

    def dequeue(self):
        """Remove first item pushed into stack."""
        try:
            return self.func.shift().data
        except IndexError:
            raise IndexError('There are no nodes to dequeue.')

    def peek(self):
        """Return the value of the next node to be removed."""
        try:
            return self.func.tail.data
        except AttributeError:
            return None

    def size(self):
        """Return the size."""
        return self.func._size

    def __len__(self):
        """Print length of stack."""
        return self.func._size
