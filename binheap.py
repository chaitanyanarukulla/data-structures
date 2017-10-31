"""Binary heap."""


class BinHeap(object):
    """ini the class node."""

    def __init__(self):
        """Create a new min heap."""
        self.heaplist = [0]
        self._size = 0

    def push(self, val):
        """."""
        self.heaplist.append(val)
        self._size += 1
        idx = self._size
        while idx // 2 > 0:
            if self.heaplist[idx] > self.heaplist[idx // 2]:
                temp_val = self.heaplist[idx]
                self.heaplist[idx] = self.heaplist[idx // 2]
                self.heaplist[idx // 2] = temp_val
            idx = idx // 2

    def pop(self):
        """."""
        self._size -= 1
        pop_val = self.heaplist[1]
        self.heaplist[1] = self.heaplist.pop()
        idx = 1
        while idx * 2 < self._size:
            if self.heaplist[idx * 2] > self.heaplist[idx * 2 + 1]:
                temp_val = self.heaplist[idx * 2 + 1]
                self.heaplist[idx * 2 + 1] = self.heaplist[idx]
                self.heaplist[idx] = temp_val
            idx = idx * 2
        return pop_val
