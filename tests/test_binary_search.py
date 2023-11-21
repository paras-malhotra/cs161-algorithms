import pytest
from binary_search import binary_search_list, binary_search_lower_bound, binary_search_upper_bound, binary_search_monotonically_increasing

@pytest.mark.parametrize("arr, target, expected", [
    ([1, 2, 3, 4, 5], 3, 2),
    ([1, 2, 3, 4, 5], 1, 0),
    ([1, 2, 3, 4, 5], 5, 4),
    ([1, 2, 3, 4, 5], 6, -1),
    ([], 3, -1),
    ([10], 10, 0),
    ([1, 2, 4, 5, 6], 3, -1)
])
def test_binary_search_list(arr, target, expected):
    assert binary_search_list(arr, target) == expected

@pytest.mark.parametrize("arr, target, expected", [
    ([1, 2, 3, 4, 5], 3, 2),
    ([1, 2, 4, 5, 6], 3, 1),
    ([1, 2, 4, 5, 6], 1, 0),
    ([1, 2, 4, 5, 6], 0, -1),
    ([], 3, -1),
    ([10], 5, -1),
    ([1, 2, 4, 5, 6], 6, 4)
])
def test_binary_search_lower_bound(arr, target, expected):
    assert binary_search_lower_bound(arr, target) == expected

@pytest.mark.parametrize("arr, target, expected", [
    ([1, 2, 3, 4, 5], 3, 2),
    ([1, 2, 4, 5, 6], 3, 2),
    ([1, 2, 4, 5, 6], 7, 5),
    ([1, 2, 4, 5, 6], 1, 0),
    ([], 3, 0),
    ([10], 15, 1),
    ([1, 2, 4, 5, 6], 1, 0)
])
def test_binary_search_upper_bound(arr, target, expected):
    assert binary_search_upper_bound(arr, target) == expected

@pytest.mark.parametrize("func, target, left, right, expected", [
    (lambda x: x**2, 3, 0, 3, 1.7320508075688772),  # Square root of 3
    (lambda x: 2**x, 10, 0, 10, 3.321928094887362), # Logarithm base 2 of 10
])
def test_binary_search_monotonically_increasing(func, target, left, right, expected):
    result = binary_search_monotonically_increasing(func, target, left, right)
    assert abs(result - expected) < 1e-7  # Check if the result is within the precision threshold