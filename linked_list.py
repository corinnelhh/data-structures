class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class List(object):
    def __init__(self):
        self.size = 0
        self.head = None

    def insert(self, val):
        a = Node(val)
        a.data = val
        val.next = self.head
        self.head = val
        self.size += 1

    def pop(self):
        a = self.head
        self.head = a.next
        self.size -= 1
        return a.data

    def size(self):
        return self.size

    def search(self, val):
        a = self.head
        while a is not None:
            if a.data == val:
                return a
            a = a.next
        return None

    def remove(self, node):
        a = self.head
        while a is not None:
            if a.next is node:
                a.next = node.next
                node.next = None
                self.size -= 1
            a = a.next

    def print_me(self):
        a = self.head
        result = "("
        while a.next is not None:
            result = result + "'" + a.data + "',"
            a = a.next
        print result + "'" + a.data + "')"
