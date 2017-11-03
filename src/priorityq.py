"""Create a priority queue instance."""


class Priorityq(object):
    """Create a que with priority attributes for each value."""

    def __init__(self):
        """Initialize a priority queue instance."""
        self._que = {}
        self._highest = 0
        self._lowest = 0

    def insert(self, val, priority=0):
        """Insert a new value into the queue."""
        if priority <= self._highest:
            self._highest = priority
        if priority >= self._lowest:
            self._lowest = priority
        if priority in self._que:
            self._que[priority].append(val)
        else:
            self._que[priority] = [val]

    def pop(self):
        """Remove the highest prioty value from queue."""
        if len(self._que) == 0:
            raise IndexError('There are no value to pop.')
        else:
            self._que[self._highest].pop(0)
            if self._que[self._highest] == []:
                self._que.pop(self._highest)
                if len(self._que) == 0:
                    self._highest = 0
                    self._lowest = 0
                high = max(self._highest)
                self._highest = high
            if self._que[self._lowest] == []:
                self._que.pop(self._lowest)
                if len(self._que) == 0:
                    self._lowest = 0
                    self._lowest = 0
                high = max(self._lowest)
                self._highest = high

    def peek(self):
        """View the hightest priority item."""
        return self._que[self._highest][0]
