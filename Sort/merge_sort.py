def merge_sort(iterable):
    x = iterable[:]
    size = len(x)>>1
    return _tail_merge(x[:size], x[size:])


def _tail_merge(left, right):
    if len(right) == 0:
        return left
    elif len(left) == 0:
        return right
    else:
        l = len(left) >> 1
        r = len(right) >> 1
        x = _tail_merge(left[:l], left[l:])
        y = _tail_merge(right[:r], right[r:])
        # print str(x), str(y)
        return _join(x, y)


def _join(x, y):
    result = []
    ix = iy = 0
    while True:
        if ix == len(x):
            for i in y[iy:]:
                result.append(i)
            break
        elif iy == len(y):
            for i in x[ix:]:
                result.append(i)
            break
        else:
            if x[ix] < y[iy]:
                result.append(x[ix])
                ix += 1
            else:
                result.append(y[iy])
                iy += 1
    return result


if __name__ == "__main__":
    import time
    size = 10
    print "Size: "+str(size)
    a = [size-i for i in xrange(size)]
    b = [i for i in xrange(size)]
    start = time.clock()
    merge_sort(a)
    end = time.clock()
    print "Worst Case %.2gs" % (end-start)
    start = time.clock()
    merge_sort(b)
    end = time.clock()
    print "Best Case %.2gs" % (end-start)


# Size: 1000
# Worst Case 0s
# Best Case 0.01s

# Size: 10000
# Worst Case 0.06s
# Best Case 0.05s

# Size: 100000
# Worst Case 0.63s
# Best Case 0.61s

# Size: 1000000
# Worst Case 7.2s
# Best Case 7s

# Size: 2000000
# Worst Case 15s
# Best Case 15s
