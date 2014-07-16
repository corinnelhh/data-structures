import pytest
from duy_bst import BST

@pytest.fixture(scope="function")
def make_bst():
    b = BST()
    our_list = [32, 16, 48, 8, 24, 40, 56, 11, 22, 33, 10, 55]
    for num in our_list:
        b.insert(num)
    return b

def test_insert():
    b = BST()
    b.insert(50)
    assert b.size() == 1
    assert b.depth(50) == 1
    assert b._root == 50
    b.insert(25)
    b.insert(75)
    assert b._left(50) == 25
    assert b._right(50) == 75
    assert b._parent(25) == 50
    assert b._parent(75) == 50
    assert not b._left(25)
    assert not b._right(75)


def test_balance(make_bst):
    b = make_bst
    assert b.balance(32) == -1
    assert b.balance(48) == 0
    assert b.balance(33) == 0
    assert b.balance(40) == -1
    assert b.balance(10) == 0
    assert b.balance(11) == -1
    assert b.balance(16) == -1
    assert b.balance(8) == 2


def test_in_order(make_bst):
    b = make_bst
    res = []
    for i in b.in_order(32):
        res.append(i)
    assert res == [8, 10, 11, 16, 22, 24, 32, 33, 40, 48, 55, 56]


def test_pre_order(make_bst):
    b = make_bst
    res = []
    for i in b.pre_order(32):
        res.append(i)
    assert res == [32, 16, 8, 11, 10, 24, 22, 48, 40, 33, 56, 55]


def test_post_order(make_bst):
    b = make_bst
    res = []
    for i in b.post_order(32):
        res.append(i)
    assert res == [10, 11, 8, 22, 24, 16, 33, 40, 55, 56, 48, 32]


def test_level_order(make_bst):
    b = make_bst
    res = []
    for i in b.level_order():
        res.append(i)
    assert res == [32, 16, 48, 8, 24, 40, 56, 11, 22, 33, 55, 10]


def test_delete_node(make_bst):
    b = make_bst
    b.delete_node(32)
    res = []
    for i in b.level_order():
        res.append(i)
    assert res == [24, 16, 48, 8, 22, 40, 56, 11, 33, 55, 10]
    b.delete_node(16)
    res = []
    for i in b.level_order():
        res.append(i)
    assert res == [24, 11, 48, 8, 22, 40, 56, 10, 33, 55]
    b.delete_node(48)
    res = []
    for i in b.level_order():
        res.append(i)
    assert res == [24, 11, 40, 8, 22, 33, 56, 10, 55]
    b.delete_node(8)
    res = []
    for i in b.level_order():
        res.append(i)
    assert res == [24, 11, 40, 10, 22, 33, 56, 55]
