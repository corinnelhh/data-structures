import pytest
from hash import HashTable

"""
Every Unix-like operating system provides a list of dictionary words
 in a file at /usr/share/dict/words. This very long list (over 250,000
    on my system) can provide a reasonable test bed for a hash table.
 For your tests, use this file.  Insert all the word from the file into
 your hashtable, with the key and the value being the same (in other words,
  my_table.set('pear', 'pear')) Then, you can test by using each word as a key,
   and verify that the result you get back is the same word.
"""


@pytest.fixture(scope="session")
def fill_test_lexicon():
    with open("/usr/share/dict/words", 'rb') as f:
        our_dict = f.readlines()
    return our_dict


def test_hash_find_vals(fill_test_lexicon):
    our_dict = fill_test_lexicon
    pass
