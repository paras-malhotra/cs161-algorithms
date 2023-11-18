from typing import List, Callable, TypeVar

T = TypeVar('T')

def insertion_sort(arr: List[T], comparator: Callable[[T, T], bool] = lambda x, y: x < y) -> List[T]:
    """
    Perform an in-place insertion sort on a list with an optional custom comparator.

    Parameters:
    arr (List): A list of elements to be sorted.
    comparator (Callable[[int, int], bool], optional): A comparison function that returns True if the first argument is considered smaller than the second. Defaults to ascending order.

    Returns:
    List: The sorted list.

    Time Complexity:
    Average and Worst Case: O(n^2), where n is the number of items in the list.

    Example:
    >>> insertion_sort([3, 1, 4, 1, 5])
    [5, 4, 3, 1, 1]
    """
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and comparator(current, arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current

    return arr