"""Create a Stack class composed from instance of LinkedList()."""
from linked_list import LinkedList


class Stack(object):
    """Simple class from LinkdedList() instance."""

    def __init__ (self, iterable=()):
        self.func = LinkedList(iterable)


    def push(self, val):
        return self.func.push(val)


    def pop(self):
        return self.func.pop().data


    def __len__(self):
        return self.func._size
