class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue(object):
    def __init__(self, *data):
        self._size = 0
        self.head = None
        self.tail = None
        if data:
            for i in data:
                self.enqueue(i)

    def enqueue(self, val):
        if self._size == 0:
            self.tail = self.head = Node(val)
        else:
            self.tail.next = self.tail = Node(val)
        self._size += 1

    def dequeue(self):
        if self.size <= 0:
            raise IndexError
    #    return_node = self.head
    #    self.head = self.head.next
    #    return_node.next = None
        return_node, self.head, return_node.next = self.head, self.head.next, None
        self._size -= 1
        return return_node.data

    def size(self):
        return self._size