#!/usr/bin/env python
import math
import sys


class BinaryHeap(object):
    """
    min_heap and max_heap implementations with lists
    class takes do_max input
        do_max == True : if it is a max_heap
        do_max == False : if it is a min_heap
    Time Complexity : O(logn)
    No extra space is used
    """

    def __init__(self, do_max=True):
        self._list = []
        self._do_max = do_max

    def push(self, value):
        self._list.append(value)
        tmp_index = self._list.index(value)
        return self._max_traverse_push(tmp_index, value) \
            if self._do_max else self._min_traverse_push(tmp_index, value)

    def pop(self):
        if not len(self._list):
            return
        if len(self._list) == 1:
            self._list.pop()
            return
        self._list[0] = self._list[-1]
        self._list.pop()

        height = int(math.log(len(self._list), 2))
        return self._max_traverse_pop(height, 0) \
            if self._do_max else self._min_traverse_pop(height, 0)

    def _max_traverse_push(self, tmp_index, value):
        cur_index = tmp_index
        while tmp_index:
            tmp_index = (tmp_index - 1) // 2
            if (self._list[tmp_index] >= value):
                break
            self._list[tmp_index], self._list[cur_index] = \
                self._list[cur_index], self._list[tmp_index]
            cur_index = tmp_index

    def _min_traverse_push(self, tmp_index, value):
        cur_index = tmp_index
        while tmp_index:
            tmp_index = (tmp_index - 1) // 2
            if (self._list[tmp_index] <= value):
                break
            self._list[tmp_index], self._list[cur_index] = \
                self._list[cur_index], self._list[tmp_index]
            cur_index = tmp_index

    def _max_traverse_pop(self, height, parent_index):
        if (len(self._list) == 2):
            if (self._list[1] > self._list[0]):
                self._list[0] = self._list[1]
            return

        while height > 0:
            lchild = (parent_index * 2) + 1
            rchild = (parent_index * 2) + 2
            print lchild, rchild
            if (self._list[parent_index] > self._list[lchild] and
                    self._list[parent_index] > self._list[rchild]):
                break
            if self._list[lchild] > self._list[rchild]:
                self._list[parent_index] = self._list[lchild]
                parent_index = lchild
            else:
                self._list[parent_index] = self._list[rchild]
                parent_index = rchild
            height -= height
            print parent_index
            if ((parent_index * 2) + 2 == len(self._list) - 1):
                break

        if ((parent_index * 2) + 1 == len(self._list) - 1):
            if (self._list[(parent_index * 2) + 1] > self._list[parent_index]):
                self._list[parent_index] = self._list[(parent_index * 2) + 1]

    def _min_traverse_pop(self, height, parent_index):
        if (len(self._list) == 2):
            if (self._list[1] < self._list[0]):
                self._list[0] = self._list[1]
            return

        while height > 0:
            lchild = (parent_index * 2) + 1
            rchild = (parent_index * 2) + 2
            print lchild, rchild
            if (self._list[parent_index] < self._list[lchild] and
                    self._list[parent_index] < self._list[rchild]):
                break
            if self._list[lchild] < self._list[rchild]:
                self._list[parent_index] = self._list[lchild]
                parent_index = lchild
            else:
                self._list[parent_index] = self._list[rchild]
                parent_index = rchild
            height -= height
            print parent_index
            if ((parent_index * 2) + 2 == len(self._list) - 1):
                break

        if ((parent_index * 2) + 1 == len(self._list) - 1):
            if (self._list[(parent_index * 2) + 1] < self._list[parent_index]):
                self._list[parent_index] = self._list[(parent_index * 2) + 1]

if __name__ == '__main__':
    bh = BinaryHeap(sys.argv[1])
