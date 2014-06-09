class Node(object):
    def __init__(self, data, node = None):
        self.data = data
        self.next = node

class LinkedList(object):
    def __init__(self, *data):
        self.size = 0
        self.head = None
        # populate the LinkedList if an iterable is detected
        if data:
            for val in data:
                self.insert(val)

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next

    def insert(self, val):
        new_node = Node(val, self.head)
        self.head = new_node
        self.size += 1

    def pop(self):
        old_node = self.head
        if old_node is None:
            raise IndexError
        self.head = old_node.next
        self.size -= 1
        old_node.next = None
        return old_node.data

    def search(self, val):
        node = self.head
        while node is not None:
            if node.data == val:
                return node
            node = node.next
        return None

    def remove(self, val):
        first = self.head
        # removing the head of the linked list
        if first.data == val:
            self.pop()
            return first
        # if first node is wrong, look for the right one and remove
        while first.next is not None:
            if first.next.data == val:
                remove_node = first.next
                second = remove_node.next
                remove_node.next = None
                first.next = second
                self.size -= 1
                return remove_node
            first = first.next
        if first.next is None:
            raise IndexError

    def toString(self):
        node = self.head
        result = "("
        while node.next is not None:
            val = node.data
            if type(val) == type(u'hello'):
                result = result + "'" + str(val) + "', "
            else:
                result = result + "" + str(val) + ", "
            node = node.next
        if type(node.data) == type(u'hello'):
            return result + "'" + str(node.data) + "')"
        else:
            return result + "" + str(node.data) + ")"
