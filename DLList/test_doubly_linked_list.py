import pytest
from doubly_linked_list import Node, List
import sys


def test_node():
    our_node = Node("first")
    assert our_node.data == "first"
    assert our_node.next is None
    assert our_node.last is None


def test_list_creation():
    our_list = List()
    assert our_list.head is None
    assert our_list.tail is None


def test_insert():
    our_list = List()
    our_list.insert("first")

    assert our_list.head.data == "first"
    assert our_list.tail.data == "first"

    our_list.insert("second")
    our_list.insert("third")

    assert our_list.head.data == "third"
    assert our_list.tail.data == "first"

    assert our_list.head.next.data == "second"
    assert our_list.tail.last.data == "second"
    assert our_list.head.next.last.data == "third"
    assert our_list.tail.next is None


def test_append():
    our_list = List()
    our_list.append("first")

    assert our_list.tail.data == "first"
    assert our_list.head.data == "first"

    our_list.append("second")
    our_list.append("third")

    assert our_list.tail.data == "third"
    assert our_list.head.data == "first"

    assert our_list.tail.last.data == "second"
    assert our_list.head.next.data == "second"
    assert our_list.tail.last.last.data == "first"
    assert our_list.head.last is None


def test_pop():
    our_list = List()
    our_list.insert("first")
    our_list.insert("second")
    our_list.append("third")

    assert our_list.pop() == "second"

    assert our_list.head.data == "first"
    assert our_list.tail.data == "third"


def test_shift():
    our_list = List()
    our_list.insert("first")
    our_list.insert("second")
    our_list.append("third")

    assert our_list.shift() == "third"

    assert our_list.head.data == "second"
    assert our_list.tail.data == "first"


def test_remove(capsys):
    our_list = List()
    our_list.insert("first")
    our_list.insert("second")
    our_list.insert("third")

    assert our_list.head.next.data == "second"
    assert our_list.tail.last.data == "second"

    our_list.remove("second")

    assert our_list.head.next.data == "first"
    assert our_list.tail.last.data == "third"

    with pytest.raises(IndexError):
        our_list.remove("second")
