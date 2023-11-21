from linked_list import LinkedList

def test_prepend_and_str():
    ll = LinkedList()
    ll.prepend(3)
    ll.prepend(2)
    ll.prepend(1)
    assert str(ll) == "1 -> 2 -> 3"
    assert ll.head.data == 1
    assert ll.tail.data == 3

def test_append_and_str():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert str(ll) == "1 -> 2 -> 3"
    assert ll.head.data == 1
    assert ll.tail.data == 3

def test_delete_first():
    ll = LinkedList()
    ll.prepend(3)
    ll.prepend(2)
    ll.prepend(1)
    ll.delete_first()
    assert str(ll) == "2 -> 3"
    assert ll.head.data == 2
    assert ll.tail.data == 3
    ll.delete_first()
    assert ll.head.data == 3
    assert ll.tail.data == 3
    assert str(ll) == "3"
    ll.delete_first()
    assert str(ll) == ""
    assert ll.head is None
    assert ll.tail is None

def test_peek():
    ll = LinkedList()
    assert ll.peek() is None
    ll.prepend(1)
    assert ll.peek() == 1
    ll.prepend(2)
    assert ll.peek() == 2

def test_iteration():
    ll = LinkedList()
    ll.prepend(3)
    ll.prepend(2)
    ll.prepend(1)
    ll.append(4)
    elements = [element.data for element in ll]
    assert elements == [1, 2, 3, 4]
    assert ll.head.data == 1
    assert ll.tail.data == 4

def test_empty_list():
    ll = LinkedList()
    assert str(ll) == ""
    assert ll.peek() is None
    assert [element for element in ll] == []

def test_string_elements():
    ll = LinkedList()
    ll.prepend("a")
    ll.prepend("b")
    ll.prepend("c")
    ll.append("d")
    assert str(ll) == "c -> b -> a -> d"
    assert ll.peek() == "c"
    assert [element.data for element in ll] == ["c", "b", "a", "d"]
    assert ll.head.data == "c"
    assert ll.tail.data == "d"
