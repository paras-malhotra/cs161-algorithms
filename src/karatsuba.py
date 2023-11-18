def karatsuba(x, y):
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