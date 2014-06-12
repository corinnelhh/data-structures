#!/usr/bin/env python
import math, random

class BinaryHeap(object) :
    def __init__ (self, max=1, *data):
        self._list = []
        self._size = 0
        self.max = max
        if data:
            for i in data:
                self.push(i)

    def push(self, value):
        self._list.append(value)
        child = parent = self._size
        self._size += 1
        while parent > 0:
            parent = (child-1)//2
            if self.compare(child, parent):
                break
            self.swap(child, parent)
            child = parent


    def pop(self) :
        if not self._size:
            print "Yo, this is an empty heap."
            raise IndexError

        val = self._list[0]
        self._list[0] = self._list[-1]
        self._list.pop()
        self._size -= 1
        parent, left, right = 0, 1, 2

        while right < self._size:
            if (self.compare(left, parent) and
                self.compare(right, parent)):
                break

            if self.compare(right, left):
                self.swap(parent, left)
                parent = left

            else:
                self.swap(parent, right)
                parent = right

            left = parent*2 + 1
            right = left + 1

        if left < self._size:
            if self.compare(parent, left):
                self.swap(parent, left)

        return val


    def swap(self, x, y):
        self._list[x], self._list[y] = self._list[y], self._list[x]

    def compare(self, x, y):
        if self.max:
            return self._list[x] < self._list[y]
        else:
            return self._list[x] > self._list[y]


"""
        #DEBUGGING
for x in range(10):
    a = BinaryHeap(1,*[random.randint(0,100) for i in range(11)])
    print str(a._list)
"""










