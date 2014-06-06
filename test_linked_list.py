import pytest
from linked_list import Node, LinkedList

def test_node_constructor():
    a = Node(u'a')
    b = Node(u'b')
    assert a.data == u'a'
    assert a.next is None

def test_node_set_next():
    a = Node(u'a')
    b = Node(u'b')
    a.set_next(b)
    assert a.next is b
    assert a.next.data == b.data

def test_node_get_next():
    a = Node(u'a')
    b = Node(u'b', a)
    assert a.get_next() is None
    assert b.get_next() is a

def test_node_get_data():
    a = Node(u'a')
    b = Node(u'b', a)
    assert a.get_data() == u'a'
    assert b.get_data() == u'b'

def test_list_constructor():
    a = LinkedList()
    assert a.size == 0
    assert a.head == None
    a = LinkedList(*[1,2,3,4,5])
    assert a.size == 5
    assert a.head.get_data() == 5

def test_list_iterable():
    a = LinkedList(1,2,3,4,5)
    b = [1,2,3,4,5]
    for x in a:
        assert b[x.get_data()-1] == x.get_data()

def test_list_insert():
    llist = LinkedList()
    llist.insert(u'e')
    llist.insert(u'd')
    llist.insert(u'c')
    llist.insert(u'b')
    llist.insert(u'a')
    assert llist.size == 5
    assert llist.head.get_data() == u'a'
    assert llist.head.get_next().get_data() == u'b'

def test_list_pop():
    llist = LinkedList(*[1,2,3,4,5])
    assert llist.pop() == 5
    assert llist.size == 4
    llist.pop()     # pop 4
    llist.pop()     # pop 3
    assert llist.head.get_data() == 2
    assert llist.size == 2

def test_list_search():
    llist = LinkedList(*[1,2,3,4,5])
    assert llist.search(6) is None
    assert llist.search(5).get_next().get_data() == 4
    assert llist.search(1).get_next() is None

def test_list_remove():
    llist = LinkedList(*[1,2,3,4,5])
    assert llist.remove(3).get_next() is None
    assert llist.search(4).get_next() is llist.search(2)
    llist.remove(1)
    assert llist.search(2).get_next() is None
    assert llist.size == 3

def test_list_toString():
    llist = LinkedList(*[u'a',u'b',u'c',u'd',u'e'])
    assert llist.toString() == "('e', 'd', 'c', 'b', 'a')"
    llist = LinkedList(*[1,2,3,4,5])
    assert llist.toString() == "('5', '4', '3', '2', '1')"
