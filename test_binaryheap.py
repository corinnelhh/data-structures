#!/usr/bin/env python
from binaryheap import BinaryHeap
import random


def test_init():
    pass

def test_push():
    bt = BinaryHeap()
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

def test_pop():
    bt = BinaryHeap()
    for i in range(50):
        bt.push(random.randint(0,100))
    for i in range(49):
        tmp = max(bt._list[1:])
        bt.pop()
        assert  tmp == bt._list[0]






