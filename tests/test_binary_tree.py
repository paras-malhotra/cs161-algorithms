from binary_tree import Node, BinaryTree

# Test for BinaryTree initialization
def test_binary_tree_initialization():
    tree = BinaryTree()
    assert tree.root is None

# Test for tree height and node depth
def test_binary_tree_height_and_depth():
    tree = create_small_tree()
    tree.insert_before(tree.root.left, Node(4))

    assert tree.height() == 2
    assert tree.depth_node(tree.root.left.left) == 2

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

# Test for finding the successor of a node
def test_successor():
    tree = create_large_tree()
    assert tree.successor(tree.root).key == 6
    assert tree.successor(tree.root.left.right).key == 1

# Test for finding the predecessor of a node
def test_predecessor():
    tree = create_large_tree()
    assert tree.predecessor(tree.root).key == 5
    assert tree.predecessor(tree.root.left.left) == None

# Test for finding the first node in a subtree
def test_subtree_first():
    tree = create_large_tree()
    assert tree.subtree_first(tree.root).key == 4
    assert tree.subtree_first(tree.root.right).key == 6

# Test for finding the last node in a subtree
def test_subtree_last():
    tree = create_large_tree()
    assert tree.subtree_last(tree.root).key == 7
    assert tree.subtree_last(tree.root.left).key == 5

def test_insert_after():
    tree = create_small_tree()
    new_node = Node(4)
    tree.insert_after(tree.root, new_node)
    assert tree.size() == 4
    assert tree.inorder_traversal() == [2, 1, 4, 3]

    tree.insert_after(tree.root.right, Node(5))
    assert tree.size() == 5
    assert tree.inorder_traversal() == [2, 1, 4, 3, 5]

def test_insert_before():
    tree = create_small_tree()
    new_node = Node(0)
    tree.insert_before(tree.root.left, new_node)
    assert tree.size() == 4
    assert tree.inorder_traversal() == [0, 2, 1, 3]

    tree.insert_before(tree.root.left, Node(-1))
    assert tree.size() == 5
    assert tree.inorder_traversal() == [0, -1, 2, 1, 3]

# Test deletion of a leaf node
def test_delete_leaf_node():
    tree = create_small_tree()
    leaf_node = tree.root.left
    tree.delete(leaf_node)
    assert tree.root.left is None
    assert tree.size() == 2
    assert tree.inorder_traversal() == [1, 3]

# Test deletion of a node with one child
def test_delete_node_with_one_child():
    tree = create_small_tree()
    tree.insert_before(tree.root.left, Node(4))
    node_with_one_child = tree.root.left
    assert tree.root.left.key == 2
    tree.delete(node_with_one_child)
    # Check if the tree structure is maintained correctly
    assert tree.size() == 3
    assert tree.inorder_traversal() == [4, 1, 3]

# Test deletion of a node with two children
def test_delete_node_with_two_children():
    tree = create_large_tree()
    node_with_two_children = tree.root
    tree.delete(node_with_two_children)
    # Check if the tree structure is maintained correctly
    assert tree.size() == 6
    assert tree.inorder_traversal() == [4, 2, 5, 6, 3, 7]

# Helper function to create a small tree for testing
r"""
    1
   / \
  2   3
"""
def create_small_tree() -> BinaryTree:
    tree = BinaryTree()
    tree.root = Node(1)
    tree.insert_before(tree.root, Node(2))
    tree.insert_after(tree.root, Node(3))
    return tree

# Helper function to create a larger tree for testing
r"""
       1
      / \
     2   3
    / \ / \
   4  5 6  7
"""
def create_large_tree() -> BinaryTree:
    tree = create_small_tree()
    tree.insert_before(tree.root.left, Node(4))
    tree.insert_after(tree.root.left, Node(5))
    tree.insert_before(tree.root.right, Node(6))
    tree.insert_after(tree.root.right, Node(7))
    return tree
