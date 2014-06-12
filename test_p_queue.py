#!/usr/bin/env python
from p_queue import Node, P_Queue
import random
import pytest

def test_node():
    a = Node(100, 10, 1)
    assert a._data == 100
    assert a._priority == 10
    assert a._order == 1

def test_init():
    a = P_Queue()
    assert a._size == 0
    assert a._counter == 0

def test_insert():
    a = P_Queue()
    for i in range(1000):
        val = random.randint(0,1000)
        pri = random.randint(0,20)
        a.insert(val, pri)
    index = a._size - 1
    while index :
        assert a._list[index]._priority <= a._list[(index-1)>>1]._priority
        if (a._list[index]._priority == a._list[(index-1)>>1]._priority):
            assert a._list[index]._order >= a._list[(index-1)>>1]._order
        index -= 1

def test_peek():
    a = P_Queue()
    for i in range(1000):
        val = random.randint(0,1000)
        pri = random.randint(0,20)
        a.insert(val, pri)
    assert a.peek()._priority >= a._list[1]._priority

def test_pop():
    a = P_Queue()
    with pytest.raises(IndexError):
        assert a.pop()

def test_pop_2():
    a = P_Queue()
    for i in range(1000):
        val = random.randint(0,10000)
        pri = random.randint(0,200)
        a.insert(val, pri)
    for i in range(999):
        node = a.pop()
        assert node._priority >= a.peek()._priority
        if node._priority == a.peek()._priority:
            assert node._order < a.peek()._order
