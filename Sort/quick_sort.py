def quick_sort(iterable):
    x = [i for i in iterable]
    m = _median(x[0], x[len(x)>>1], x[-1])
    _pivoting(x, m, 0, len(x)-1)
    return x


def _pivoting(x, med, low, hi):
    m = _swap(x, med, low, hi)
    if m < hi:
        mid = _median(x[m+1], x[(m+hi+1)>>1], x[hi])
        _pivoting(x, mid, m+1, hi)
    if m > low:
        mid = _median(x[low], x[(m+low-1)>>1], x[m-1])
        _pivoting(x, mid, low, m-1)


def _swap(x, med, low, hi):
    while low < hi:
        while x[low] < med:
            low += 1
        while x[hi] > med:
            hi -= 1
        if low > hi:
            break
        x[low], x[hi] = x[hi], x[low]
        if x[low] == x[hi] == med:
            low -= 1
        elif x[low] == med:
            low -= 1
        elif x[hi] == med:
            hi += 1
        low += 1
        hi -= 1
    return low


def _median(a, b, c):
    print a, b, c
    if a <= b <= c or a >= b >= c:
        return b
    elif b <= a <= c or b >= a >= c:
        return a
    else:
        return c


if __name__=="__main__":
    import random
    x = [random.randint(10,100) for i in xrange(20)]
    a = [11-i for i in xrange(10)]
    print "Original ", x
    x = quick_sort(x)
    print "Sorted ", x
