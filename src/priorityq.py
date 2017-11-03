"""Create a priority queue instance."""


class Priorityq(object):
    """Create a que with priority attributes for each value."""

    def __init__(self):
        """Initialize a priority queue instance."""
        self._que = {}
        self._highest = 0

    def insert(self, val, priority):
        """Insert a new value into the queue."""
        if priority:
            if priority < self._highest:
                self._highest = priority
            if self._que[priority]:
                self._que[priority].append(val)
            else:
                self._que[priority] = [val]
        else:
            lowest = 0
            for low_priority in self._que:
                if low_priority > self._highest:
                    lowest = low_priority
            self._que[lowest].append(val)

    def pop(self):
        """Remove the highest prioty value from queue."""
        return self._que[self._highest].pop(0)

    def peek(self):
        """View the hightest priority item."""
        return self._que[self._highest][0]
