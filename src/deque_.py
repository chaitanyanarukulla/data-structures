"""Create dueue class."""
from doubly_linked_list import Dll


class Deque(object):
    """Simple instance of Deque class."""

    def __init__(self):
        """Initiate an empty Deque."""
        self._container = Dll()

    def append(self, val):
        """Append adds val to the end of the Deque."""
        self._container.push(val)

    def appendleft(self, val):
        """Appendleft adds val to the front of the Deque."""
        self._container.append(val)

    def pop(self):
        """Remove first val from end of the Deque."""
        try:
            return self._container.pop()
        except IndexError:
            raise IndexError('There are no nodes to pop.')

    def popleft(self):
        """Remove first val from front of the Deque."""
        try:
            return self._container.shift()
        except IndexError:
            raise IndexError('There are no nodes to popleft.')

    def peek(self):
        """Return the value of the next node to be popped."""
        try:
            return self._container.head.data
        except AttributeError:
            return None

    def peekleft(self):
        """Return the value of the next node to be popped left."""
        try:
            return self._container.tail.data
        except AttributeError:
            return None

    def size(self):
        """Return the size."""
        return self._container._size
