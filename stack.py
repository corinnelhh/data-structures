class Node(object):
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class Stack(object):
    def __init__(self, data=None):
        self.head = None
        if data:
            for val in data:
                self.push(val)

    def push(self, data):
        self.head = Node(data, self.head)

    def pop(self):
        if self.head is None:
            raise IndexError
        our_returned_value = self.head.data
        self.head.next = None
        self.head = self.head.next
        return our_returned_value
