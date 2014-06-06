class Node(object):
    def __init__(self, data, node = None):
        self.data = data
        self.next = node

    def set_next(self, node = None):
        self.next = node

    def get_next(self):
        return self.next

    def get_data(self):
        return self.data

class LinkedList(object):
    def __init__(self, data = None):
        self.size = 0
        self.head = None
        # populate the LinkedList if an iterable is detected
        if data:
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
        a.set_next(None)
        return a.get_data()

    def search(self, val):
        a = self.head
        while a is not None:
            if a.get_data() == val:
                return a
            a = a.get_next()
        return None

    def remove(self, val):
        a = self.head
        # removing the head of the linked list
        if a.get_data() == val:
            self.pop()
            return a
        # if first node is wrong, look for the right one and remove
        while a.get_next() is not None:
            if a.get_next().get_data() == val:
                remove_node = a.get_next()
                b = remove_node.get_next()
                remove_node.set_next(None)
                a.set_next(b)
                self.size -= 1
                return remove_node
            a = a.get_next()
        if a.get_next() is None:
            raise IndexError

    def toString(self):
        a = self.head
        result = "("
        while a.get_next() is not None:
            result = result + "'" + str(a.get_data()) + "', "
            a = a.get_next()
        return result + "'" + str(a.data) + "')"
