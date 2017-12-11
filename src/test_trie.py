"""Test that trie tree."""
import pytest


def test_basic():
    """Add a banana."""
    from trie import Trie
    t = Trie()
    t.insert('Banana')
    assert 'B' in t.root.next_node


def test_contains_true():
    """Contain a banana."""
    from trie import Trie
    t = Trie()
    t.insert('Banana')
    assert t.contains('Banana')


def test_contains_false():
    """Contain a banana, not an apple."""
    from trie import Trie
    t = Trie()
    t.insert('Banana')
    assert not t.contains('Apple')


def test_contains_partial_false():
    """Partial word returns false."""
    from trie import Trie
    t = Trie()
    t.insert('Banana')
    assert not t.contains('ban')


def test_does_contain_ban():
    """Adding a partial word causes true return."""
    from trie import Trie
    t = Trie()
    t.insert('Banana')
    t.insert('ban')
    assert t.contains('ban')


def test_removing_removes_word():
    """Remove will remove words."""
    from trie import Trie
    t = Trie()
    t.insert('Banana')
    t.remove('Banana')
    assert not t.contains('Banana')


def test_inserting_dupes_are_ignored():
    """Banana don't go in twice."""
    from trie import Trie
    t = Trie()
    t.insert('Banana')
    t.insert('Banana')
    assert t.size == 1


def test_dict_updates():
    """The dict of words stays updated."""
    from trie import Trie
    t = Trie()
    t.insert('Apple')
    t.insert('Banana')
    t.insert('Stalin')
    assert 'Stalin' in t.dict_of_words


def test_removing_banana_leaves_ban_intact():
    """Bananananana."""
    from trie import Trie
    t = Trie()
    t.insert('Banana')
    t.insert('Ban')
    assert t.contains('Ban')
    t.remove('Banana')
    assert t.contains('Ban')
    assert 'Ban' in t.dict_of_words
    assert t.size == 1