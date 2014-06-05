import pytest
from linked_list import Node, List


def test_node_1():
    a = Node("hello")
    assert a.data == "hello"


def test_node_2():
    a = Node("one")
    b = Node("two")
    c = Node("three")
    a.next = b
    b.next = c
    assert a.next is b
    assert b.data == a.next.data
    assert c.data == a.next.next.data


def test_insert_1():
    a = List()
    assert a.head is None
    assert a.size == 0


def test_insert_2():
    linked = List()
    a = Node("first")
    b = Node("second")

    linked.insert(a)

    assert linked.head is a
    assert linked.size == 1

    linked.insert(b)

    assert linked.head is not a
    assert linked.head is b
    assert linked.size == 2
    assert linked.head.next.data == a.data
    assert a.next is None


def test_pop():
    linked = List()
    a = Node("one")
    b = Node("two")

    linked.insert(a)
    linked.insert(b)

    assert linked.pop() == b.data

    assert linked.head is not b
    assert linked.head is a
    assert linked.size == 1


def test_search():
    linked = List()
    a = Node("one")
    b = Node("two")

    linked.insert(a)
    linked.insert(b)

    assert linked.search("one") is a
    assert linked.search("two") is b
    assert linked.search("happy") is None
    assert linked.size == 2


def test_remove():
    linked = List()
    a = Node("one")
    b = Node("two")
    c = Node("three")
    d = Node("four")
    e = Node("five")

    linked.insert(a)
    linked.insert(b)
    linked.insert(c)
    linked.insert(d)
    linked.insert(e)

    linked.remove(c)

    assert linked.size == 4
    assert d.next is b
    assert c.next is None


def test_print_me(capfd):
    linked = List()
    a = Node("one")
    b = Node("two")

    linked.insert(a)
    linked.insert(b)

    linked.print_me()

    out, err = capfd.readouterr()

    assert out == "('two','one')\n"
