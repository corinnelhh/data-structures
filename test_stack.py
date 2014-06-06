import pytest
from stack import Node, Stack


def test_node():
    our_node = Node("hi")
    assert our_node.data == "hi"
    assert our_node.next is None


def test_get_data():
    our_node = Node("test node")
    assert our_node.data is "test node"


def test_set_next():
    our_node = Node("test node")
    assert our_node.next is None


#def test_get_next():

def stack_creation():
    our_stack = Stack()


#def test_stack():



#def test_push():

#def test_pop():
