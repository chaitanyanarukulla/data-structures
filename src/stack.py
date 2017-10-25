"""."""
from linked_list import LinkedList

class Stack(object):
    def __init__ (self, iterable=()):
        self.func = LinkedList(iterable=())
        self.head = self.func.head
        self.length = self.func._size


    def push(self, val):
        return self.func.push(val)


    def pop(self):
        return self.func.pop()


    def __len__(self):
        return self.func._size
s