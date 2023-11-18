from radix_sort import radix_sort

def test_radix_sort_basic():
    assert radix_sort([52, 3, 1, 18, 4, 1, 15]) == [1, 1, 3, 4, 15, 18, 52]

def test_radix_sort_large_numbers():
    assert radix_sort([123, 1, 456, 12, 789]) == [1, 12, 123, 456, 789]

def test_radix_sort_with_different_base():
    assert radix_sort([3, 1, 4, 1, 5], 2, 3) == [1, 1, 3, 4, 5]