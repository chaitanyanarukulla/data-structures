"""Binary Search Tree."""


class Node(object):
    """Node object for bst."""

    def __init__(self, data, lc=None, rc=None, mom=None):
        """Initialize a new node."""
        self.data = data
        self.left = lc
        self.right = rc
        self.parent = mom


class Bst(object):
    """Binary Search Tree class."""

    def __init__(self, iterable=None):
        """Initiate a new instance of bst."""
        self.root = None
        self._size = 0
        if isinstance(iterable, (list, tuple)):
            for item in iterable:
                self.insert(item)

    def insert(self, val):
        """Insert a value into bst."""
        if not isinstance(val, (int, float)):
            raise ValueError('Sorry, I only take numbers right now.')
        if self.root is None:
            self.root = Node(val)
            self._size += 1
            return
        elif val == self.root.data:
            raise ValueError('This node already exists.')
        current = self.root
        while current:
            if val == current.data:
                    raise ValueError('This node already exists.')
            elif val < current.data:
                if current.left:
                    current = current.left
                else:
                    current.left = Node(val)
                    current.left.parent = current
                    self._check_balance(current)
                    self._size += 1
                    break
            elif val > current.data:
                if current.right:
                    current = current.right
                else:
                    current.right = Node(val)
                    current.right.parent = current
                    self._check_balance(current)
                    self._size += 1
                    break

    def search(self, val):
        """Search bst for val and return node of this val, else none."""
        if self.root is None or not isinstance(val, (int, float)):
            return
        current = self.root
        while current:
            if val == current.data:
                return current
            elif val < current.data:
                current = current.left
            elif val > current.data:
                current = current.right

    def size(self):
        """Return size of bst."""
        return self._size

    def depth(self, root):
        """Return total number of levels in bst."""
        if root is None:
            return 0
        elif root == self.root and not root.left and not root.right:
            return 0
        elif not root.left and not root.right:
            return 1
        elif root.left and not root.right:
            return self.depth(root.left) + 1
        elif root.right and not root.left:
            return self.depth(root.right) + 1
        else:
            return max(self.depth(root.left), self.depth(root.right)) + 1

    def contains(self, val):
        """Search for val in tree and return boolean."""
        if self.search(val) is not None:
            return True
        else:
            return False

    def balance(self, node):
        """Return integer indicating balance of tree."""
        if node is None:
            return 'There are no nodes in this tree.'
        if not node.left and not node.right:
            return 0
        else:
            return self.depth(node.left) - self.depth(node.right)

    def breadth_first(self):
        """Return generator of breadth first search."""
        if self.root is None:
            raise ValueError('There are no nodes in this tree.')
        bfs = [self.root]
        while bfs:
            current = bfs.pop(0)
            if current.left:
                bfs.append(current.left)
            if current.right:
                bfs.append(current.right)
            yield current.data

    def in_order(self):
        """Return generator of in order search."""
        if self.root is None:
            raise ValueError('There are no nodes in this tree.')
        current = self.root
        ios = []
        while current or ios:
            if current:
                ios.append(current)
                current = current.left
            else:
                current = ios.pop()
                yield current.data
                current = current.right

    def pre_order(self):
        """Return generator of pre order search."""
        if self.root is None:
            raise ValueError('There are no nodes in this tree.')
        current = self.root
        ios = []
        while current or ios:
            if current:
                yield current.data
                if current.right:
                    ios.append(current.right)
                current = current.left
            else:
                current = ios.pop()

    def post_order(self):
        """Return generator of post order wearch."""
        if self.root is None:
            raise ValueError('There are no nodes in this tree.')
        current = self.root
        child = None
        ios = []
        while current or ios:
            if current:
                ios.append(current)
                current = current.left
            else:
                if ios[-1].right and ios[-1].right is not child:
                    current = ios[-1].right
                else:
                    child = ios.pop()
                    yield child.data

    def delete(self, val):
        """Delete node with given val."""
        if self.root is None or not isinstance(val, (int, float)):
            return
        on_deck = self.search(val)
        if not on_deck.left and not on_deck.right:
            self._delete_no_children(on_deck)
        elif on_deck.left and not on_deck.right:
            self._delete_one_child(on_deck)
        elif on_deck.right and not on_deck.left:
            self._delete_one_child(on_deck)
        elif on_deck.left and on_deck.right:
            self._delete_two_children(on_deck)

    def _delete_no_children(self, on_deck):
        """Delete node with no children."""
        self._size -= 1
        if not on_deck.parent:
            self.root = None
        elif on_deck.parent.data < on_deck.data:
            on_deck.parent.right = None
        elif on_deck.parent.data > on_deck.data:
            on_deck.parent.left = None
        self._check_balance(on_deck.parent)

    def _delete_one_child(self, on_deck):
        """Delete node with only one child."""
        self._size -= 1
        if on_deck == self.root:
            if self.root.right:
                self.root = self.root.right
                self.root.right = on_deck.right
                self.root.left = on_deck.left
            else:
                self.root = self.root.left
                self.root.right = on_deck.right
                self.root.left = on_deck.left
            self.root.parent is None
        elif on_deck.parent.data < on_deck.data:
            if on_deck.left:
                on_deck.parent.right = on_deck.left
                on_deck.left.parent = on_deck.parent
            elif on_deck.right:
                on_deck.parent.right = on_deck.right
                on_deck.right.parent = on_deck.parent
        else:
            if on_deck.left:
                on_deck.parent.left = on_deck.left
                on_deck.left.parent = on_deck.parent
            elif on_deck.right:
                on_deck.parent.left = on_deck.right
                on_deck.right.parent = on_deck.parent
        self._check_balance(on_deck.parent)

    def _delete_two_children(self, on_deck):
        """Delete node with two children."""
        self._size -= 1
        current = on_deck.right
        while current:
            if current.left:
                current = current.left
            else:
                break
        if current.parent == on_deck:
            current.parent = on_deck.parent
            current.left = on_deck.left
            if current.parent:
                if current.parent.data < current.data:
                    current.parent.right = current
                else:
                    current.parent.left = current
            else:
                self.root = current
        elif current.right:
            current.right.parent = current.parent
            current.parent.left = current.right
            current.parent = on_deck.parent
            current.right = on_deck.right
            current.left = on_deck.left
            current.left.parent = current
            current.right.parent = current
            if current.parent:
                if current.parent.data < current.data:
                    current.parent.right = current
                else:
                    current.parent.left = current
            else:
                self.root = current
        else:
            current.parent.left = None
            current.parent = on_deck.parent
            current.right = on_deck.right
            current.left = on_deck.left
            current.left.parent = current
            current.right.parent = current
            if current.parent:
                if current.parent.data < current.data:
                    current.parent.right = current
                else:
                    current.parent.left = current
            else:
                self.root = current
        self._check_balance(on_deck.parent)

    def _check_balance(self, node):
        """Check parent nodes for balance on insert or delete."""
        check = node.parent
        while check:
            if self.balance(check) > 1:
                if self.balance(check.left) >= 0:
                    self._right_rotation(check)
                else:
                    self._left_rotation(check.left)
                    self._right_rotation(check)
            elif self.balance(check) < -1:
                if self.balance(check.right) <= 0:
                    self._left_rotation(check)
                else:
                    self._right_rotation(check.right)
                    self._left_rotation(check)
            else:
                check = check.parent

    def _right_rotation(self, node):
        """Rotate node to the right."""
        swing = node.left

        swing.parent = node.parent
        node.parent = swing
        swing.right = node
        node.left = None
        if swing.parent is None:
            self.root = swing

    def _left_rotation(self, node):
        """Rotate node to the left."""
        swing = node.right

        swing.parent = node.parent
        node.parent = swing
        swing.left = node
        node.right = None
        if swing.parent is None:
            self.root = swing


