<<<<<<< HEAD
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
=======
"""Test trie tree class."""
import pytest


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
    assert 'a' in list(childs.keys())
    assert 'h' in list(childs.keys())
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


def test_trie_remove_reduces_size(trie_10_words):
    """Test trie remove reduces size as needed."""
    trie_10_words.remove('carol')
    trie_10_words.remove('cookie')
    assert trie_10_words.size() == 8


def test_trie_remove_word_gone_from_contains(trie_10_words):
    """Test trie remove word is gone from contains."""
    trie_10_words.remove('party')
    assert trie_10_words.contains('party') is False


def test_trie_remove_word_with_shared_letters_leaves_other_word(trie_10_words):
    """Test trie remove does not change other words when sharing letters."""
    trie_10_words.insert('Sweet')
    trie_10_words.insert('Sweetheart')
    trie_10_words.insert('Sweetie')
    trie_10_words.insert('Sweat')
    trie_10_words.insert('Sweatshirt')
    trie_10_words.insert('Sweaty')
    trie_10_words.remove('sweat')
    assert trie_10_words.contains('sweat') is False
    assert trie_10_words.contains('sweet') is True
    assert trie_10_words.contains('sweetheart') is True
    assert trie_10_words.contains('Sweetie') is True
    assert trie_10_words.contains('sweaty') is True
    assert trie_10_words.contains('sweatshirt') is True
    assert trie_10_words.size() == 15


def test_trie_remove_multiple_times_in_chained_words(trie_10_words):
    """Test trie remove many words from shared letters only changes removed."""
    trie_10_words.insert('Sweet')
    trie_10_words.insert('Sweetheart')
    trie_10_words.insert('Sweetie')
    trie_10_words.insert('Sweat')
    trie_10_words.insert('Sweatshirt')
    trie_10_words.insert('Sweaty')
    trie_10_words.remove('sweaty')
    trie_10_words.remove('sweater')
    trie_10_words.remove('sweatshirt')
    trie_10_words.remove('sweet')
    assert trie_10_words.contains('sweat') is False
    assert trie_10_words.contains('sweet') is False
    assert trie_10_words.contains('sweetheart') is True
    assert trie_10_words.contains('Sweetie') is True
    assert trie_10_words.contains('sweaty') is False
    assert trie_10_words.contains('sweatshirt') is False
    assert trie_10_words.size() == 12


def test_remove_if_word_reaches_root(trie):
    """Test remove when word reaches root."""
    trie.insert('humbug')
    trie.remove('humbug')
    assert len(trie.root.children) == 0
    assert trie.contains('humbug') is False
    assert trie.size() == 0


def test_remove_raises_valueerror_if_word_not_in_tree(trie):
    """Test remove raises value error if word not in tree."""
    with pytest.raises(ValueError):
        trie.remove('humbug')


def test_insert_raises_typeerror_if_input_not_string(trie):
    """Test insert raises type error if input not string."""
    with pytest.raises(TypeError):
        trie.insert(40)
>>>>>>> 3b0fbd79798eb08b38ec6f16485831bc6e47cf68
