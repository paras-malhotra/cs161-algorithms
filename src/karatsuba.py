def karatsuba(x: int, y: int) -> int:
    """
    Perform multiplication using the Karatsuba algorithm.

    The Karatsuba algorithm is a divide-and-conquer algorithm that
    multiplies two numbers more efficiently than the traditional 
    approach. It's particularly useful for large numbers.

    Parameters:
    x (int): The first integer to multiply.
    y (int): The second integer to multiply.

    Returns:
    int: The product of x and y.

    Time Complexity:
    O(n^log2(3)) ≈ O(n^1.585), where n is the number of digits in the larger number.

    Example:
    >>> karatsuba(1234, 5678)
    7006652
    """
    # Base case
    if x < 10 and y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    m = n // 2

    # Splitting x = 10**(n/2) * a + b and y = 10**(n/2) * c + d
    a = x // 10**m
    b = x % 10**m
    c = y // 10**m
    d = y % 10**m

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_plus_bc = karatsuba(a + b, c + d) - ac - bd

    # x * y = 10**n * ac + 10**(n/2) * (ad + bc) + bd
    return ac * 10**(2*m) + (ad_plus_bc * 10**m) + bd