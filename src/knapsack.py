from typing import List

def unbounded_knapsack(budget: int, weights: List[int], values: List[int]) -> int:
    """
    Solve the unbounded knapsack problem using dynamic programming.

    Parameters:
        budget (int): The budget of the knapsack.
        weights (List[int]): The weights of the items.
        values (List[int]): The values of the items.

    Returns:
        int: The maximum total value of items that can be put in the knapsack.

    Time complexity: O(nW) where n is the number of items and W is the budget.
    Space complexity: O(W) where W is the budget.

    Examples:
        >>> unbounded_knapsack(10, [6, 3, 4, 2], [30, 14, 16, 9])
        48
        >>> unbounded_knapsack(15, [6, 3, 4, 2], [30, 14, 16, 9])
        74
        >>> unbounded_knapsack(10, [3, 4, 2], [14, 16, 9])
        46
    """
    n = len(weights)
    maxValues = [0 for _ in range(budget + 1)]

    for i in range(budget + 1):
        for j in range(n):
            if weights[j] <= i:
                maxValues[i] = max(maxValues[i], maxValues[i - weights[j]] + values[j])

    return maxValues[budget]

def zero_one_knapsack(budget: int, weights: List[int], values: List[int]) -> int:
    """
    Solve the 0-1 knapsack problem using dynamic programming.

    Parameters:
        budget (int): The budget of the knapsack.
        weights (List[int]): The weights of the items.
        values (List[int]): The values of the items.

    Returns:
        int: The maximum total value of items that can be put in the knapsack.

    Time complexity: O(nW) where n is the number of items and W is the budget.
    Space complexity: O(nW) where n is the number of items and W is the budget.

    Examples:
        >>> zero_one_knapsack(10, [6, 3, 4, 2], [30, 14, 16, 9])
        46
        >>> zero_one_knapsack(15, [6, 3, 4, 2], [30, 14, 16, 9])
        69
        >>> zero_one_knapsack(10, [3, 4, 2, 6, 5], [14, 16, 9, 30, 50])
        73
    """
    n = len(weights)
    maxValues = [[0 for _ in range(n + 1)] for _ in range(budget + 1)]

    for i in range(budget + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                maxValues[i][j] = 0
            elif weights[j - 1] <= i:
                maxValues[i][j] = max(maxValues[i][j - 1], maxValues[i - weights[j - 1]][j - 1] + values[j - 1])
            else:
                maxValues[i][j] = maxValues[i][j - 1]

    return maxValues[budget][n]