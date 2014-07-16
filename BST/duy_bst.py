class BST(object):

    def __init__(self):
        self._dict = {}
        self._root = None
        self._size = 0

    def _left(self, val):
        return self._dict[val][0]

    def _right(self, val):
        return self._dict[val][1]

    def _parent(self, val):
        return self._dict[val][2]

    def _set_left(self, parent, val):
        if parent:
            self._dict[parent][0] = val
        if val:
            self._dict[val][2] = parent

    def _set_right(self, parent, val):
        if parent:
            self._dict[parent][1] = val
        if val:
            self._dict[val][2] = parent

    def _height(self, val):
        if val in self._dict:
            if not self._left(val) and not self._right(val):
                return 1
            lh = 1 + self._height(self._left(val))
            rh = 1 + self._height(self._right(val))
            return lh if lh > rh else rh
        else:
            return 0

    def insert(self, val):
        if val in self._dict:
            pass
        self._dict[val] = [None, None, None]
        if not self._root:
            self._root = val
        else:
            tmp = self._root
            while True:
                if val < tmp:
                    if self._left(tmp) is None:
                        self._set_left(tmp, val)
                        break
                    tmp = self._left(tmp)
                else:
                    if self._right(tmp) is None:
                        self._set_right(tmp, val)
                        break
                    tmp = self._right(tmp)
        self._size += 1

    def delete_node(self, val):
        if val not in self._dict:
            raise IndexError
        if not self._left(val) and not self._right(val):
            if self._size == 1:
                self._root = None
            elif self._right(self._parent(val)) == val:
                self._set_right(self._parent(val), None)
            else:
                self._set_left(self._parent(val), None)
        else:
            side = self.balance(val)
            bottom = val
            if side > 0:
                bottom = self._get_bottom(self._right(val), side)
            else:
                bottom = self._get_bottom(self._left(val), side)
            if self._root == val:
                self._root = bottom
                self._swap_root(side, val, bottom)
                self._dict[bottom][2] = None
            else:
                self._swap(self._parent(val), val, bottom)
            self._swap_val(bottom, val)
        self._dict.pop(val)
        self._size -= 1

    def _swap_root(self, side, val, bottom):
        if side > 0:
            if self._parent(bottom) != val:
                self._set_left(self._parent(bottom), self._right(bottom))
        else:
            if self._parent(bottom) != val:
                self._set_right(self._parent(bottom), self._left(bottom))

    def _swap(self, parent, val, bottom):
        if self._left(parent) == val:
            if self._parent(bottom) != val:
                self._set_right(self._parent(bottom), self._left(bottom))
            self._set_left(parent, bottom)
        else:
            if self._parent(bottom) != val:
                self._set_left(self._parent(bottom), self._right(bottom))
            self._set_right(parent, bottom)

    def _swap_val(self, bottom, val):
        if bottom != self._left(val):
            self._set_left(bottom, self._left(val))
        if bottom != self._right(val):
            self._set_right(bottom, self._right(val))

    def _get_bottom(self, val, side):
        tmp = val
        if side > 0:
            while True:
                if self._left(tmp) is None:
                    return tmp
                tmp = self._left(tmp)
        else:
            while True:
                if self._right(tmp) is None:
                    return tmp
                tmp = self._right(tmp)

    def balance(self, val):
        lh = self._height(self._left(val))
        rh = self._height(self._right(val))
        return rh - lh

    def in_order(self, val):
        if self._left(val):
            for i in self.in_order(self._left(val)):
                yield i
        yield val
        if self._right(val):
            for i in self.in_order(self._right(val)):
                yield i

    def pre_order(self, val):
        yield val
        if self._left(val):
            for i in self.pre_order(self._left(val)):
                yield i
        if self._right(val):
            for i in self.pre_order(self._right(val)):
                yield i

    def post_order(self, val):
        if self._left(val):
            for i in self.post_order(self._left(val)):
                yield i
        if self._right(val):
            for i in self.post_order(self._right(val)):
                yield i
        yield val

    def level_order(self):
        tmp = {}
        for i in self._dict:
            tmp[i] = self.depth(i)
        sort_tmp = sorted(tmp.items(), key=lambda x: (x[1], x[0]))
        for i in sort_tmp:
            yield i[0]

    def size(self):
        return self._size

    def depth(self, val):
        tmp = self._root
        d = 1
        while True:
            if val < tmp:
                tmp = self._left(tmp)
            elif val > tmp:
                tmp = self._right(tmp)
            else:
                return d
            d += 1

if __name__ == "__main__":
    a = BST()
    b = [32, 16, 48, 8, 24, 40, 56, 11, 22, 33, 10, 55]

    for i in b:
        a.insert(i)

    for i in a._dict:
        res = str(i)+" "+str(a._dict[i])
        res += "\t\t"+str(a._height(i))+"\t"+str(a.balance(i))
        res += "\t"+str(a.depth(i))
        print res

    print "In Order:\t",
    for i in a.in_order(a._root):
        print i,

    print
    print "Pre Order:\t",
    for i in a.pre_order(a._root):
        print i,

    print
    print "Post Order:\t",
    for i in a.post_order(a._root):
        print i,

    print
    print "Level Order:\t",
    for i in a.level_order():
        print i,

    for x in b:
        a.delete_node(x)
        if a._size == 5:
            break
        print
        print "Level Order:\t",
        for i in a.level_order():
            print i,
        print
        # for i in a._dict:
        #     res = str(i)+" "+str(a._dict[i])
        #     res += "  \t"+str(a._height(i))+"\t"+str(a.balance(i))
        #     res += "\t"+str(a.depth(i))
        #     print res
