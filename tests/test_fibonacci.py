import pytest
from fibonacci import fibonacci_top_down, fibonacci_bottom_up

# Define test data for Fibonacci numbers
fibonacci_test_cases = [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (8, 21),
    (9, 34),
    (40, 102334155),
    (50, 12586269025),
]

@pytest.mark.parametrize("n, expected", fibonacci_test_cases)
def test_fibonacci_top_down(n, expected):
    assert fibonacci_top_down(n) == expected

@pytest.mark.parametrize("n, expected", fibonacci_test_cases)
def test_fibonacci_bottom_up(n, expected):
    assert fibonacci_bottom_up(n) == expected
