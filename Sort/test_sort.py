import pytest
from insert_bubble import insertion_sort, bubble_sort
from merge_sort import merge_sort, _join, _tail_merge
from quick_sort import quick_sort, _median

@pytest.fixture(scope="function")
def build_list():
    unsort = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    sort = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return unsort, sort


def test_insertion(build_list):
    x, y = build_list
    assert insertion_sort(x) == y


def test_bubble(build_list):
    x, y = build_list
    assert bubble_sort(x) == y


def test_merge(build_list):
    x, y = build_list
    assert merge_sort(x) == y


def test_merge_join(build_list):
    x, y = build_list
    assert _join(x, y) == y + x


def test_merge_tail(build_list):
    x, y = build_list
    assert _tail_merge(x, y) == insertion_sort(x + y)


def test_median():
    assert _median(1, 2, 3) == 2


def test_quick_sort(build_list):
    x, y = build_list
    assert quick_sort(x) == y

    import random
    for i in xrange(100):
        x = [random.randint(10,100) for i in xrange(20)]
        y = merge_sort(x)
        z = quick_sort(x)
        assert y == z
