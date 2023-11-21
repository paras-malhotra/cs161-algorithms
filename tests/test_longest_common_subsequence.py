import pytest
from typing import List
from longest_common_subsequence import length_longest_common_subsequence_prefix, longest_common_subsequence_via_prefix, length_longest_common_subsequence_suffix, longest_common_subsequence_via_suffix

# Test for length_longest_common_subsequence_prefix
@pytest.mark.parametrize("x, y, expected", [
    ('abcde', 'ace', [[0, 0, 0, 0], [0, 1, 1, 1], [0, 1, 1, 1], [0, 1, 2, 2], [0, 1, 2, 2], [0, 1, 2, 3]]),
    ('abc', 'abc', [[0, 0, 0, 0], [0, 1, 1, 1], [0, 1, 2, 2], [0, 1, 2, 3]]),
    ('abc', 'def', [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
])
def test_length_longest_common_subsequence_prefix(x, y, expected):
    assert length_longest_common_subsequence_prefix(x, y) == expected

# Test for longest_common_subsequence_via_prefix
@pytest.mark.parametrize("x, y, expected", [
    ('abcde', 'ace', 'ace'),
    ('abc', 'abc', 'abc'),
    ('abc', 'def', '')
])
def test_longest_common_subsequence_via_prefix(x, y, expected):
    assert longest_common_subsequence_via_prefix(x, y) == expected

# Test for length_longest_common_subsequence_suffix
@pytest.mark.parametrize("x, y, expected", [
    ('abcde', 'ace', [[3, 2, 1, 0], [2, 2, 1, 0], [2, 2, 1, 0], [1, 1, 1, 0], [1, 1, 1, 0], [0, 0, 0, 0]]),
    ('abc', 'abc', [[3, 2, 1, 0], [2, 2, 1, 0], [1, 1, 1, 0], [0, 0, 0, 0]]),
    ('abc', 'def', [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
])
def test_length_longest_common_subsequence_suffix(x, y, expected):
    assert length_longest_common_subsequence_suffix(x, y) == expected

# Test for longest_common_subsequence_via_suffix
@pytest.mark.parametrize("x, y, expected", [
    ('abcde', 'ace', 'ace'),
    ('abc', 'abc', 'abc'),
    ('abc', 'def', '')
])
def test_longest_common_subsequence_via_suffix(x, y, expected):
    assert longest_common_subsequence_via_suffix(x, y) == expected

# Test for length_longest_common_subsequence_prefix with integer lists
@pytest.mark.parametrize("x, y, expected", [
    ([1, 2, 3, 4, 5], [1, 3, 5], [[0, 0, 0, 0], [0, 1, 1, 1], [0, 1, 1, 1], [0, 1, 2, 2], [0, 1, 2, 2], [0, 1, 2, 3]]),
    ([1, 3, 5], [1, 2, 3, 4, 5], [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 2, 2, 2], [0, 1, 1, 2, 2, 3]])
])
def test_length_longest_common_subsequence_prefix_integers(x, y, expected):
    assert length_longest_common_subsequence_prefix(x, y) == expected

# Test for longest_common_subsequence_via_prefix with integer lists
@pytest.mark.parametrize("x, y, expected", [
    ([1, 2, 3, 4, 5], [1, 3, 5], [1, 3, 5]),
    ([1, 3, 5], [1, 2, 3, 4, 5], [1, 3, 5])
])
def test_longest_common_subsequence_via_prefix_integers(x, y, expected):
    assert longest_common_subsequence_via_prefix(x, y) == expected

# Test for length_longest_common_subsequence_suffix with integer lists
@pytest.mark.parametrize("x, y, expected", [
    ([1, 2, 3, 4, 5], [1, 3, 5], [[3, 2, 1, 0], [2, 2, 1, 0], [2, 2, 1, 0], [1, 1, 1, 0], [1, 1, 1, 0], [0, 0, 0, 0]]),
    ([1, 3, 5], [1, 2, 3, 4, 5], [[3, 2, 2, 1, 1, 0], [2, 2, 2, 1, 1, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0]])
])
def test_length_longest_common_subsequence_suffix_integers(x, y, expected):
    assert length_longest_common_subsequence_suffix(x, y) == expected

# Test for longest_common_subsequence_via_suffix with integer lists
@pytest.mark.parametrize("x, y, expected", [
    ([1, 2, 3, 4, 5], [1, 3, 5], [1, 3, 5]),
    ([1, 3, 5], [1, 2, 3, 4, 5], [1, 3, 5])
])
def test_longest_common_subsequence_via_suffix_integers(x, y, expected):
    assert longest_common_subsequence_via_suffix(x, y) == expected