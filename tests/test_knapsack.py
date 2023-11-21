import pytest
from knapsack import unbounded_knapsack, zero_one_knapsack

# Define unbounded test cases
unbounded_test_cases = [
    (10, [6, 3, 4, 2], [30, 14, 16, 9], 48),
    (15, [6, 3, 4, 2], [30, 14, 16, 9], 74),
    (10, [3, 4, 2], [14, 16, 9], 46),
    (0, [1, 2, 3], [10, 20, 30], 0),
    (5, [1, 2, 3], [10, 20, 30], 50),
]

@pytest.mark.parametrize("budget, weights, values, expected", unbounded_test_cases)
def test_unbounded_knapsack(budget, weights, values, expected):
    assert unbounded_knapsack(budget, weights, values) == expected

# Define 0-1 test cases
zero_one_test_cases = [
    (10, [6, 3, 4, 2], [30, 14, 16, 9], 46),
    (15, [6, 3, 4, 2], [30, 14, 16, 9], 69),
    (10, [3, 4, 2, 6, 5], [14, 16, 9, 30, 50], 73),
    (0, [1, 2, 3], [10, 20, 30], 0),
    (5, [1, 2, 3], [10, 20, 30], 50),
]

@pytest.mark.parametrize("budget, weights, values, expected", zero_one_test_cases)
def test_zero_one_knapsack(budget, weights, values, expected):
    assert zero_one_knapsack(budget, weights, values) == expected
