"""Hash table for storing strings."""


def simple_hash(data, buckets):
    """A simple hash for strings."""
    hash_val = 0
    for letter in data:
        hash_val += ord(letter)
    return hash_val % buckets


def complex_hash(data):
    """A hash for strings."""
    pass


class HashTable(object):
    """Hash table class for hashing strings."""

    def __init__(self, size=10, hash_func=simple_hash):
        """Initialize a new hashtable."""
        self.hash_func = hash_func
        self._size = size
        self._buckets = [[] for x in range(self._size)]

    def get(self, key):
        """Return the value of the key given."""
        hash_key = self._hash(key)
        if self._buckets[hash_key] == []:
            return 'There are no items with that key.'
        else:
            for i in range(len(self._buckets[hash_key])):
                if self._buckets[hash_key][i][0] == key:
                    return self._buckets[hash_key][i][1]
                else:
                    return 'There are not items with that key.'

    def set(self, key, val):
        """Pass a value into the table for storage."""
        if not isinstance(key, str):
            raise TypeError('You must enter a word as a key.')
        hash_key = self._hash(key)
        if self._buckets[hash_key] == []:
            self._buckets[hash_key].append((key, val))
        else:
            for i in range(len(self._buckets[hash_key])):
                if self._buckets[hash_key][i][0] == key:
                    gone = self._buckets[hash_key][i][1]
                    self._buckets[hash_key][i] = (key, val)
                    return 'Your data {} has been updated to {} at key {}.'\
                        .format(gone, val, key)
                else:
                    self._buckets[hash_key].append((key, val))

    def _hash(self, key):
        """Hash the data given on set."""
        buckets = self._size
        return self.hash_func(key, buckets)
