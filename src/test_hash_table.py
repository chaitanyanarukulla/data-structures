"""Test hash table."""
import os
import pytest

def test_hashtable_if_works():
    """Just seeing if the thing works."""
    from hash_table import HashTable
    table = HashTable(100)
    table.set('Mark', 'Mark')
    mark = table.get('Mark')
    assert mark == 'Mark'


def test_input_same_key_twice_resets_val():
    """Test set at same key twice updates value at key."""
    from hash_table import HashTable
    table = HashTable(10)
    table.set('Mark', 'Mark')
    assert table.set('Mark', 'Reynoso') == ('Your data Mark has been '
                                            'updated to Reynoso at key Mark.')
    mark = table.get('Mark')
    assert table.get('Mark') == 'Reynoso'



# word_list = []
# with open('/usr/share/dict/words', 'r') as dictionary:
#     for line in dictionary:
#         word_list.append((line, line))


# @pytest.mark.parametrize('input_word, output_word', word_list)
# def test_all_dictionary_words(input_word, output_word):
#     """Test all the entire dictionary."""
#     from hash_table import HashTable
#     table = HashTable(len(word_list))
#     table.set(input_word, input_word)
#     output = table.get(input_word)
#     assert output == output_word
