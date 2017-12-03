"""Test hash table."""
import os

import pytest


def test_naive_hashtable_set_and_get_one_word():
    """Just seeing if the thing works."""
    from hash_table import HashTable
    table = HashTable(100)
    table.set('Mark', 'Mark')
    mark = table.get('Mark')
    assert mark == 'Mark'


def test_naive_input_same_key_twice_resets_val():
    """Test set at same key twice updates value at key."""
    from hash_table import HashTable
    table = HashTable(10)
    table.set('Mark', 'Mark')
    assert table.set('Mark', 'Reynoso') == ('Your data Mark has been '
                                            'updated to Reynoso at key Mark.')
    mark = table.get('Mark')
    assert table.get('Mark') == 'Reynoso'


def test_naive_hash_returns_int_between_zero_and_input():
    """Test navie hash returns an int between zero and len buckets."""
    from hash_table import naive_hash
    word = 'Hashtale'
    length = 100
    assert naive_hash(word, length) < 100
    assert naive_hash(word, length) >= 0


def test_naive_get_if_item_not_in_table_returns_error_message():
    """Test naive get if item not in table returns error message."""
    from hash_table import HashTable
    table = HashTable()
    assert table.get('Christmas') == 'There are no items with that key.'


def test_naive_get_item_not_in_table_returns_error_if_other_item_has_key():
    """Test naive get if item not in table returns error message."""
    from hash_table import HashTable
    table = HashTable()
    table.set('Christmas', 'Christmas')
    assert table.get('Thanksgiving') == 'There are no items with that key.'


def test_hashtable_raises_type_error_if_not_input_string():
    """Test hashtable raises typeerror if input is not string."""
    from hash_table import HashTable
    table = HashTable()
    with pytest.raises(TypeError):
        table.set(5, 'Test')


def test_horners_hashtable_set_and_get_one_word():
    """Just seeing if the thing works."""
    from hash_table import HashTable, horner_hash
    table = HashTable(100, horner_hash)
    table.set('Mark', 'Mark')
    mark = table.get('Mark')
    assert mark == 'Mark'


def test_horners_input_same_key_twice_resets_val():
    """Test set at same key twice updates value at key."""
    from hash_table import HashTable, horner_hash
    table = HashTable(10, horner_hash)
    table.set('Mark', 'Mark')
    assert table.set('Mark', 'Reynoso') == ('Your data Mark has been '
                                            'updated to Reynoso at key Mark.')
    mark = table.get('Mark')
    assert table.get('Mark') == 'Reynoso'


def test_horners_hash_returns_int_between_zero_and_input():
    """Test navie hash returns an int between zero and len buckets."""
    from hash_table import horner_hash
    word = 'Hashtale'
    length = 100
    assert horner_hash(word, length) < 100
    assert horner_hash(word, length) >= 0


def test_horners_get_if_item_not_in_table_returns_error_message():
    """Test horners get if item not in table returns error message."""
    from hash_table import HashTable, horner_hash
    table = HashTable(10, horner_hash)
    assert table.get('Christmas') == 'There are no items with that key.'


def test_horners_get_item_not_in_table_returns_error_if_other_item_has_key():
    """Test horners get if item not in table returns error message."""
    from hash_table import HashTable, horner_hash
    table = HashTable(10, horner_hash)
    table.set('Christmas', 'Christmas')
    assert table.get('Thanksgiving') == 'There are no items with that key.'


# <-------- Test entire dictionary --------->
# word_list = []
# with open('/usr/share/dict/words', 'r') as dictionary:
#     for line in dictionary:
#         word_list.append((line, line))


# @pytest.mark.parametrize('input_word, output_word', word_list)
# def test_naive_all_dictionary_words(input_word, output_word):
#     """Test all the entire dictionary."""
#     from hash_table import HashTable
#     table = HashTable(len(word_list))
#     table.set(input_word, input_word)
#     output = table.get(input_word)
#     assert output == output_word


# @pytest.mark.parametrize('input_word, output_word', word_list)
# def test_horners_all_dictionary_words(input_word, output_word):
#     """Test all the entire dictionary."""
#     from hash_table import HashTable, horner_hash
#     table = HashTable(len(word_list), horner_hash)
#     table.set(input_word, input_word)
#     output = table.get(input_word)
#     assert output == output_word
