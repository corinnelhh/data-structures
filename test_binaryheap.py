#!/usr/bin/env python
from binaryheap import BinaryHeap
import random


def test_init():
    pass

def test_push_max():
    bt = BinaryHeap(1)
    tmp = random.randint(0,100)
    bt.push(tmp)
    assert bt._list[0] == tmp
    bt.push(random.randint(0,100))
    bt.push(random.randint(0,100))
    bt.push(random.randint(0,100))
    bt.push(random.randint(0,100))
    bt.push(random.randint(0,100))
    bt.push(random.randint(0,100))
    assert max(bt._list) == bt._list[0]
    index = len(bt._list)-1
    while index :
        assert bt._list[index] <= bt._list[(index-1)//2]
        index -= 1


def test_push_min():
    bt = BinaryHeap(0)
    tmp = random.randint(0,100)
    bt.push(tmp)
    assert bt._list[0] == tmp
    bt.push(random.randint(0,100))
    bt.push(random.randint(0,100))
    bt.push(random.randint(0,100))
    bt.push(random.randint(0,100))
    bt.push(random.randint(0,100))
    bt.push(random.randint(0,100))
    assert min(bt._list) == bt._list[0]
    index = len(bt._list)-1
    while index :
        assert bt._list[index] >= bt._list[(index-1)//2]
        index -= 1

def test_pop_max():
    bt = BinaryHeap(1)
    for i in range(50):
        bt.push(random.randint(0,1000))

    for i in range(49):
        tmp = max(bt._list[1:])
        bt.pop()
        assert  tmp == bt._list[0]
    bt.pop()
    assert 0 == len(bt._list)


def test_pop_min():
    bt = BinaryHeap(0)
    for i in range(50):
        bt.push(random.randint(0,1000))

    for i in range(49):
        tmp = min(bt._list[1:])
        bt.pop()
        assert  tmp == bt._list[0]
    bt.pop()
    assert 0 == len(bt._list)


