def merge(iterable):
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
    size = 10
    print "Size: "+str(size)
    a = [size-i for i in xrange(size)]
    print a, str(merge(a))
    import random
    a = [random.randint(10, 100) for i in xrange(size)]
    print a, str(merge(a))

