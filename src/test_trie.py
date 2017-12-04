"""Test trie tree class."""


def test_instantiate_new_trie_has_root(trie):
    """Test that new trie tree has root with value of root."""
    assert trie.root.letter == 'root'


def test_insert_word_creates_node_for_each_letter(trie):
    """Test insert on empty tree creates a node for each letter."""
    trie.insert('Christmas')
    assert trie.size() == 1


def test_insert_two_words_with_same_first_letter_share(trie):
    """Test insert two words with same first letter share node."""
    trie.insert('Christmas')
    trie.insert('Carols')
    childs = trie.root.children['c'].children
    assert list(childs.keys()) == ['h', 'a']
    assert trie.size() == 2


def test_insert_word_creates_end_node(trie):
    """Test insert word creates end node following word."""
    trie.insert('Tree')
    end = trie.root.children['t'].children['r'].children['e'].children['e']
    assert end.end is True


def test_contains_returns_false_if_word_not_in_tree(trie):
    """Test return false if world not in tree."""
    trie.insert('Christmas')
    assert trie.contains('carols') is False


def test_contains_returns_true_if_word_in_tree(trie):
    """Test contains returns true if word in tree."""
    trie.insert('Christmas')
    assert trie.contains('christmas') is True


def test_contains_word_with_shared_letters(trie):
    """Test contains with word sharing multple letters."""
    trie.insert('word')
    trie.insert('world')
    trie.insert('wordsmith')
    assert trie.contains('world') is True
    assert trie.contains('word') is True
    assert trie.contains('wordsmith') is True


def test_size_returns_size_with_three_words(trie):
    """Test size with three words inserted."""
    trie.insert('word')
    trie.insert('world')
    trie.insert('wordsmith')
    assert trie.size() == 3
