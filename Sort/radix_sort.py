def radix_sort(iterable):
    bit = 10
    size = pow(2, bit)
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
    i = 0
    while i < len(res)-1:
        assert res[i] <= res[i+1]
        i += 1
    return res

if __name__ == "__main__":
    import random
    a = [random.randint(10,999999) for i in xrange(1000000)]
    import time
    start = time.clock()
    x = radix_sort(a)
    end = time.clock()
    print "Radix with size 128: %.2gs" % (end-start)

    print "Iteration: ", c, len(a), c/len(a)
    # count = 0
    # for i in a:
    #     count +=1
    #     print i,
    #     if count % 15 == 0:
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