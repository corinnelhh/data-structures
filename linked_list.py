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
            current_node = current_node.get_next()

    def insert(self, val):
        new_node = Node(val, self.head)
        self.head = new_node
        self.size += 1

    def pop(self):
        old_node = self.head
        if old_node is None:
            raise IndexError
        self.head = old_node.get_next()
        self.size -= 1
        old_node.set_next(None)
        return old_node.get_data()

    def search(self, val):
        node = self.head
        while node is not None:
            if node.get_data() == val:
                return node
            node = node.get_next()
        return None

    def remove(self, val):
        first = self.head
        # removing the head of the linked list
        if first.get_data() == val:
            self.pop()
            return first
        # if first node is wrong, look for the right one and remove
        while first.get_next() is not None:
            if first.get_next().get_data() == val:
                remove_node = first.get_next()
                second = remove_node.get_next()
                remove_node.set_next(None)
                first.set_next(second)
                self.size -= 1
                return remove_node
            first = first.get_next()
        if first.get_next() is None:
            raise IndexError

    def toString(self):
        node = self.head
        result = "("
        while node.get_next() is not None:
            val = node.get_data()
            if type(val) == type(u'hello'):
                result = result + "'" + str(val) + "', "
            else:
                result = result + "" + str(val) + ", "
            node = node.get_next()
        if type(node.get_data()) == type(u'hello'):
            return result + "'" + str(node.get_data()) + "')"
        else:
            return result + "" + str(node.get_data()) + ")"
