from typing import List, Callable, TypeVar
from binary_heap import BinaryHeap

T = TypeVar('T')

def heap_sort(arr: List[T], comparator: Callable[[T, T], bool] = lambda x, y: x < y) -> List[T]:
    """
    Perform a heap sort on a list with an optional custom comparator.
    This function is not in-place and returns a new sorted list.

    Parameters:
    arr (List[T]): A list of elements to be sorted.
    comparator (Callable[[T, T], bool], optional): A comparison function that returns True if the first argument is considered smaller than the second. Defaults to ascending order.

    Returns:
    List[T]: The sorted list.

    Time Complexity:
    Worst Case: O(nlog(n)), where n is the number of items in the list.

    Example:
    >>> heap_sort([3, 1, 4, 1, 5])
    [1, 1, 3, 4, 5]
    >>> heap_sort([3, 1, 4, 1, 5], lambda x, y: x > y)
    [5, 4, 3, 1, 1]
    """
    heap = BinaryHeap(comparator)
    heap.build(arr)
    sorted_arr = []

    for i in range(len(arr)):
        sorted_arr.append(heap.extract_top())

    return sorted_arr