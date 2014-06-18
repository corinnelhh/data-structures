import pytest
from queue import Node, Queue


def test_node():
    our_node = Node("first")
    assert our_node.data == "first"
    assert our_node.next is None

    our_next_node = Node("second", our_node)
    assert our_next_node.data == "second"
    assert our_next_node.next is our_node


def test_queue_creation():
    our_queue = Queue()
    assert our_queue.head is None
    assert our_queue.tail is None
    assert our_queue.size == 0


def test_enqueue():
    our_queue = Queue()
    our_queue.enqueue("first")

    assert our_queue.head.data == "first"
    assert our_queue.tail.data == "first"
    assert our_queue.size == 1

    our_queue.enqueue("second")
    our_queue.enqueue("third")

    assert our_queue.head.data == "third"
    assert our_queue.tail.data == "first"
    assert our_queue.size == 3

    assert our_queue.head.next.data == "second"
    assert our_queue.tail.last.data == "second"
    assert our_queue.head.next.last.data == "third"
    assert our_queue.tail.next is None


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
