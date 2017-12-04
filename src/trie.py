"""Trie tree for storing strings."""


class Node(object):
    """Node class for trie object."""

    def __init__(self, letter):
        """Initialize a new node instance for trie."""
        self.letter = letter
        self.children = {}
        # self.parent = None
        self.end = False


class Trie(object):
    """Trie class for implementing a trie tree object."""

    def __init__(self):
        """Initialize a new instance of trie."""
        self.root = Node('root')
        self._size = 0

    def insert(self, string):
        """Insert the given string into the trie.

        If character in the string is already present, it will be ignored.
        """
        if not isinstance(string, str):
            raise TypeError('You must enter a word.')
        else:
            string = string.lower()
            trace = self.root
            for letter in string:
                if letter in trace.children:
                    trace = trace.children[letter]
                else:
                    trace.children[letter] = Node(letter)
                    trace = trace.children[letter]
            trace.end = True
            self._size += 1

    def contains(self, string):
        """Return True if the string is in the trie, False if not."""
        string = string.lower()
        trace = self.root
        for letter in string:
            if letter in trace.children:
                trace = trace.children[letter]
                if trace.end is True:
                    return True
            else:
                return False

    def size(self):
        """Return the total number of words in trie. 0 if empty."""
        return self._size

    def remove(self, string):
        """Remove given string from trie. If not in tree, raise exception."""
        if self.contains(string) is False:
            raise ValueError('This word is not in the tree.')
        else:
            string = string.lower()
            parent = None
            trace = self.root
            for letter in string:
                if letter in trace.children:
                    parent = trace
                    trace = trace.children[letter]
                    if 
                else:
                    return False
