import pytest
from bst import BST


@pytest.fixture(scope="function")
def make_bst():
    b = BST()
    our_list = [4, 2, 6, 1, 3, 7, 5]
    for num in our_list:
        b.insert(num)
    return b


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


def test_delete(make_bst):
    b = make_bst
    b.delete(5)
    a = []
    for i in b.in_order(b._root):
        a.append(i)
    assert a == [1, 2, 3, 4, 6, 7]
    b.delete(2)
    a = []
    for i in b.in_order(b._root):
        a.append(i)
    assert a == [1, 3, 4, 6, 7]
    b.delete(4)
    a = []
    for i in b.in_order(b._root):
        a.append(i)
    assert a == [1, 3, 6, 7]
    b.delete(1)
    a = []
    for i in b.in_order(b._root):
        a.append(i)
    assert a == [3, 6, 7]


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


def test_in_order(make_bst):
    b = make_bst
    a = [1, 2, 3, 4, 5, 6, 7]
    count = 0
    for i in b.in_order(b._root):
        assert a[count] == i._data
        count += 1


def test_pre_order(make_bst):
    b = make_bst
    a = [4, 2, 1, 3, 6, 5, 7]
    count = 0
    for i in b.pre_order(b._root):
        assert i._data == a[count]
        count += 1


def test_post_order(make_bst):
    b = make_bst
    a = [1, 3, 2, 5, 7, 6, 4]
    count = 0
    for i in b.post_order(b._root):
        assert i._data == a[count]
        count += 1


def test_level_order(make_bst):
    b = make_bst
    a = [4, 2, 6, 1, 3, 5, 7]
    count = 0
    for i in b.level_order(b._root):
        assert i._data == a[count]
        count += 1
