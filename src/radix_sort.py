from typing import List, TypeVar
from bucket_sort import bucket_sort

T = TypeVar('T')

def radix_sort(arr: List[int], base: int = 10, num_digits: int = 0) -> List[int]:
    """
    Perform a radix sort on a list with an optional custom base and number of digits. Works only on non-negative integers.

    Parameters:
    arr (List[int]): A list of integer elements to be sorted.
    base (int, optional): The base to use. Defaults to 10.
    num_digits (int, optional): The number of digits to use. Defaults to the maximum number of digits in the list.

    Returns:
    List[int]: The sorted list.

    Time Complexity:
    Worst Case: O(d * (n + r)), where d is the maximum number of digits, n is the number of items in the list, and r is the base.

    Example:
    >>> radix_sort([3, 1, 4, 1, 5])
    [1, 1, 3, 4, 5]
    >>> radix_sort([3, 1, 4, 1, 5], 2, 3)
    [1, 1, 3, 4, 5]
    """
    if num_digits == 0:
        num_digits = len(str(max(arr)))

    for exponent in range(num_digits):
        arr = bucket_sort(arr, base, lambda x: (x // base ** exponent) % base)

    return arr