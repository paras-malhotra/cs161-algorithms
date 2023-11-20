import pytest
from itertools import product
from avl_tree import AVLTree
from binary_tree import Node

# Define self balancing tree classes and test data
self_balancing_bst_classes = [AVLTree]
insertion_test_cases = [
    ([10, 20, 30, 40, 50, 25], [10, 20, 25, 30, 40, 50]),
    ([50, 40, 30, 20, 10, 25], [10, 20, 25, 30, 40, 50]),
    ([10, 50, 30, 20, 25, 40], [10, 20, 25, 30, 40, 50]),
    # Add more test data here
]

deletion_test_cases = [
    ([10, 20, 30, 40, 50, 25], 30, [10, 20, 25, 40, 50]),
    ([50, 40, 30, 20, 10, 25], 30, [10, 20, 25, 40, 50]),
    ([10, 50, 30, 20, 25, 40], 30, [10, 20, 25, 40, 50]),
    # Add more test data here
]

combined_test_cases_insertion = product(self_balancing_bst_classes, insertion_test_cases)
prepared_test_cases_insertion = [(tree_class, *nodes_and_expected_inorder) for tree_class, nodes_and_expected_inorder in combined_test_cases_insertion]

combined_test_cases_deletion = product(self_balancing_bst_classes, deletion_test_cases)
prepared_test_cases_deletion = [(tree_class, nodes, delete_key, expected_inorder) for tree_class, (nodes, delete_key, expected_inorder) in combined_test_cases_deletion]

# Test for Self-Balancing Tree Insertion and Auto-Balancing
@pytest.mark.parametrize("tree_class, nodes, expected_inorder", prepared_test_cases_insertion)
def test_tree_insertion(tree_class, nodes, expected_inorder):
    tree = tree_class()
    for key in nodes:
        tree.insert(Node(key))

    # Check if the tree is balanced
    assert tree.is_balanced()
    assert tree.inorder_traversal() == expected_inorder
    assert abs(tree.height_subtree(tree.root.right) - tree.height_subtree(tree.root.left)) <= 1

# Test for Self-Balancing Tree Deletion and Auto-Balancing
@pytest.mark.parametrize("tree_class, nodes, delete_key, expected_inorder", prepared_test_cases_deletion)
def test_tree_deletion(tree_class, nodes, delete_key, expected_inorder):
    tree = tree_class()
    for key in nodes:
        tree.insert(Node(key))

    tree.delete_by_key(delete_key)

    # Check if the tree remains balanced after deletion
    assert tree.is_balanced()
    assert tree.inorder_traversal() == expected_inorder
    assert abs(tree.height_subtree(tree.root.right) - tree.height_subtree(tree.root.left)) <= 1
