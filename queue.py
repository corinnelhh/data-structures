class Node(object):
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node
        self.last = None


class Queue(object):
    def __init__(self, data=None):
        self.head = None
        self.tail = None
        self.size = 0
        if data:
            for val in data:
                self.enqueue(val)

    def enqueue(self, data):
        self.last_node = self.head
        self.head = Node(data, self.head)
        if self.last_node:
            self.last_node.last = self.head
        if self.tail is None:
            self.tail = self.head
        self.size += 1

    def dequeue(self):
        if self.tail is None:
            print "Sorry, the queue is empty!"
            raise IndexError
        our_returned_value = self.tail.data
        self.tail = self.tail.last
        self.size -= 1
        return our_returned_value

    def size_me(self):
        return self.size
