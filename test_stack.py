import pytest
from stack import Node, Stack


def test_node():
    our_node = Node("hi")
    assert our_node.data == "hi"
    assert our_node.next is None


def test_get_data():
    our_node = Node("test node")
    assert our_node.get_data() is "test node"


def test_set_next():
    our_first_node = Node("first")
    our_second_node = Node("second")
    our_second_node.set_next(our_first_node)
    assert our_second_node.next is our_first_node


def test_get_next():
    our_first_node = Node("first")
    our_second_node = Node("second", our_first_node)
    assert our_second_node.get_next() is our_first_node


def test_stack_creation():
    our_stack = Stack()
    assert our_stack.head is None


def test_push():
    our_list = ["first", "second", "third", "fourth"]
    our_stack = Stack(our_list)

    our_stack.push("fifth")
    assert our_stack.head.get_data() is "fifth"


def test_pop_1():
    our_stack = Stack()
    with pytest.raises(IndexError):
        our_stack.pop()


def test_pop_2():
    our_list = ["first", "second", "third", "fourth"]
    our_stack = Stack(our_list)
    assert our_stack.pop() == "fourth"
