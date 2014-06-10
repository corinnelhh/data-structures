import pytest
from queue import Node, Queue

def test_Node():
    a = Node(5)
    b = Node('x')
    assert a.data == 5
    assert a.next is None
    assert b is not a
    assert b.data == 'x'

def test_queue_init():
    q = Queue(1,'a',2,'b',3)
    assert q.head.data == 1
    assert q.tail.data == 3
    assert q.size() == 5
    assert q.tail.next is None
    assert q.head.next.data == 'a'

def test_enqueue():
    q = Queue()
    q.enqueue('a')
    assert q.tail is q.head         #testing for a Queue of 1 element
    q.dequeue()
    assert q.size() == 0
    q.enqueue('b')
    assert q.size() == 1
    assert q.head.data == 'b'
    q.enqueue('c')
    assert q.size() == 2
    q.enqueue('d')
    assert q.tail.data == 'd'

def test_dequeue():
    q = Queue(u'first', u'second', u'third', u'fourth', u'fifth')
    q.enqueue(u'sixth')
    q.enqueue(u'seventh')
    assert q.dequeue() == u'first'         # 1st in line got removed
    assert q.size() == 6
    q.dequeue()                            # 2nd in line
    q.dequeue()                            # 3rd in line
    assert q.dequeue() == u'fourth'        # 4th in line
    assert q.size() == 3

def test_size():
    q = Queue(1,2,3,4,5)
    assert q.size() is 5
    q.enqueue(6)
    assert q.size() == 6
    q.dequeue()
    q.dequeue()
    assert q.size() == 4