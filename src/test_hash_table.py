"""Test hash table."""

import pytest


def test_naive_hash_returns_int_between_zero_and_input():
    """Test navie hash returns an int between zero and len buckets."""
    from hash_table import naive_hash
    word = 'Testing'
    length = 100
    assert naive_hash(word, length) < 100
    assert naive_hash(word, length) >= 0


def test_naive_get_if_item_not_in_table_returns_error_message():
    """Test naive get if item not in table returns error message."""
    from hash_table import HashTable
    table = HashTable()
    assert table.get('Testing') == 'This key does not exist.'


def test_naive_get_item_not_in_table_returns_error_if_other_item_has_key():
    """Test naive get if item not in table returns error message."""
    from hash_table import HashTable
    table = HashTable()
    table.set('Bob', 'Ross')
    assert table.get('Painting') == 'This key does not exist.'


def test_hashtable_raises_type_error_if_not_input_string():
    """Test hashtable raises typeerror if input is not string."""
    from hash_table import HashTable
    table = HashTable()
    with pytest.raises(TypeError):
        table.set(5, 'Test')


def test_horners_hashtable_set_and_get_one_word():
    """Test horners hashtable set and gets one word."""
    from hash_table import HashTable, horner_hash
    table = HashTable(100, horner_hash)
    table.set('Bob', 'Ross')
    bob = table.get('Bob')
    assert bob == 'Ross'


def test_horners_input_same_key_twice_resets_val():
    """Test horners input same key twice resets vala at  key."""
    from hash_table import HashTable, horner_hash
    table = HashTable(10, horner_hash)
    table.set('Ross', 'Ross')
    assert table.set('Ross', 'Bob') == ('Your data Ross has been '
                                        'updated to Bob at key Ross.')
    ross = table.get('Ross')
    assert table.get('Ross') == 'Bob'

