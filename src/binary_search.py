from typing import List, TypeVar, Callable

T = TypeVar('T')

def binary_search_list(arr: List[T], target: T) -> int:
    """
    Perform binary search on a sorted list.

    Parameters:
        arr (List[T]): The list to search in, must be pre-sorted in ascending order.
        target (T): The target to search for.

    Returns:
        int: The index of the target in the list, or -1 if not found.

    Worst-case time complexity: O(log n)

    Example:
    >>> binary_search_list([1, 2, 3, 4, 5], 3)
    2
    >>> binary_search_list([1, 2, 3, 4, 5], 6)
    -1
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        # Loop invariant: arr[left] <= target <= arr[right]
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            return mid

    return -1

def binary_search_lower_bound(arr: List[T], target: T) -> int:
    """
    Perform binary search on a sorted list to find the closest element to the left of the target, i.e., the largest element in the list <= target.

    Parameters:
        arr (List[T]): The list to search in, must be pre-sorted in ascending order.
        target (T): The target to search for.

    Returns:
        int: The index of the closest element to the left of the target in the list or -1 if target is smaller than all elements in the list.

    Worst-case time complexity: O(log n)

    Example:
    >>> binary_search_lower_bound([1, 2, 3, 4, 5], 3)
    2
    >>> binary_search_lower_bound([1, 2, 4, 5, 6], 3)
    1
    >>> binary_search_lower_bound([1, 2, 3, 4, 5], 0)
    -1
    """
    left = -1
    right = len(arr)

    while right > left + 1:
        mid = (left + right) // 2

        # Loop invariant: arr[left] <= target < arr[right]
        if arr[mid] <= target:
            left = mid
        else:
            right = mid

    return left

def binary_search_upper_bound(arr: List[T], target: T) -> int:
    """
    Perform binary search on a sorted list to find the closest element to the right of the target, i.e., the smallest element in the list >= target.

    Parameters:
        arr (List[T]): The list to search in, must be pre-sorted in ascending order.
        target (T): The target to search for.

    Returns:
        int: The index of the closest element to the right of the target in the list or len(arr) if target is larger than all elements in the list.

    Worst-case time complexity: O(log n)

    Example:
    >>> binary_search_upper_bound([1, 2, 3, 4, 5], 3)
    2
    >>> binary_search_upper_bound([1, 2, 4, 5, 6], 3)
    2
    >>> binary_search_upper_bound([1, 2, 4, 5, 6], 7)
    5
    """
    left = -1
    right = len(arr)

    while right > left + 1:
        mid = (left + right) // 2

        # Loop invariant: arr[left] < target <= arr[right]
        if arr[mid] < target:
            left = mid
        else:
            right = mid

    return right

def binary_search_monotonically_increasing(func: Callable[[float], float], target: float, left: float, right: float, precision: float = 1e-7) -> float:
    """
    Perform binary search on a monotonically increasing function.

    Parameters:
        func (Callable[[float], float]): The function to search in, must be monotonically increasing within the search interval.
        target (float): The target to search for.
        left (float): The left boundary of the search interval.
        right (float): The right boundary of the search interval.
        precision (float): The precision threshold for termination.

    Returns:
        float: The value of x such that func(x) is closest to the target.

    Example:
    >>> binary_search_monotonically_increasing(lambda x: x**2, 3, 0, 3)
    1.7320508075688772
    >>> binary_search_monotonically_increasing(lambda x: 2**x, 10, 0, 10)
    3.321928094887362

    Note: The above examples are for computing the square root of 3 and the logarithm (base 2) of 10, respectively.
    """

    while right - left > precision:
        mid = (left + right) / 2

        if func(mid) < target:
            left = mid
        else:
            right = mid

    return (left + right) / 2