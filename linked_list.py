class Node(object):
    def __init__(self, data, node = None):
        self.data = data
        self.next = node

    def set_next(self, node):
        self.next = node

    def get_next(self):
        return self.next

    def get_data(self):
        return self.data


class LinkedList(object):
    def __init__(self, *data):
        self.size = 0
        self.head = None
        for val in data:
            self.insert(val)

    def insert(self, val):
        a = Node(val, self.head)
        self.head = a
        self.size += 1

    def pop(self):
        a = self.head
        if a is None:
            raise IndexError
        self.head = a.get_next()
        self.size -= 1
        return a.get_data()

    def size(self):
        return self.size

    def search(self, val):
        a = self.head
        while a is not None:
            if a.get_data() == val:
                return a.get_data()
            a = a.get_next()
        return None

    def remove(self, val):
        a = self.head
        while a.get_next() is not None:
            if a.get_next().get_data() == val:
                remove_node = a.get_next()
                b = remove_node.get_next()
                remove_node.set_next(None)
                a.set_next(b)
                return

    def print_me(self):
        a = self.head
        result = "("
        while a.next is not None:
            result = result + "'" + a.data + "',"
            a = a.next
        print result + "'" + a.data + "')"
