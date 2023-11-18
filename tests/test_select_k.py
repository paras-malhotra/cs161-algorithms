from select_k import select_k, quick_select_k
import pytest
import random

pytestmark = pytest.mark.parametrize("selectk_function", [select_k, quick_select_k])

def test_select_k_small_array(selectk_function):
    assert selectk_function([3, 1, 4, 1, 5], 3) == 3

def test_select_k_with_custom_comparator(selectk_function):
    assert selectk_function([3, 1, 4, 1, 5], 4, lambda x, y: x > y) == 1

def test_select_k_first_element(selectk_function):
    assert selectk_function([3, 1, 4, 1, 5], 1) == 1

def test_select_k_last_element(selectk_function):
    assert selectk_function([3, 1, 4, 1, 5], 5) == 5

def test_select_k_large_array(selectk_function):
    arr = [i for i in range(1, 102)]
    random.shuffle(arr)
    assert selectk_function(arr, 45) == 45
