import pytest
from binary_tree import Node, BinaryTree

# Test for BinaryTree initialization
def test_binary_tree_initialization():
    tree = BinaryTree()
    assert tree.root is None

# Test for height of the tree
def test_binary_tree_height():
    tree = create_small_tree()
    tree.root.left.left = Node(4)

    assert tree.height() == 3

# Test for size of the tree
def test_binary_tree_size():
    tree = create_small_tree()

    assert tree.size() == 3

# Test for inorder traversal
def test_inorder_traversal():
    tree = create_small_tree()
    assert tree.inorder_traversal() == [2, 1, 3]

    # Test with larger tree
    tree = create_large_tree()
    assert tree.inorder_traversal() == [4, 2, 5, 1, 6, 3, 7]

# Test for preorder traversal
def test_preorder_traversal():
    tree = create_small_tree()
    assert tree.preorder_traversal() == [1, 2, 3]

    # Test with larger tree
    tree = create_large_tree()
    assert tree.preorder_traversal() == [1, 2, 4, 5, 3, 6, 7]

# Test for postorder traversal
def test_postorder_traversal():
    tree = create_small_tree()
    assert tree.postorder_traversal() == [2, 3, 1]

    # Test with larger tree
    tree = create_large_tree()
    assert tree.postorder_traversal() == [4, 5, 2, 6, 7, 3, 1]

# Helper function to create a small tree for testing
def create_small_tree() -> BinaryTree:
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    return tree

# Helper function to create a larger tree for testing
def create_large_tree() -> BinaryTree:
    tree = create_small_tree()
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    return tree
