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
    q = Queue(1, 'a', 2, 'b', 3)
    assert q.head.data == 1
    assert q.tail.data == 3
    assert q.size() == 5
    assert q.tail.next is None
    assert q.head.next.data == 'a'


def test_enqueue():
    q = Queue()
    q.enqueue('a')
    assert q.tail is q.head  # testing for a Queue of 1 element
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
    our_list = ["first", "second", "third"]
    our_queue = Queue(our_list)

    assert our_queue.size == 3

    assert our_queue.dequeue() == "first"

    assert our_queue.head.data == "third"
    assert our_queue.tail.data == "second"

    assert our_queue.size == 2

    our_queue.dequeue()
    our_queue.dequeue()

    with pytest.raises(IndexError):
        our_queue.dequeue()


def test_size_me():
    our_queue = Queue()
    our_queue.enqueue("first")

    assert our_queue.size_me() == 1

    our_queue.enqueue("second")
    our_queue.enqueue("third")

    assert our_queue.size_me() == 3
