from typing import List, Callable, TypeVar
from merge_sort import merge_sort
import random

T = TypeVar('T')

def select_k(arr: List[T], k: int, comparator: Callable[[T, T], bool] = lambda x, y: x < y) -> T:
    """
    Select the kth smallest element from a list with an optional custom comparator. This function uses the median of medians algorithm to select the pivot element.

    Parameters:
    arr (List[T]): A list of elements to be sorted.
    k (int): The kth smallest element to select.
    comparator (Callable[[T, T], bool], optional): A comparison function that returns True if the first argument is considered smaller than the second. Defaults to ascending order.

    Returns:
    T: The selected element.

    Time Complexity:
    Worst Case: O(n), where n is the number of items in the list.

    Example:
    >>> select_k([3, 1, 4, 1, 5], 3)
    3
    >>> select_k([3, 1, 4, 1, 5], 4, lambda x, y: x > y)
    1
    """
    if len(arr) <= 1:
        return arr[0]

    if len(arr) <= 30:
        # Avoids maximum recursion depth error
        return merge_sort(arr, comparator)[k - 1]

    pivot = choose_pivot(arr)
    left = [x for x in arr if comparator(x, pivot)]
    right = [x for x in arr if not comparator(x, pivot)]

    if len(left) == k - 1:
        return pivot
    elif len(left) > k - 1:
        return select_k(left, k, comparator)
    else:
        return select_k(right, k - len(left), comparator)

def quick_select_k(arr: List[T], k: int, comparator: Callable[[T, T], bool] = lambda x, y: x < y) -> T:
    """
    Select the kth smallest element from a list with an optional custom comparator. This function uses a randomized pivot selection.

    Parameters:
    arr (List[T]): A list of elements to be sorted.
    k (int): The kth smallest element to select.
    comparator (Callable[[T, T], bool], optional): A comparison function that returns True if the first argument is considered smaller than the second. Defaults to ascending order.

    Returns:
    T: The selected element.

    Time Complexity:
    Worst Case: O(n), where n is the number of items in the list.

    Example:
    >>> quick_select_k([3, 1, 4, 1, 5], 3)
    3
    >>> quick_select_k([3, 1, 4, 1, 5], 4, lambda x, y: x > y)
    1
    """
    if len(arr) <= 1:
        return arr[0]

    if len(arr) <= 30:
        # Avoids maximum recursion depth error
        return merge_sort(arr, comparator)[k - 1]

    pivot = random.choice(arr)
    left = [x for x in arr if comparator(x, pivot)]
    right = [x for x in arr if not comparator(x, pivot)]

    if len(left) == k - 1:
        return pivot
    elif len(left) > k - 1:
        return quick_select_k(left, k, comparator)
    else:
        return quick_select_k(right, k - len(left), comparator)

def choose_pivot(arr: List[T], comparator: Callable[[T, T], bool] = lambda x, y: x < y) -> T:
    """
    Choose a pivot element from a list by splitting the list into groups of 5 and selecting the median of each group. Then, select the median of the medians as the pivot element.

    Parameters:
    arr (List[T]): A list of elements to be sorted.
    comparator (Callable[[T, T], bool], optional): A comparison function that returns True if the first argument is considered smaller than the second. Defaults to ascending order.

    Returns:
    T: The selected pivot element.

    Example:
    >>> choose_pivot([1, 3, 2, 5, 4])
    3
    >>> choose_pivot([1, 3, 2, 5, 4], lambda x, y: x > y)
    3
    """
    groups = [arr[i:i + 5] for i in range(0, len(arr), 5)]
    medians = [merge_sort(group, comparator)[len(group) // 2] for group in groups]
    return select_k(medians, len(medians) // 2, comparator)
