def insertion_sort(iterable):
    x = [i for i in iterable]
    for i in range(len(x)-1):
        j = i+1
        while j < len(x):
            if x[i] > x[j]:
                x[i], x[j] = x[j], x[i]
            j += 1
    return x


def bubble_sort(iterable):
    x = [i for i in iterable]
    y = len(x) - 1
    while y > 0:
        i = 0
        while i < y:
            if x[i] > x[i+1]:
                x[i], x[i+1] = x[i+1], x[i]
            i += 1
        y -= 1
    return x


if __name__ == "__main__":
    a = [10,9,8,7,6,5,4,3,2,1]
    print str(insertion_sort(a))
    print str(bubble_sort(a))
