class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue(object):
    def __init__(self, *data):
        self.size = 0
        self.head = None
        self.tail = None
        if data:
            for i in data:
                self.enqueue(i)

    def enqueue(self, val):
        if self.size == 0:
            new_node = Node(val)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(val)
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def dequeue(self):
        if self.size <= 0:
            raise IndexError
        return_node = self.head
        self.head = self.head.next
        return_node.next = None
        self.size -= 1
        return return_node.data

    def __size__(self):
        return self.size