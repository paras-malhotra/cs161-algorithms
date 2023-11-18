from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
import random
import pytest

pytestmark = pytest.mark.parametrize("sort_function", [insertion_sort, merge_sort, quick_sort])

def test_sort_ascending(sort_function):
    assert sort_function([3, 2, 1]) == [1, 2, 3]
    assert sort_function([1, 3, 5, 2, 4]) == [1, 2, 3, 4, 5]

def test_sort_descending(sort_function):
    assert sort_function([3, 2, 1], lambda x, y: x > y) == [3, 2, 1]
    assert sort_function([3, 1, 4, 2, 5], lambda x, y: x > y) == [5, 4, 3, 2, 1]

def test_sort_empty(sort_function):
    assert sort_function([]) == []

def test_sort_single_element(sort_function):
    assert sort_function([5]) == [5]

def test_sort_duplicate_elements(sort_function):
    assert sort_function([3, 2, 1, 2, 3]) == [1, 2, 2, 3, 3]
    assert sort_function([5, 5, 4, 3, 3, 4], lambda x, y: x > y) == [5, 5, 4, 4, 3, 3]
    assert sort_function([2, 3, 4, 3] + [1 for i in range(100)]) == ([1 for i in range(100)] + [2, 3, 3, 4])

def test_sort_negative_numbers(sort_function):
    assert sort_function([-3, -1, -4, -1, -5]) == [-5, -4, -3, -1, -1]

def test_sort_large_array(sort_function):
    arr = [i for i in range(1, 102)]
    random.shuffle(arr)
    assert sort_function(arr) == [i for i in range(1, 102)]