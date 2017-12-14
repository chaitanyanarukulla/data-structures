"""Binary heap class."""


class Binheap(object):
    """Iniitialize the class node."""

    def __init__(self, iterable=None):
        """Create a new min heap."""
        self.heaplist = []
        self._size = 0
        if isinstance(iterable, (list, tuple)):
            for item in iterable:
                self.push(item)

    def push(self, val):
        """Push a value to the end of heap and sort up."""
        if type(val) == int or type(val) == float:
            self.heaplist.append(val)
            self._size += 1
            sort_up = True
            idx = self._size - 1
            while sort_up:
                if idx > 0:
                    if idx % 2 == 0:
                        parent = (idx - 2) // 2
                    else:
                        parent = (idx - 1) // 2
                    if val < self.heaplist[parent]:
                        self.heaplist[idx] = self.heaplist[parent]
                        self.heaplist[parent] = val
                        idx = parent
                    else:
                        sort_up = False
                else:
                    sort_up = False
        else:
            raise ValueError('You must input numbers only.')

    def pop(self):
        """Remove first value in heap and sort down."""
        if self._size == 0:
            raise IndexError('There are no values to pop.')
        elif self._size == 1:
            self._size -= 1
            return self.heaplist.pop()
        elif self._size > 1:
            pop_val = self.heaplist[0]
            self.heaplist[0] = self.heaplist.pop()
            self._size -= 1
            idx = 0
            sort_down = True
            while sort_down:
                l_child = idx * 2 + 1
                r_child = idx * 2 + 2
                if r_child <= self._size - 1 and l_child <= self._size - 1:
                    if self.heaplist[l_child] > self.heaplist[r_child]:
                        if self.heaplist[r_child] < self.heaplist[idx]:
                            self.heaplist[r_child], self.heaplist[idx] =\
                                self.heaplist[idx], self.heaplist[r_child]
                            idx = r_child
                        else:
                            sort_down = False
                    else:
                        if self.heaplist[l_child] < self.heaplist[r_child]:
                            if self.heaplist[l_child] < self.heaplist[idx]:
                                self.heaplist[idx], self.heaplist[l_child] =\
                                    self.heaplist[l_child], self.heaplist[idx]
                                idx = l_child
                            else:
                                sort_down = False
                elif l_child == self._size - 1:
                    if self.heaplist[l_child] < self.heaplist[idx]:
                        self.heaplist[idx], self.heaplist[l_child] =\
                            self.heaplist[l_child], self.heaplist[idx]
                        sort_down = False
                    else:
                        sort_down = False
                else:
                    sort_down = False
            return pop_val
