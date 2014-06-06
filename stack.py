class Node(object):
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

    def get_data(self):
        return self.data

    def set_next(self, next_node):
        self.next = next_node

    def get_next(self):
        return self.next


class Stack(object):
    def __init__(self, data=None):
        self.head = None
        if data:
            for val in data:
                self.push(val)

    def push(self, data):
        a = Node(data, self.head)
        self.head = a

    def pop(self):
        if self.head is None:
            raise IndexError
        our_returned_value = self.head.get_data()
        self.head.set_next(None)
        self.head = self.head.get_next()
        return our_returned_value
