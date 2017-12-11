"""Hash table."""


def naive_hash(word, buckets):
    """Hash for strings."""
    hash_val = 0
    for letter in word:
        hash_val += ord(letter)
    return hash_val % buckets


def horner_hash(word, buckets):
    """Using horner's rule for hashing key."""
    constant = 37
    result = 0
    for letter in word:
        result = result * constant + ord(letter)
    return result % buckets


class HashTable(object):
    """Hash table class."""

    def __init__(self, size=10, hash_func=naive_hash):
        """Initialize a new hashtable."""
        self.hash_func = hash_func
        self._size = size
        self._buckets = [[] for x in range(self._size)]

    def get(self, key):
        """Return the value of the key given."""
        hash_key = self._hash(key)
        if self._buckets[hash_key] == []:
            return 'This key does not exist.'
        else:
            for idx, item in enumerate(self._buckets[hash_key]):
                if item[0] == key:
                    return self._buckets[hash_key][idx][1]
                else:
                    return 'This key does not exist.'

    def set(self, key, val):
        """Pass a value into the table for storage."""
        if not isinstance(key, str):
            raise TypeError('You must enter a word as a key.')
        hash_key = self._hash(key)
        if self._buckets[hash_key] == []:
            self._buckets[hash_key].append((key, val))
        else:
            for idx, item in enumerate(self._buckets[hash_key]):
                if item[0] == key:
                    gone = item[1]
                    self._buckets[hash_key][idx] = (key, val)
                    return 'Your data {} has been updated to {} at key {}.'\
                        .format(gone, val, key)
                else:
                    self._buckets[hash_key].append((key, val))

    def _hash(self, key):
        """Hash the data on set."""
        buckets = self._size
        return self.hash_func(key, buckets)