if __name__ == '__main__':  # pragma: no cover
    import timeit

    insert_time_ub = Bst()
    num = (x for x in range(1000))
    a = timeit.timeit('insert_time_ub.insert(next(num))',
                      setup='from __main__ import insert_time_ub, num',
                      number=1000)
    search_time_ub = Bst()
    for i in range(100):
        search_time_ub.insert(i)
    b = timeit.timeit('search_time_ub.search(99)',
                      setup='from __main__ import search_time_ub',
                      number=1000)
    c = timeit.timeit('search_time_ub.search(0)',
                      setup='from __main__ import search_time_ub',
                      number=1000)
    insert_time_b = Bst()

    def insert_time(val):
        """."""
        if (500 + val) % 2 == 0:
            insert_time_b.insert(500 + val)
        else:
            insert_time_b.insert(500 - val)

    num_b = (x for x in range(1000))
    d = timeit.timeit('insert_time(next(num_b))',
                      setup='from __main__ import insert_time, num_b',
                      number=1000)

    search_time_b = Bst()
    for i in range(1000):
        if (500 + i) % 2 == 0:
            search_time_b.insert(500 + i)
        else:
            search_time_b.insert(500 - i)
    e = timeit.timeit('search_time_b.search(999)',
                      setup='from __main__ import search_time_b',
                      number=1000)
    f = timeit.timeit('search_time_b.search(500)',
                      setup='from __main__ import search_time_b',
                      number=1000)

    print('The following time relates to worst case insert.')
    print('Insert unbalanced: {}'.format(a))
    print('Insert balanced: {}'.format(d))
    print('\nThe following time relates to worst case search.')
    print('Search unbalanced leaf: {}'.format(b))
    print('Search balanced leaf: {}'.format(e))
    print('\nThe following time relates to best base search.')
    print('Search unbalanced head: {}'.format(c))
    print('Search balanced head: {}'.format(f))
