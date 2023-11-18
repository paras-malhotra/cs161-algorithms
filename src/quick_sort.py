from typing import List, Callable, TypeVar
import random

T = TypeVar('T')

def quick_sort(arr: List[T], comparator: Callable[[T, T], bool] = lambda x, y: x < y) -> List[T]:
    """
    Perform a quick sort on a list with an optional custom comparator. This function is in-place and returns the original list.

    Parameters:
    arr (List[T]): A list of elements to be sorted.
    comparator (Callable[[T, T], bool], optional): A comparison function that returns True if the first argument is considered smaller than the second. Defaults to ascending order.

    Returns:
    List[T]: The sorted list.

    Time Complexity:
    Expected: O(nlog(n)), where n is the number of items in the list.

    Example:
    >>> quick_sort([3, 1, 4, 1, 5])
    [1, 1, 3, 4, 5]
    >>> quick_sort([3, 1, 4, 1, 5], lambda x, y: x > y)
    [5, 4, 3, 1, 1]
    """
    if len(arr) <= 1:
        return arr

    pivot = random.choice(arr)

    # < and > arrays are chosen instead of < and >= arrays to avoid infinite recursion or maximum recursion depth error
    less = [x for x in arr if comparator(x, pivot)]
    greater = [x for x in arr if not comparator(x, pivot) and x != pivot]

    return quick_sort(less, comparator) + [x for x in arr if x == pivot] + quick_sort(greater, comparator)