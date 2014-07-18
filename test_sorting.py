import random
from sorting import insertion_sort, merge_sort, quick_sort


def test_insertion_sort():
    tester_list = [random.randint(0, 100) for i in range(100)]
    s_tester_list = sorted(tester_list)
    sorted_list = insertion_sort(tester_list)
    assert sorted_list == s_tester_list


def test_merge_sort():
    tester_list = [random.randint(0, 100) for i in range(100)]
    s_tester_list = sorted(tester_list)
    sorted_list = merge_sort(tester_list)
    assert sorted_list == s_tester_list


def test_quick_sort():
    tester_list = [random.randint(0, 100) for i in range(100)]
    s_tester_list = sorted(tester_list)
    sorted_list = quick_sort(tester_list)
    assert sorted_list == s_tester_list
