import pytest
from binary_search_tree import BinarySearchTree, Node

# Test insertion into the BST
def test_bst_insertion():
    bst = BinarySearchTree()
    bst.insert(Node(10))
    bst.insert(Node(5))
    bst.insert(Node(15))
    assert bst.inorder_traversal() == [5, 10, 15]

# Test insertion of duplicate key
def test_bst_insertion_duplicate():
    bst = BinarySearchTree()
    bst.insert(Node(10))
    with pytest.raises(ValueError):
        bst.insert(Node(10))

# Test searching in the BST
def test_bst_search():
    bst = BinarySearchTree()
    bst.insert(Node(10))
    bst.insert(Node(5))
    bst.insert(Node(15))
    assert bst.search(5).key == 5
    assert bst.search(15).key == 15
    assert bst.search(10).key == 10
    assert bst.search(20) is None

# Test right rotation
def test_right_rotation():
    bst = BinarySearchTree()
    bst.insert(Node(10))
    bst.insert(Node(5))
    bst.insert(Node(3))
    left_height = bst.height_subtree(bst.root.left)
    right_height = bst.height_subtree(bst.root.right)
    # Perform right rotation at root
    bst.rotate_right(bst.root)
    new_left_height = bst.height_subtree(bst.root.left)
    new_right_height = bst.height_subtree(bst.root.right)
    assert new_right_height == right_height + 1
    assert new_left_height == left_height - 1
    assert bst.inorder_traversal() == [3, 5, 10]

# Test left rotation
def test_left_rotation():
    bst = BinarySearchTree()
    bst.insert(Node(10))
    bst.insert(Node(15))
    bst.insert(Node(20))
    left_height = bst.height_subtree(bst.root.left)
    right_height = bst.height_subtree(bst.root.right)
    # Perform left rotation at root
    bst.rotate_left(bst.root)
    new_left_height = bst.height_subtree(bst.root.left)
    new_right_height = bst.height_subtree(bst.root.right)
    assert new_right_height == right_height - 1
    assert new_left_height == left_height + 1
    assert bst.inorder_traversal() == [10, 15, 20]