from binary_heap import BinaryHeap, MinHeap, MaxHeap

def test_min_heap():
    heap = MinHeap()
    heap.insert(3)
    heap.insert(1)
    heap.insert(4)
    assert heap.extract_min() == 1
    assert heap.extract_min() == 3
    assert heap.extract_min() == 4

def test_min_heap_peek():
    heap = MinHeap()
    heap.insert(3)
    assert heap.peek() == 3
    heap.insert(1)
    assert heap.peek() == 1
    heap.insert(2)
    assert heap.peek() == 1

def test_min_heap_size():
    heap = MinHeap()
    assert heap.size() == 0
    heap.insert(3)
    assert heap.size() == 1
    heap.insert(1)
    assert heap.size() == 2

def test_min_heap_build():
    heap = MinHeap()
    heap.build([3, 1, 4, 2])
    assert heap.extract_min() == 1
    assert heap.extract_min() == 2
    assert heap.extract_min() == 3
    assert heap.extract_min() == 4

def test_max_heap():
    heap = MaxHeap()
    heap.insert(3)
    heap.insert(1)
    heap.insert(4)
    assert heap.extract_max() == 4
    assert heap.extract_max() == 3
    assert heap.extract_max() == 1

def test_max_heap_peek():
    heap = MaxHeap()
    heap.insert(1)
    assert heap.peek() == 1
    heap.insert(3)
    assert heap.peek() == 3
    heap.insert(2)
    assert heap.peek() == 3

def test_max_heap_size():
    heap = MaxHeap()
    assert heap.size() == 0
    heap.insert(3)
    assert heap.size() == 1
    heap.insert(1)
    assert heap.size() == 2

def test_max_heap_build():
    heap = MaxHeap()
    heap.build([3, 1, 4, 2])
    assert heap.extract_max() == 4
    assert heap.extract_max() == 3
    assert heap.extract_max() == 2
    assert heap.extract_max() == 1

