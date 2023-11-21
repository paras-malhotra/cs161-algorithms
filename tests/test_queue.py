from linked_queue import Queue

def test_queue_operations():
    q = Queue()
    assert q.is_empty() == True
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert str(q) == "1 -> 2 -> 3"
    assert q.dequeue() == 1
    assert q.peek() == 2
    assert q.is_empty() == False
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.dequeue() is None
    assert q.is_empty() == True

def test_queue_with_strings():
    q = Queue()
    q.enqueue("a")
    q.enqueue("b")
    q.enqueue("c")
    assert str(q) == "a -> b -> c"
    assert q.is_empty() == False
    assert q.peek() == "a"
    assert q.dequeue() == "a"
    assert q.dequeue() == "b"
    assert q.dequeue() == "c"
    assert q.dequeue() is None
    assert q.is_empty() == True