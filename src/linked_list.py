"""DATA"""

class Node(object):
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next_node = next_node


    def get_data(self):
        return self.data


    def get_next(self):
        return self.next


    def set_next(self, new_next):
        self.next = new_next


class LinkedList(object):
    def __init__(self, head = None)
        self.head = head

    def push(val):
        new_node = Node(val)
        new_node.set_next(self.head)
        self.head = new_node


    def pop():
        current = self.head
        self.head = current.get_next()
        return current


