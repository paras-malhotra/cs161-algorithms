from typing import List, Callable, TypeVar

T = TypeVar('T')

def bucket_sort(arr: List[T], k: int, key: Callable[[T], int] = lambda x: x) -> List[T]:
    """
    Perform a bucket sort on a list with an optional custom key function.

    Parameters:
    arr (List[T]): A list of elements to be sorted.
    k (int): The number of buckets to use.
    key (Callable[[T], int], optional): A function that maps an element to a bucket index. Defaults to identity function.

    Returns:
    List[T]: The sorted list.

    Time Complexity:
    Average Case: O(n + k), where n is the number of items in the list and k is the number of buckets.

    Example:
    >>> bucket_sort([3, 1, 4, 1, 2], 4, lambda x: x - 1)
    [1, 1, 2, 3, 4]
    >>> bucket_sort([(3, 1), (2, 1), (1, 1), (1, 2), (2, 2)], 3, lambda x: x[0] - 1)
    [(1, 1), (1, 2), (2, 1), (2, 2), (3, 1)]
    """
    buckets = [[] for _ in range(k)]
    sorted_arr = []

    for x in arr:
        buckets[key(x)].append(x)

    for bucket in buckets:
        sorted_arr += bucket

    return sorted_arr