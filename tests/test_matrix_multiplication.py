import pytest
from matrix_multiplication import multiply_square_matrices

test_cases = [
    # Base cases
    ([[1]], [[2]], [[2]]),
    ([[1, 2], [3, 4]], [[5, 6], [7, 8]], [[19, 22], [43, 50]]),
    ([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]], [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]], [[4, 4, 4, 4], [4, 4, 4, 4], [4, 4, 4, 4], [4, 4, 4, 4]]),
    # Zero matrix
    ([[1, 2], [3, 4]], [[0, 0], [0, 0]], [[0, 0], [0, 0]]),
    # Single digit
    ([[7]], [[8]], [[56]]),
    # Negative numbers
    ([[-1, -2], [-3, -4]], [[-5, -6], [-7, -8]], [[19, 22], [43, 50]]),
    ([[1, 2], [3, 4]], [[-5, -6], [-7, -8]], [[-19, -22], [-43, -50]]),
    ([[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]], [[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]], [[4, 4, 4, 4], [4, 4, 4, 4], [4, 4, 4, 4], [4, 4, 4, 4]]),
]
@pytest.mark.parametrize("A, B, expected", test_cases)
def test_multiply_square_matrices(A, B, expected):
    assert multiply_square_matrices(A, B) == expected