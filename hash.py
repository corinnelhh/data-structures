

class HashTable(object):

    def __init__(self, n=128):
        self.hashed = [[] for i in range(n)]
        self.mask_size = n - 1

    def hash(self, item):
        if isinstance(item, basestring):
            hashed_item = []
            for el in item:
                hashed_item.append(ord(el))
        else:
            raise TypeError
        return self.mask_size & sum(hashed_item)

    def get(self, item):
        key = self.hash(item)
        for el in self.hashed[key]:
            if el == item:
                print "we found it!"
                return el
        else:
            raise IndexError

    def set(self, item):
        key = self.hash(item)
        print key
        self.hashed[key].append(item)
        print self.hashed[key]


if __name__ == "__main__":
    our_hash = HashTable()
    our_hash.set("alice")
    our_hash.set("elica")
    print our_hash.get("elica")
    print our_hash.get("muazzez")
