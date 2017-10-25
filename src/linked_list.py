"""DATA Structure for linked list"""

class Node(object):
    """This create a class of Node"""
    def __init__(self, data = None, next = None):
    """This function creates instance of class Node"""
        self.data = data
        self.next = next


    def get_data(self):
    """This function  sets  self  to data"""
        return self.data


    def get_next(self):
    """This function  return next of data"""
        return self.next


    def set_next(self, new_next):
     """This function  sets data to next data"""
        self.next = new_next


class LinkedList(object):
    """This create a class of LinkedList"""
    def __init__(self, iterable=()):
    """This function creates instance of LinkedList"""
        self.head = None
        self._size = 0
        if isinstance(iterable, (tuple, list)):
            for item in iterable:
                self.push(item)
        elif isinstance(iterable, (str, int)):
            self.push(iterable)
        else:
            self.head = Node()


    def push(self, val):
        """This function creates new node and makes it a head"""
        new_node = Node(val)
        new_node.set_next(self.head)
        self.head = new_node
        self._size += 1


    def pop(self):
    """This function delets the first node and mkes next node a head"""
        if self.head is None:
            raise IndexError('This is an empty list. No values to pop.')
        current = self.head
        self.head = current.get_next()
        self._size -= 1
        return current


    def size(self):
    """This function returns the length"""
        print(self._size)
        return self._size


    def search(self, val):
    """This function searchs the val"""
        current = self.head
        while current:
            if current.get_data() == val:
                print('current')
                return current
            else:
                current = current.get_next()
        return None


    def remove_node(self, data):
    """This function serches the value and removes a node of that value and links the between nodes"""
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
    """This function displays the data in str of tuples"""
        print_list = '('
        current = self.head
        while current:
            if current.get_next():
                print_list = print_list + str(current.data) + ', '
            else:
                print_list = print_list + str(current.data) + ')'
            current = current.get_next()
        print(print_list)
        return print_list


    def __str__(self):
    """This function returns the displays of data in str of tuples"""
        return str(self.display())


    def __len__(self):
        return self._size