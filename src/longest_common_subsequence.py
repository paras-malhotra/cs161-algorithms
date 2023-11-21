from typing import List, TypeVar, Sequence

T = TypeVar('T')

def length_longest_common_subsequence_prefix(x: Sequence[T], y: Sequence[T]) -> List[List[int]]:
    """
    Find the length of the longest common subsequence of the prefixes of x and y.

    Parameters:
        x (Sequence[T]): The first sequence.
        y (Sequence[T]): The second sequence.

    Returns:
        List[List[int]]: A table of size (len(x) + 1) * (len(y) + 1) such that table[i][j] is the length of the longest common subsequence of the prefixes x[:i] and y[:j].

    Time complexity: O(mn)
    Space complexity: O(mn)

    Examples:
    >>> length_longest_common_subsequence_prefix('abcde', 'ace')
    [[0, 0, 0, 0], [0, 1, 1, 1], [0, 1, 1, 1], [0, 1, 2, 2], [0, 1, 2, 2], [0, 1, 2, 3]]
    >>> length_longest_common_subsequence_prefix('abc', 'abc')
    [[0, 0, 0, 0], [0, 1, 1, 1], [0, 1, 2, 2], [0, 1, 2, 3]]
    >>> length_longest_common_subsequence_prefix('abc', 'def')
    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    >>> length_longest_common_subsequence_prefix([1, 2, 3, 4, 5], [1, 3, 5])
    [[0, 0, 0, 0], [0, 1, 1, 1], [0, 1, 1, 1], [0, 1, 2, 2], [0, 1, 2, 2], [0, 1, 2, 3]]
    """
    m = len(x)
    n = len(y)

    # Initialize the lengths
    lengths = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Fill the lengths
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                lengths[i][j] = lengths[i - 1][j - 1] + 1
            else:
                lengths[i][j] = max(lengths[i - 1][j], lengths[i][j - 1])

    return lengths

def longest_common_subsequence_via_prefix(x: Sequence[T], y: Sequence[T]) -> Sequence[T]:
    """
    Find the longest common subsequence of x and y using the length of the longest common subsequence of the prefixes of x and y.

    Parameters:
        x (Sequence[T]): The first sequence.
        y (Sequence[T]): The second sequence.

    Returns:
        Sequence[T]: The longest common subsequence of x and y.

    Time complexity: O(mn)
    Space complexity: O(mn)

    Examples:
    >>> longest_common_subsequence('abcde', 'ace')
    'ace'
    >>> longest_common_subsequence('abc', 'abc')
    'abc'
    >>> longest_common_subsequence('abc', 'def')
    ''
    >>> longest_common_subsequence([1, 2, 4, 5, 6], [1, 2, 3, 4, 5])
    [1, 2, 4, 5]
    """
    # Find the lengths
    lengths = length_longest_common_subsequence_prefix(x, y)
    m = len(x)
    n = len(y)

    # Reconstruct the subsequence
    subsequence = []
    while m > 0 and n > 0:
        if x[m - 1] == y[n - 1]:
            subsequence.insert(0, x[m - 1])
            m -= 1
            n -= 1
        elif lengths[m - 1][n] > lengths[m][n - 1]:
            m -= 1
        else:
            n -= 1

    if isinstance(x, str) and isinstance(y, str):
        return ''.join(subsequence)
    else:
        return subsequence

def length_longest_common_subsequence_suffix(x: Sequence[T], y: Sequence[T]) -> List[List[int]]:
    """
    Find the length of the longest common subsequence of the suffixes of x and y.

    Parameters:
        x (Sequence[T]): The first sequence.
        y (Sequence[T]): The second sequence.

    Returns:
        List[List[int]]: A table of size (len(x) + 1) * (len(y) + 1) such that table[i][j] is the length of the longest common subsequence of the suffixes x[i:] and y[j:].

    Time complexity: O(mn)
    Space complexity: O(mn)

    Examples:
    >>> length_longest_common_subsequence_suffix('abcde', 'ace')
    [[3, 2, 1, 0], [2, 2, 1, 0], [2, 2, 1, 0], [1, 1, 1, 0], [1, 1, 1, 0], [0, 0, 0, 0]]
    >>> length_longest_common_subsequence_suffix('abc', 'abc')
    [[3, 2, 1, 0], [2, 2, 1, 0], [1, 1, 1, 0], [0, 0, 0, 0]]
    >>> length_longest_common_subsequence_suffix('abc', 'def')
    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    >>> length_longest_common_subsequence_suffix([1, 3, 5], [1, 2, 3, 4, 5])
    [[3, 2, 2, 1, 1, 0], [2, 2, 2, 1, 1, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0]]
    """
    m = len(x)
    n = len(y)

    # Initialize the lengths
    lengths = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Fill the lengths
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if x[i] == y[j]:
                lengths[i][j] = lengths[i + 1][j + 1] + 1
            else:
                lengths[i][j] = max(lengths[i + 1][j], lengths[i][j + 1])

    return lengths

def longest_common_subsequence_via_suffix(x: Sequence[T], y: Sequence[T]) -> Sequence[T]:
    """
    Find the longest common subsequence of x and y using the length of the longest common subsequence of the suffixes of x and y.

    Parameters:
        x (Sequence[T]): The first sequence.
        y (Sequence[T]): The second sequence.

    Returns:
        Sequence[T]: The longest common subsequence of x and y.

    Time complexity: O(mn)
    Space complexity: O(mn)

    Examples:
    >>> longest_common_subsequence('abcde', 'ace')
    'ace'
    >>> longest_common_subsequence('abc', 'abc')
    'abc'
    >>> longest_common_subsequence('abc', 'def')
    ''
    >>> longest_common_subsequence([1, 2, 4, 5, 6], [1, 2, 3, 4, 5])
    [1, 2, 4, 5]
    """
    # Find the lengths
    lengths = length_longest_common_subsequence_suffix(x, y)
    m = len(x)
    n = len(y)

    # Reconstruct the subsequence
    subsequence = []
    i = 0
    j = 0
    while i < m and j < n:
        if x[i] == y[j]:
            subsequence.append(x[i])
            i += 1
            j += 1
        elif lengths[i + 1][j] > lengths[i][j + 1]:
            i += 1
        else:
            j += 1

    if isinstance(x, str) and isinstance(y, str):
        return ''.join(subsequence)
    else:
        return subsequence