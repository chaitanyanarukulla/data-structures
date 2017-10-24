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
    def __init__(self, *args):
        if not args:
            self.head = None
            self.size = 0
            print('size')
        else:
            self.head = None
            self.size = 0
            for arg in args:
                new_node = Node(arg)
                new_node.set_next(self.head)
                self.head = new_node
                self.size += 1
                print('another size')


    def push(self, val):
        new_node = Node(val)
        new_node.set_next(self.head)
        self.head = new_node
        self.size += 1


    def pop(self):
        current = self.head
        self.head = current.get_next()
        self.size -= 1
        return current


    def size(self):
        print(self.size)
        return self.size


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
                    self.size -= 1
                else:
                    prev.set_next(current.get_next())
                    self.size -= 1
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


    def __str__(self):
        self.display()


    def __len__(self):
        self.size()