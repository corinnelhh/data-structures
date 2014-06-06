import pytest
from linked_list import Node, List


@pytest.fixture(scope="function")
def iterate_nodes():
    a = Node("one")
    b = Node("two")
    c = Node("three")
    d = Node("four")
    e = Node("five")
    return a, b, c, d, e


@pytest.fixture(scope="function")
def create_populated_list(iterate_nodes):
    a, b, c, d, e = iterate_nodes
    our_list = List()

    our_list.insert(a)
    our_list.insert(b)
    our_list.insert(c)
    our_list.insert(d)
    our_list.insert(e)

    return our_list


def test_node_1():
    a = Node("hello")
    assert a.data == "hello"


def test_node_2(iterate_nodes):
    a, b, c, d, e = iterate_nodes
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


def test_pop(iterate_nodes, create_populated_list):
    a, b, c, d, e = iterate_nodes
    linked = create_populated_list

    assert linked.pop() == e.data

    assert linked.head is not e
    assert linked.head is d
    assert linked.size == 4


def test_search(iterate_nodes, create_populated_list):
    a, b, c, d, e = iterate_nodes
    linked = create_populated_list

    assert linked.search("one") is a
    assert linked.search("two") is b
    assert linked.search("happy") is None
    assert linked.size == 5


def test_remove(iterate_nodes, create_populated_list):
    a, b, c, d, e = iterate_nodes
    linked = create_populated_list

    linked.remove(c)

    assert linked.size == 4
    assert d.next is b
    assert c.next is None


def test_print_me(capfd, iterate_nodes, create_populated_list):
    a, b, c, d, e = iterate_nodes
    linked = create_populated_list

    linked.print_me()

    out, err = capfd.readouterr()

    assert out == "('five','four','three','two','one')\n"
