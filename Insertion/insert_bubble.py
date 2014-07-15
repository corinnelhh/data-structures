def insertion_sort(iterable):
    x = iterable[:]
    for i in range(len(x)-1):
        j = i+1
        while j < len(x):
            if x[i] > x[j]:
                x[i], x[j] = x[j], x[i]
            j += 1
    return x


def bubble_sort(iterable):
    x = iterable[:]
    y = len(x) - 1
    while y > 0:
        i = 0
        while i < y:
            if x[i] > x[i+1]:
                x[i], x[i+1] = x[i+1], x[i]
            i += 1
        y -= 1
    return x


def time_track(size):
    import time
    a = [size-i for i in xrange(size)]
    print "Worst Case"

    start = time.clock()
    insertion_sort(a)
    end = time.clock()
    print "Insertion: %.2gs" % (end-start)

    start = time.clock()
    bubble_sort(a)
    end = time.clock()
    print "Bubble: %.2gs" % (end-start)


if __name__ == "__main__":
    size = 20000
    print "Size: "+str(size)
    time_track(size)
    print


# Size: 100
# Worst Case
# Insertion: 0s
# Bubble: 0s

# Size: 1000
# Worst Case
# Insertion: 0.18s
# Bubble: 0.21s

# Size: 10000
# Worst Case
# Insertion: 18s
# Bubble: 20s

# Size: 20000
# Worst Case
# Insertion: 72s
# Bubble: 81s

# Size: 100000
# It's not stopping