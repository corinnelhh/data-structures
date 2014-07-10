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
def read_test_lexicon():
    a = []
    with open("/usr/share/dict/words", 'rb') as f:
        a.append(f.read())
    return a


def test_hasher():
    ht = HashTable()
    a = ht.hash("alice")
    b = ht.hash("elica")
    c = ht.hash("Alice")
    assert a == b
    assert a != c


def test_hash_fill_table(read_test_lexicon):
    ht = HashTable()
    for i in read_test_lexicon:
        ht.set(i)
    for i in read_test_lexicon:
        assert ht.get(i) == i




