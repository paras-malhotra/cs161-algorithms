from karatsuba import karatsuba

def test_karatsuba_small_numbers():
    assert karatsuba(1234, 5678) == 1234 * 5678

def test_karatsuba_large_numbers():
    assert karatsuba(12345678, 87654321) == 12345678 * 87654321

def test_karatsuba_unequal_length():
    assert karatsuba(12345, 678) == 12345 * 678

def test_karatsuba_with_zero():
    assert karatsuba(12345, 0) == 0

def test_karatsuba_single_digit():
    assert karatsuba(7, 8) == 56

def test_karatsuba_negative_numbers():
    assert karatsuba(-1234, 5678) == -1234 * 5678
    assert karatsuba(1234, -5678) == 1234 * -5678
    assert karatsuba(-1234, -5678) == 1234 * 5678