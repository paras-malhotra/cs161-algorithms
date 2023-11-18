from typing import List, Callable, TypeVar

T = TypeVar('T')

def merge_sort(arr: List[T], comparator: Callable[[T, T], bool] = lambda x, y: x < y) -> List[T]:
    """
    Perform a merge sort on a list with an optional custom comparator.
    This function is not in-place and returns a new sorted list.

    Parameters:
    arr (List[T]): A list of elements to be sorted.
    comparator (Callable[[T, T], bool], optional): A comparison function that returns True if the first argument is considered smaller than the second. Defaults to ascending order.

    Returns:
    List[T]: The sorted list.

    Time Complexity:
    Worst Case: O(nlog(n)), where n is the number of items in the list.

    Example:
    >>> merge_sort([3, 1, 4, 1, 5])
    [1, 1, 3, 4, 5]
    >>> merge_sort([3, 1, 4, 1, 5], lambda x, y: x > y)
    [5, 4, 3, 1, 1]
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid], comparator)
    right = merge_sort(arr[mid:], comparator)

    return merge(left, right, comparator)

def merge(left: List[T], right: List[T], comparator: Callable[[T, T], bool] = lambda x, y: x < y) -> List[T]:
    """
    Merge two sorted lists into a single sorted list.

    Parameters:
    left (List[T]): A sorted list.
    right (List[T]): A sorted list.
    comparator (Callable[[T, T], bool]): A comparison function that returns True if the first argument is considered smaller than the second.

    Returns:
    List[T]: The merged and sorted list.

    Example:
    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([5, 3, 1], [6, 4, 2], lambda x, y: x > y)
    [6, 5, 4, 3, 2, 1]
    """
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if comparator(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result