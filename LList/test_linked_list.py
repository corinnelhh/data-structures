import pytest
from linked_list import Node, LinkedList

def test_node_constructor():
    a = Node(u'a')
    b = Node(u'b')
    assert a.data == u'a'
    assert a.next is None

def test_list_constructor():
    a = LinkedList()
    assert a.size == 0
    assert a.head == None
    a = LinkedList(*[1,2,3,4,5])
    assert a.size == 5
    assert a.head.data == 5

def test_list_iterable():
    a = LinkedList(1,2,3,4,5)
    b = [1,2,3,4,5]
    for x in a:
        assert b[x.data-1] == x.data

def test_list_insert():
    llist = LinkedList()
    llist.insert(u'e')
    llist.insert(u'd')
    llist.insert(u'c')
    llist.insert(u'b')
    llist.insert(u'a')
    assert llist.size == 5
    assert llist.head.data == u'a'
    assert llist.head.next.data == u'b'

def test_list_pop():
    llist = LinkedList(*[1,2,3,4,5])
    assert llist.pop() == 5
    assert llist.size == 4
    llist.pop()     # pop 4
    llist.pop()     # pop 3
    assert llist.head.data == 2
    assert llist.size == 2

def test_list_search():
    llist = LinkedList(*[1,2,3,4,5])
    assert llist.search(6) is None
    assert llist.search(5).next.data == 4
    assert llist.search(1).next is None

def test_list_remove():
    llist = LinkedList(*[1,2,3,4,5])
    assert llist.remove(3).next is None
    assert llist.search(4).next is llist.search(2)
    llist.remove(1)
    assert llist.search(2).next is None
    assert llist.size == 3

def test_list_toString():
    llist = LinkedList(*[u'a',u'b',u'c',u'd',u'e'])
    assert llist.toString() == u'(\'e\', \'d\', \'c\', \'b\', \'a\')'
    llist = LinkedList(*[1,2,3,4,5])
    assert llist.toString() == u'(5, 4, 3, 2, 1)'
    llist = LinkedList(1,2,3,4,5,*(u'a',u'b',u'c',u'd',u'e'))
    assert llist.toString() == "('e', 'd', 'c', 'b', 'a', 5, 4, 3, 2, 1)"
