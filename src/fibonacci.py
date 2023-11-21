memo = {}

def fibonacci_top_down(n: int) -> int:
    """
    Get the nth Fibonacci number using top-down dynamic programming using memoization.

    Time complexity: O(n)
    Space complexity: O(n)
    """
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fibonacci_top_down(n - 1) + fibonacci_top_down(n - 2)
    return memo[n]

def fibonacci_bottom_up(n: int) -> int:
    """
    Get the nth Fibonacci number using bottom-up (iterative) dynamic programming.

    Time complexity: O(n)
    Space complexity: O(1)
    """
    if n <= 1:
        return n

    a = 0
    b = 1
    c = 1
    for _ in range(n - 1):
        c = a + b
        a = b
        b = c
    return c