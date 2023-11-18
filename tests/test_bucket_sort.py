from bucket_sort import bucket_sort
import random

def test_bucket_sort_simple_case():
    assert bucket_sort([3, 1, 4, 1, 2], 4, lambda x: x - 1) == [1, 1, 2, 3, 4]

def test_bucket_sort_tuples():
    assert bucket_sort([(3, 1), (2, 1), (1, 1), (1, 2), (2, 2)], 3, lambda x: x[0] - 1) == [(1, 1), (1, 2), (2, 1), (2, 2), (3, 1)]

def test_bucket_sort_empty():
    assert bucket_sort([], 4) == []

def test_bucket_sort_single_element():
    assert bucket_sort([1], 4) == [1]

def test_bucket_sort_large_array():
    arr = [i for i in range(101)]
    random.shuffle(arr)
    assert bucket_sort(arr, 101) == [i for i in range(101)]
