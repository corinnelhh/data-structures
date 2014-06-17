#!/usr/bin/env python
from binary_heap import BinaryHeap
import random
import pytest


def test_init_max():
    #TEST for MAX
    a = BinaryHeap("max",*[random.randint(0,100) for i in range(37)])
    index = a._size - 1
    while index :
        assert a._list[index] <= a._list[(index-1)//2]
        index -= 1

def test_init_min():
    #TEST for MIN
    a = BinaryHeap("min",*[random.randint(0,100) for i in range(37)])
    index = a._size - 1
    while index :
        assert a._list[index] >= a._list[(index-1)//2]
        index -= 1

def test_push():
    for x in range(50):
        a = BinaryHeap()
        for i in range(47):
            a.push(random.randint(0,100))
        assert max(a._list) == a._list[0]
    index = a._size - 1
    while index :
        assert a._list[index] <= a._list[(index-1)//2]
        index -= 1

def test_pop():
    bt = BinaryHeap()
    for i in range(50):
        bt.push(random.randint(0,1000))

    for i in range(49):
        tmp = max(bt._list[1:])
        bt.pop()
        assert  tmp == bt._list[0]
    bt.pop()
    assert 0 == len(bt._list)

    # testing for empty list pop
    a = BinaryHeap()
    with pytest.raises(IndexError):
        assert a.pop()


