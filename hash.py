

class HashTable(object):

    def __init__(self, n=128):
        self.hashed = [[] for i in range(n)]
        self.mask_size = n - 1

    def hash(self, item):
        if isinstance(item, basestring):
            hashed_item = []
            for el in item:
                hashed_item.append(ord(el))
            total = sum(hashed_item)
        else:
            raise TypeError
        return self.mask_size & total

    def get(self, item):
        pass

    def set(self, item):
        key = self.hash(item)
        self.hashed.insert([key], item)


if __name__ == "__main__":
    our_hash = HashTable()
    print our_hash.hash("peach")
