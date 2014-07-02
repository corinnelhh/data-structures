import pytest
from bst import BST


def test_insert():
    btree = BST()
    btree.insert(1)
    assert btree._depth == 1
    assert btree._root._data == 1
    current_node = btree._root
    btree.insert(1)
    assert btree._depth == 1
    assert btree._root._data == 1
    btree.insert(3)
    current_node = current_node._right
    assert btree._depth == 2
    assert current_node._data == 3
    btree.insert(5)
    current_node = current_node._right
    assert btree._depth == 3
    assert current_node._data == 5
    btree.insert(2)
    assert btree._depth == 3
    assert btree._root._right._left._data == 2


def test_contains():
    btree = BST()
    btree.insert(3)
    btree.insert(2)
    btree.insert(5)
    btree.insert(4)
    btree.insert(1)
    assert btree.contains(5) is True
    assert btree.contains(1) is True
    assert btree.contains(10) is False


def test_balanced():
    b = BST()
    b.insert(10)
    b.insert(5)
    b.insert(15)
    b.insert(3)
    b.insert(2)
    b.insert(1)
    assert b._depth == 5
    assert b._size == 6
    assert b.is_balanced(b._root) == -3
    assert b.is_balanced(b._root._left) == -3
    assert b.is_balanced(b._root._right) == -0
