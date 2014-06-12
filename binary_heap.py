#!/usr/bin/env python
import math, random

class BinaryHeap(object) :
    def __init__ (self, *data):
        self._list = []
        self._size = 0
        if data:
            for i in data:
                self.push(i)

    def push(self, value):
        self._list.append(value)
        child = parent = self._size
        self._size += 1
        while parent > 0:
            parent = (child-1)//2
            if (self._list[child] < self._list[parent]):
                break
            self.swap(child, parent)
            child = parent


    def pop(self) :
        if not self._size:
            print "Yo, this is an empty heap."
            raise IndexError
        if self._size == 1 :
            self._size = 0
            return self._list.pop()
        val = self._list[0]
        self._list[0] = self._list[-1]
        self._list.pop()
        self._size -= 1
        parent, left, right = 0, 1, 2

        while right < self._size:
            if right >= self._size:
                if self._list[parent] < self._list[left]:
                    self.swap(parent, left)

            if (self._list[parent] > self._list[left] and
                self._list[parent] > self._list[right]):
                break
            if self._list[right] < self._list[left]:
                if self._list[parent] < self._list[left]:
                    self.swap(parent, left)
                parent = left

            else:
                if self._list[parent] < self._list[right]:
                    self.swap(parent, right)
                parent = right

            left = parent*2 + 1
            right = left + 1

        if left < self._size:
            if self._list[parent] < self._list[left]:
                self.swap(parent, left)

        return val


    def swap(self, x, y):
        self._list[x], self._list[y] = self._list[y], self._list[x]


"""
        #DEBUGGING
for x in range(50):
    a = BinaryHeap(*[random.randint(0,100) for i in range(11)])
    print str(a._list)

"""









