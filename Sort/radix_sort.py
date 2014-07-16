def radix_sort(iterable):
    bit = 7
    size = pow(2, bit)
    mask = size - 1
    cache = [[] for i in range(size)]
    count = 0
    for i in iterable:
        cache[i&mask].append(i)
        count += 1
    num = max([j for i in cache for j in i])
    print num
    ran = 1
    while num > (size << (bit * (ran - 1))):
        mask = mask << bit
        tmp = [[] for i in range(size)]
        for i in cache:
            for j in i:
                tmp[(j & mask) >> (bit * ran)].append(j)
                count += 1
        cache = tmp[:]
        ran += 1
        print ran
    res = []
    for i in cache:
        for j in i:
            res.append(j)
    return res, count

if __name__ == "__main__":
    import random
    a, c = radix_sort([random.randint(10,9999) for i in xrange(1000)])
    count = 0
    for i in a:
        count +=1
        print i,
        if count % 15 == 0:
            print
    print "\n\nIteration Count: ",
    print c, len(a), c / len(a)