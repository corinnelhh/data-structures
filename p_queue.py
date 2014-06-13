#!/usr/bin/env python
import random
#import copy

class Node(object):
    def __init__(self, data, p, o=0):
        self._priority = p
        self._order = o
        self._data = data

class P_Queue(object):
    def __init__(self):
        self._list = []
        self._counter = 0
        self._size = 0

    def insert(self, data=None, p=0):
        new_node = Node(data, p, self._counter)
        self._counter += 1
        self._list.append(new_node)
        child = parent = self._size
        self._size += 1
        while parent > 0:
            parent = (child-1)//2
            if self._compare(child, parent):
                break
            self._swap(child, parent)
            child = parent

    def pop(self):
        if not self._size:
            raise IndexError("This is an empty Queue, yo.")

        val = self._list[0]
        self._list[0] = self._list[-1]
        self._list.pop()
        self._size -= 1
        parent, left, right = 0, 1, 2

        while right < self._size:
            if (self._compare(left, parent) and
                self._compare(right, parent)):
                break

            if self._compare(right, left):
                self._swap(parent, left)
                parent = left

            else:
                self._swap(parent, right)
                parent = right

            left = parent*2 + 1
            right = left + 1

        if left < self._size:
            if self._compare(parent, left):
                self._swap(parent, left)

        return val

    def peek(self):
        return self._list[0]

    def _swap(self, x, y):
        self._list[x], self._list[y] = self._list[y], self._list[x]


    def _compare(self, x, y):
        if self._list[x]._priority < self._list[y]._priority:
            return True
        elif self._list[x]._priority == self._list[y]._priority:
            return True if self._list[x]._order > self._list[y]._order else False
        else:
            return False

"""
    def __iter__(self):
        b = copy.deepcopy(self)
        current_node = self._list[0]
        b.pop()
        for i in range(self._size - 1):
            yield current_node
            current_node = b.pop()
"""

"""
        #DEBUGGING
a = P_Queue()
for i in range(10):
    val = random.randint(0,100)
    pri = random.randint(0,5)
    a.insert(val, pri)
for i in range(a._size):
    print "{}\t{}\t{}".format(a._list[i]._data,
        a._list[i]._priority,
        a._list[i]._order)

print max(min(a._list, a._list[0]._order),a._list[0]._priority)
print "\n"

for i in range(a._size):
    b = a.pop()
    print str(b._data) + "\tp: " + str(b._priority) + "\to: " + str(b._order)
print "\n"
"""





