import pytest
from stack import Node, Stack


def test_node():
    our_node = Node("first")
    assert our_node.data == "first"
    assert our_node.next is None

    our_other_node = Node("second", our_node)
    assert our_other_node.next is our_node


def test_stack_creation():
    our_stack = Stack()
    assert our_stack.head is None


def test_push_1():
    our_list = ["first", "second", "third", "fourth"]
    our_stack = Stack(our_list)

    our_stack.push("fifth")
    assert our_stack.head.data is "fifth"


def test_push_2():
    our_stack = Stack()
    our_stack.push("first")

    assert our_stack.head.data is "first"


def test_pop_1():
    our_stack = Stack()
    with pytest.raises(IndexError):
        our_stack.pop()


def test_pop_2():
    our_list = ["first", "second", "third", "fourth"]
    our_stack = Stack(our_list)
    assert our_stack.pop() == "fourth"
