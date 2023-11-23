import pytest
from union_find import UnionFind

def test_make_set_and_find():
    uf = UnionFind()
    uf.make_set("apple")
    uf.make_set("banana")
    assert uf.find("apple") == "apple"
    assert uf.find("banana") == "banana"

    with pytest.raises(KeyError):
        uf.find("cherry")

def test_union_and_connected():
    uf = UnionFind()
    uf.make_set("apple")
    uf.make_set("banana")
    uf.make_set("cherry")

    uf.union("apple", "banana")
    assert uf.connected("apple", "banana")
    assert uf.connected("banana", "apple")
    assert not uf.connected("apple", "cherry")
    assert not uf.connected("banana", "cherry")

    uf.union("banana", "cherry")
    assert uf.connected("apple", "cherry")

def test_union_rank():
    uf = UnionFind()
    uf.make_set("apple")
    uf.make_set("banana")
    uf.make_set("cherry")

    uf.union("apple", "banana")
    uf.union("banana", "cherry")

    # Assuming internal rank representation, "banana" or "apple" should be the root
    assert uf.find("cherry") in {"apple", "banana"}

def test_invalid_union():
    uf = UnionFind()
    uf.make_set("apple")

    with pytest.raises(KeyError):
        uf.union("apple", "banana")

def test_large_tree():
    uf = UnionFind()
    num_nodes = 100
    elements = ["node" + str(i) for i in range(num_nodes)]

    # Add all elements to the Union-Find structure
    for elem in elements:
        uf.make_set(elem)

    # Union the elements sequentially: node0 with node1, node1 with node2, etc.
    for i in range(num_nodes - 1):
        uf.union(elements[i], elements[i + 1])

    # Check if all elements are connected to the first element
    for i in range(1, num_nodes):
        assert uf.connected(elements[0], elements[i])

    # The root of all elements should be the root of the first element
    first_element_root = uf.find(elements[0])
    for i in range(1, num_nodes):
        assert uf.find(elements[i]) == first_element_root

