"""Create a Stack class composed from instance of LinkedList()."""
from linked_list import LinkedList


class Stack(object):
    """Simple class from LinkdedList() instance."""

    def __init__(self, iterable=()):
        """Initiate an empty stack."""
        self.func = LinkedList(iterable)

    def push(self, val):
        """Push an item or iterable into stack."""
        return self.func.push(val)

    def pop(self):
        """Remove last item pushed into stack."""
        try:
            return self.func.pop().data
        except IndexError:
            raise IndexError('There are no nodes to pop.')

    def __len__(self):
        """Print length of stack."""
        return self.func._size
