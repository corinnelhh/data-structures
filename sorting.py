import random
import time
import matplotlib.pyplot as plt


def insertion_sort(i_list):
    for i in range(len(i_list)):
        idx = i
        while (idx > 0) and (i_list[idx - 1] > i_list[idx]):
            i_list[idx], i_list[idx - 1] = i_list[idx - 1], i_list[idx]
            idx -= 1
    return i_list


def merge_sort(i_list):
    if len(i_list) == 1:
        return i_list
    else:
        mid = len(i_list) / 2
        left = merge_sort(i_list[:mid])
        right = merge_sort(i_list[mid:])
        print left, right
        return _split_sorting(left, right)


def _split_sorting(left, right):
    ret_list = []
    count = 0
    while len(left) or len(right):
        if len(left) and len(right):
            if left[0] <= right[0]:
                ret_list.append(left[0])
                left = left[1:]
            else:
                ret_list.append(right[0])
                right = right[1:]
        elif len(left):
            ret_list.append(left[0])
            left = left[1:]
        elif len(right):
            ret_list.append(right[0])
            right = right[1:]
        count += 1
    return ret_list


def quick_sort(i_list):
    pass




def plot_insertion_sort():
    avg_bests = []
    avg_worsts = []

    for i in range(1, 502, 100):
        n_tester_list = [random.randint(0, 1000) for m in range(i)]
        count = 0
        b_list = []
        w_list = []
        while count < 10:
            b_start = time.clock()
            insertion_sort(n_tester_list)
            b_end = time.clock()
            b_list.append(b_end - b_start)

            worst_list = n_tester_list[::-1]
            w_start = time.clock()
            insertion_sort(worst_list)
            w_end = time.clock()
            w_list.append(w_end - w_start)
            count += 1
        b_average = sum(b_list) / 10
        w_average = sum(w_list) / 10

        print "With n of: ", i
        print "The average time for the best case is: ", b_average
        print "The average time for the worst case is: ", w_average
        print
        avg_bests.append((i, b_average))
        avg_worsts.append((i, w_average))

    plt.plot(avg_bests)


if __name__ == '__main__':
    tester_list = [random.randint(0, 100) for i in range(10)]
    our_sorted_list = quick_sort(tester_list)
    print tester_list
    print our_sorted_list
    assert sorted(tester_list) == our_sorted_list

    # our_list = insertion_sort(tester_list)
    # our_s_list = sorted(tester_list)
    # try:
    #     assert our_s_list == our_list
    #     print
    #     print "Insertion sort successful"
    # except AssertionError:
    #     print "Sorry, your sorting algorithm failed."
    # print
    # print "Now testing performance."
    # print
    # print "Best case scenario is a perfectly sorted list."
    # print "Worst case scenerio is a reversed perfectly sorted list."

    # avg_bests = []
    # avg_worsts = []

    # for i in range(1, 1002, 100):
    #     n_tester_list = [random.randint(0, 1000) for m in range(i)]
    #     count = 0
    #     b_list = []
    #     w_list = []
    #     while count < 10:
    #         b_start = time.clock()
    #         insertion_sort(n_tester_list)
    #         b_end = time.clock()
    #         b_list.append(b_end - b_start)

    #         worst_list = n_tester_list[::-1]
    #         w_start = time.clock()
    #         insertion_sort(worst_list)
    #         w_end = time.clock()
    #         w_list.append(w_end - w_start)
    #         count += 1
    #     b_average = sum(b_list) / 10
    #     w_average = sum(w_list) / 10

    #     print "With n of: ", i
    #     print "The average time for the best case is: ", b_average
    #     print "The average time for the worst case is: ", w_average
    #     print
    #     avg_bests.append((i, b_average))
    #     avg_worsts.append((i, w_average))
