class Node(object):
    def __init__(self, data=None, prve=None, next=None, tail=None):
        self.data = data
        self.next = next
        self.prve = prve
        self.tail = tail

    def get_prve(self):
        return self.prve


    def get_data(self):
        return self.data


    def get_next(self):
        return self.next


    def set_next(self, new_next):
        self.next = new_next


    def set_prve(self, new_prve):
        self.prve = new_prve


class Dll(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0


    def push(self, val):
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
        new_node = Node(val)
        self._size += 1
        if self._size < 1:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_prve(self.tail)
            self.tail.set_next(new_node)
            self.tail = new_node


    def pop(self):
        if self.head is None:
            raise IndexError('This is an empty list. No values to pop.')
        current = self.head
        self.head = current.get_next()
        self.head.set_prve(None)
        self._size -= 1
        return current


    def shift(self):
        if self.head is None:
            raise IndexError('This is an empty list. No values to shift.')
        current = self.tail
        self.head = current.get_prve()
        self.tail.set_next(None)
        self._size -= 1
        return current


    def remove(self, val):
        current = self.head
        while current:
            if current.get_data() == val:
                if current == self.head:
                    self.pop()
                    self._size -= 1
                else:
                    npn = current.get_prve()
                    nnn = current.get_next()
                    npn.set_next(nnn)
                    nnn.set_prve(npn)
                    self._size -= 1
                return current
            current = current.get_next()
        else:
            raise ValueError('Your node does not exist in this linked list.')


















