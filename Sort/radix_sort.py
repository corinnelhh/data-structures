def radix_sort(iterable):
    bit = 10
    size = 1 << bit
    mask = size - 1
    cache = [[] for i in range(size)]
    # count = 0
    for i in iterable:
        cache[i&mask].append(i)
        # count += 1
    num = max([j for i in cache for j in i])
    ran = 1
    while num > (size << (bit * (ran - 1))):
        mask = mask << bit
        tmp = [[] for i in range(size)]
        for i in cache:
            for j in i:
                tmp[(j & mask) >> (bit * ran)].append(j)
                # count += 1
        cache = tmp[:]
        ran += 1
    res = []
    for i in cache:
        for j in i:
            res.append(j)
    # i = 0
    # while i < len(res)-1:
    #     assert res[i] <= res[i+1]
    #     i += 1
    return res


def radix_string(iterable):
    size = 1024
    cache = [[] for i in range(size)]
    length = 1
    for word in iterable:
        cache[_index(word, 1)].append(word)
        if len(word) > length:
            length = len(word)
    length = (length-1) >> 1
    for i in range(length):
        tmp = [[] for k in range(size)]
        for bucket in cache:
            for word in bucket:
                tmp[_index(word, i+2)].append(word)
        cache = tmp[:]
    res = []
    for i in cache:
        for j in i:
            res.append(j)
    i = 0
    while i < len(res)-1:
        assert len(res[i]) <= len(res[i+1])
        if len(res[i]) == len(res[i+1]):
            assert (ord(res[i][0]) & 31) <= (ord(res[i+1][0]) & 31)
        i += 1
    return res


def _index(word, i):
    x = len(word)
    if (x + 1)  >> 1 < i :
        return 0
    else:
        letter = ~((i-1)<<1)
        index = (ord(word[letter]) & 31)
        if x >= i << 1:
            ind = ord(word[letter-1]) & 31
            index = (ind << 5) | index
        return index


if __name__ == "__main__":
    import random, string
    a = []
    for i in xrange(1000000):
        length = random.randint(1, 100)
        word = ''.join(random.choice(string.ascii_letters) for x in range(length))
        a.append(word)


    # a = [random.randint(10,999999) for i in xrange(1000000)]
    import time
    start = time.clock()
    x = radix_string(a)
    end = time.clock()
    print "Radix with size 1024: %.3gs" % (end-start)
    #print x

    # print "Iteration: ", c, len(a), c/len(a)
    # count = 0
    # for i in x:
    #     count +=1
    #     print i,
    #     if count % 3 == 0:
    #         print


# Size: 10 million
# Cache Size: 4096
# Time: 12s

# Size: 10 million
# Cache Size: 128
# Time: 14s

# Size: 10 million
# Cache Size: 1024
# Iteration Count: 20 million   O(2n)

# Size: 1 million
# Cache Size: 1024
# Time: 1s

# String: word length - 100
# Size: 1 million
# Cache Size: 1024
# Time: 53.9s

# String: word length - 100
# Size: 1 million
# Cache Size: 32
# Time: 55.7s
