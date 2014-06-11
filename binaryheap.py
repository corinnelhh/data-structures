#!/usr/bin/env python
import math

class BinaryHeap(object) :
    def __init__ (self, do_max=1):
        self._list = []
        self._do_max = do_max

    def push(self, value):
        self._list.append(value)
        cur_index = tmp_index = self._list.index(value)
        while tmp_index :
            tmp_index = (tmp_index-1)//2
            if (self._list[tmp_index] >= value):
                break
            self._list[tmp_index], self._list[cur_index] = self._list[cur_index], self._list[tmp_index]
            cur_index = tmp_index
    def pop(self) :
        # test if is empty
        self._list[0] = self._list.pop()
        parent_index = 0
        height = int(math.log(len(self._list), 2))
        while height >0 :
            lchild = (parent_index*2)+1
            rchild = (parent_index*2)+2
            if (self._list[parent_index] > self._list[lchild] and
                self._list[parent_index] > self._list[rchild]):
                break
            if self._list[lchild] > self._list[rchild]:
                self._list[parent_index] = self._list[lchild]
                parent_index = lchild
            else :
                self._list[parent_index] = self._list[rchild]
                parent_index = rchild
            height -= height
            if ((parent_index*2)+2 < len(self._list)-1):
                break
        lchild = parent_index*2 + 1
        rchild = parent_index*2 + 2
        if (rchild == len(self._list)-1):
            if self._list[lchild] < self._list[rchild]:
                self._list[parent_index], self._list[rchild] = self._list[rchild], self._list[parent_node]
            else:

            if (self._list[parent_index] < self._list[(parent_index*2)+2]) :














