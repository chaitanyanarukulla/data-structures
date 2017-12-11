<<<<<<< HEAD
"""Trie."""


class Node(object):
    """Creates a node object."""

    def __init__(self, value=None, next_node=None):
        """Constructor for the Node object."""
        self.value = value
        self.next_node = {}
        self.entire_word = ""


class Trie(object):
    """Get that Trie, son."""

    def __init__(self):
        """Construct the trie, all smooth-like."""
        self.size = 0
        self.root = Node()
        self.dict_of_words = {}

    def insert(self, string):
        """Will insert a string into the trie. Duplicates will be ignored."""
        if string is '':
            return ValueError('You need to insert text')
        current_node = self.root
        string.split()
        i = 0
        while i < len(string):
            letter = string[i]
            if letter in current_node.next_node:
                i += 1
                current_node = current_node.next_node[letter]
            else:
                current_node.next_node[letter] = Node(letter)
                current_node = current_node.next_node[letter]
                i += 1
        if not current_node.entire_word:
            current_node.entire_word = string
            self.dict_of_words[string] = True
            self.size += 1

    def contains(self, string):
        """Will return True if the string is in the trie, False if not."""
        if string is'':
            return False
        return string in self.dict_of_words

    def _size(self):
        """Will return the total number of words in the trie. 0 if empty."""
        return self.size

    def remove(self, string):
        """Will remove the given string from the trie."""
        if string is '':
            return False
        if string not in self.dict_of_words:
            return False
        initial = string
        string.split()
        i = 0
        current_node = self.root
        letter = string[i]
        last_node = self.root
        last_key = None
        while i < len(string):
            letter = string[i]
            if letter in current_node.next_node:
                if len(current_node.next_node) > 1:
                    last_node = current_node
                    last_key = i
                i += 1
                current_node = current_node.next_node[letter]
            else:
                raise Exception('Something went wrong')
        current_node.entire_word = False
        last_node.next_node.pop(last_key, None)
        self.dict_of_words.pop(initial, None)
        self.size += -1
=======
"""Trie tree for storing strings."""


class Node(object):
    """Node class for trie object."""

    def __init__(self, letter):
        """Initialize a new node instance for trie."""
        self.letter = letter
        self.children = {}
        self.parent = None
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
        string = string.lower()
        trace = self.root
        for letter in string:
            if letter in trace.children:
                trace = trace.children[letter]
            else:
                trace.children[letter] = Node(letter)
                trace.children[letter].parent = trace
                trace = trace.children[letter]
        trace.end = True
        self._size += 1

    def contains(self, string):
        """Return True if the string is in the trie, False if not."""
        if not isinstance(string, str):
            raise TypeError('You must search for a word.')
        string = string.lower()
        trace = self.root
        for idx, letter in enumerate(string):
            if letter in trace.children:
                trace = trace.children[letter]
                if trace.end is True and idx == len(string) - 1:
                    return True
                elif trace.end is False and idx == len(string) - 1:
                    return False
            else:
                return False

    def size(self):
        """Return the total number of words in trie. 0 if empty."""
        return self._size

    def remove(self, string):
        """Remove given string from trie. If not in tree, raise exception."""
        if self.contains(string) is False:
            raise ValueError('This word is not in the tree.')
        string = string.lower()
        trace = self.root
        for letter in string:
            trace = trace.children[letter]
        if len(trace.children) > 0:
            trace.end = False
        else:
            last = None
            while True:
                if trace.letter == 'root':
                    del trace.children[last]
                    break
                elif len(trace.children) <= 1:
                    last = trace.letter
                    trace = trace.parent
                else:
                    del trace.children[last]
                    break
        self._size -= 1
>>>>>>> 3b0fbd79798eb08b38ec6f16485831bc6e47cf68
