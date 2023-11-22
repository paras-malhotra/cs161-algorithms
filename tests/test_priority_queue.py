import pytest
from priority_queue import PriorityQueue

def test_insert_and_extract_min():
    pq = PriorityQueue()
    pq.insert(3)
    pq.insert(1)
    pq.insert(4)

    assert pq.extract_min() == 1
    assert pq.extract_min() == 3
    assert pq.extract_min() == 4

    with pytest.raises(IndexError):
        pq.extract_min()  # Attempt to extract from empty queue

def test_decrease_key():
    pq = PriorityQueue()
    pq.insert(3)
    pq.insert(1)
    pq.insert(4)

    pq.decrease_key(3, 0)
    assert pq.extract_min() == 0
    assert pq.extract_min() == 1
    assert pq.extract_min() == 4

    with pytest.raises(ValueError):
        pq.decrease_key(5, 2)  # Decrease key for non-existent item

def test_peek():
    pq = PriorityQueue()
    pq.insert(3)
    pq.insert(1)
    pq.insert(4)

    assert pq.peek() == 1
    pq.extract_min()
    assert pq.peek() == 3

    pq.extract_min()
    pq.extract_min()
    with pytest.raises(IndexError):
        pq.peek()  # Peek from empty queue

def test_heap_order():
    pq = PriorityQueue()
    pq.insert(3)
    pq.insert(1)
    pq.insert(4)
    pq.insert(2)

    assert pq.extract_min() == 1
    assert pq.extract_min() == 2
    assert pq.extract_min() == 3
    assert pq.extract_min() == 4

def test_size():
    pq = PriorityQueue()
    assert pq.size() == 0

    pq.insert(3)
    pq.insert(1)
    assert pq.size() == 2

    pq.extract_min()
    assert pq.size() == 1

    pq.extract_min()
    assert pq.size() == 0

def test_insert_duplicate():
    pq = PriorityQueue()
    pq.insert(3)
    pq.insert(5)
    pq.insert(3)

    assert pq.extract_min() == 3
    assert pq.extract_min() == 3
    assert pq.extract_min() == 5

def test_increase_key():
    pq = PriorityQueue()
    pq.insert(2)
    pq.insert(3)

    pq.decrease_key(2, 4) # should do nothing
    assert pq.extract_min() == 2
    assert pq.extract_min() == 3

def test_decrease_key_non_existent():
    pq = PriorityQueue()
    pq.insert(2)
    pq.insert(3)

    with pytest.raises(ValueError):
        pq.decrease_key(4, 1)  # Decrease key of a non-existent element

def test_empty_heap_operations():
    pq = PriorityQueue()

    with pytest.raises(IndexError):
        pq.extract_min()  # Extracting from an empty queue

    assert pq.size() == 0

    with pytest.raises(IndexError):
        pq.peek()  # Peeking into an empty queue

def test_heap_order_after_key_decrease():
    pq = PriorityQueue()
    pq.insert(5)
    pq.insert(6)
    pq.insert(7)
    pq.insert(8)
    pq.decrease_key(7, 1)

    assert pq.extract_min() == 1
    assert pq.extract_min() == 5
    assert pq.extract_min() == 6
    assert pq.extract_min() == 8

def test_multiple_operations():
    pq = PriorityQueue()
    for i in range(10, 0, -1):
        pq.insert(i)

    pq.decrease_key(8, 0)
    pq.decrease_key(6, 3)
    assert pq.extract_min() == 0
    assert pq.extract_min() == 1
    assert pq.extract_min() == 2
    assert pq.extract_min() == 3

    while pq.size() > 0:
        pq.extract_min()

    assert pq.size() == 0

    with pytest.raises(IndexError):
        pq.extract_min()  # Extract from an empty heap again