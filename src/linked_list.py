"""DATA"""

class Node(object):
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


    def get_data(self):
        return self.data


    def get_next(self):
        return self.next


    def set_next(self, new_next):
        self.next = new_next


class LinkedList(object):
    def __init__(self, iterable=()):
        self.head = None
        self._size = 0
        if isinstance(iterable, (str, tuple, list)):
            for item in iterable:
                self.push(item)


    def push(self, val):
        new_node = Node(val)
        new_node.set_next(self.head)
        self.head = new_node
        self._size += 1


    def pop(self):
        if self.head is None:
            raise IndexError('This is an empty list. No values to pop.')
        current = self.head
        self.head = current.get_next()
        self._size -= 1
        return current


    def size(self):
        print(self._size)
        return self._size


    def search(self, val):
        current = self.head
        while current:
            if current.get_data() == val:
                print('current')
                return current
            else:
                current = current.get_next()
        return None


    def remove_node(self, data):
        current = self.head
        prev = None
        while current:
            if current.get_data() == data:
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
        print_list = []
        current = self.head
        while current:
            print_list.append(current.get_data())
            current = current.get_next()
        print(str(tuple(print_list)))
        return tuple(print_list)


    def __str__(self):
        return str(self.display())


    def __len__(self):
        return self._size