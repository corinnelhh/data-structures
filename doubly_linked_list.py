class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.last = None


class List(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        self.last_node = self.head
        self.head = Node(data)
        self.head.next = self.last_node
        if self.last_node:
            self.last_node.last = self.head
        if self.tail is None:
            self.tail = self.head

    def append(self, data):
        self.next_node = self.tail
        self.tail = Node(data)
        self.tail.last = self.next_node
        if self.next_node:
            self.next_node.next = self.tail
        if self.head is None:
            self.head = self.tail

    def pop(self):
        if self.head is None:
            print "Sorry, the queue is empty!"
            raise IndexError
        our_returned_value = self.head.data
        self.head = self.head.next
        return our_returned_value

    def shift(self):
        if self.tail is None:
            print "Sorry, the queue is empty!"
            raise IndexError
        our_returned_value = self.tail.data
        self.tail = self.tail.last
        return our_returned_value

    def remove(self, val):
        a = self.head
        while a is not None:
            if a.data == val:
                if a == self.head:
                    a.next.last = None
                else:
                    a.next.last = a.last
                    a.last.next = a.next
            a = a.next
