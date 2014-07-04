class Node(object):

    def __init__(self, val):
        self._data = val
        self._left = None
        self._right = None
        self._level = None
        self._visited = False


class BST(object):

    def __init__(self):
        self._depth = 0
        self._size = 0
        self._root = None

    def insert(self, val):
        if not self._root:
            self._root = Node(val)
            self._root._level = 1
            self._depth = 1
        else:
            parent = self._root
            while True:
                if val == parent._data:
                    return
                if val < parent._data:
                    if not parent._left:
                        left = Node(val)
                        left._level = parent._level + 1
                        parent._left = left
                        if left._level > self._depth:
                            self._depth = left._level
                        break
                    else:
                        parent = parent._left
                else:
                    if not parent._right:
                        right = Node(val)
                        right._level = parent._level + 1
                        parent._right = right
                        if right._level > self._depth:
                            self._depth = right._level
                        break
                    else:
                        parent = parent._right
        self._size += 1

    def contains(self, val):
        parent = self._root
        while True:
            if parent is None:
                return False
            if val == parent._data:
                return True
            parent = parent._left if val < parent._data else parent._right
        return False

    def is_balanced(self, node):
        left = self.height(node._left) if node._left else node._level
        right = self.height(node._right) if node._right else node._level
        return right - left

    def height(self, node):
        if not node._left and not node._right:
            return node._level
        else:
            if node._left:
                return self.height(node._left)
            if node._right:
                return self.height(node._right)

    def lets_traverse(self, mynode):
        if mynode._left:
            self.lets_traverse(mynode._left)
        if mynode._right:
            self.lets_traverse(mynode._right)
        print mynode._data, self.is_balanced(mynode)

    def in_order(self, node):
        if node._left:
            for i in self.in_order(node._left):
                yield i
        yield node
        if node._right:
            for i in self.in_order(node._right):
                yield i

    def pre_order(self, node):
        yield node
        if node._left:
            for i in self.pre_order(node._left):
                yield i
        if node._right:
            for i in self.pre_order(node._right):
                yield i

    def post_order(self, node):
        if node._left:
            for i in self.post_order(node._left):
                yield i
        if node._right:
            for i in self.post_order(node._right):
                yield i
        yield node

    def level_order(self, node):
        q = []
        q.insert(0, node)
        while q:
            node = q.pop()
            yield node
            if node._left:
                q.insert(0, node._left)
            if node._right:
                q.insert(0, node._right)


if __name__ == "__main__":
    # b = BST()

    # b.insert(10)
    # b.insert(5)
    # b.insert(15)
    # b.insert(3)
    # b.insert(2)
    # b.insert(1)

    # p = b._root
    # b.lets_traverse(p)

    b = BST()
    our_list = [4, 2, 6, 1, 3, 7, 5]
    for num in our_list:
        b.insert(num)
    for num in b.level_order(b._root):
        print num._data
