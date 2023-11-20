from binary_tree import BinaryTree, Node
from typing import Optional

class BinarySearchTree(BinaryTree):
    def insert(self, node: Node):
        """
        Insert a new node into the BST. Raises ValueError if a node with the same key already exists.

        Parameters:
            node (Node): The node to be inserted into the BST.

        Example:
        >>> bst = BinarySearchTree()
        >>> bst.insert(Node(10))
        >>> bst.root.key
        10
        """
        if self.root is None:
            self.root = node
        else:
            self.insert_subtree(self.root, node)

    def insert_subtree(self, root: Node, node: Node):
        """
        Recursively insert a new node into the subtree rooted at the given root.

        Parameters:
            root (Node): The root node of the subtree where the new node is to be inserted.
            node (Node): The node to be inserted.
        """
        if node.key < root.key:
            if root.left is None:
                self.insert_before(root, node)
            else:
                self.insert_subtree(root.left, node)
        elif node.key > root.key:
            if root.right is None:
                self.insert_after(root, node)
            else:
                self.insert_subtree(root.right, node)
        else:
            raise ValueError('Duplicate key')

    def search(self, key: int) -> Optional[Node]:
        """
        Search for a node by its key in the BST.

        Parameters:
            key (int): The key of the node to search for.

        Returns:
            Optional[Node]: The node with the given key, or None if not found.

        Example:
        >>> bst = BinarySearchTree()
        >>> bst.insert(Node(10))
        >>> bst.insert(Node(15))
        >>> bst.search(15).key
        15
        >>> bst.search(20)
        None
        """
        return self.search_subtree(self.root, key)

    def search_subtree(self, node: Optional[Node], key: int) -> Optional[Node]:
        """
        Recursively search for a node by its key in the subtree rooted at the given node.

        Parameters:
            node (Optional[Node]): The root node of the subtree to search within.
            key (int): The key of the node to search for.

        Returns:
            Optional[Node]: The node with the given key, or None if not found.
        """
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self.search_subtree(node.left, key)
        else:
            return self.search_subtree(node.right, key)

    def rotate_right(self, node: Node):
        r"""
        Rotate the subtree rooted at the given node to the right.

        Parameters:
            node (Node): The root node of the subtree to rotate.
                    Y                      X
                   / \                    / \
                  X   C                  A   Y
                 / \           -->          / \
                A   B                      B   C
        """
        y = node
        x = node.left
        if not x:
            raise ValueError('Node has no left child')

        # Turn x's right subtree into y's left subtree
        y.left = x.right

        # If x's right subtree is not empty, set its parent to y
        if x.right:
            x.right.parent = y

        # Link y's parent to x
        x.parent = y.parent

        # If y is the root, set x to be the new root
        if not y.parent:
            self.root = x
        elif y == y.parent.right:
            # If y is the right child of its parent, set x to be the new right child
            y.parent.right = x
        else:
            # If y is the left child of its parent, set x to be the new left child
            y.parent.left = x

        # Put y on x's right
        x.right = y
        y.parent = x

    def rotate_left(self, node: Node):
        r"""
        Rotate the subtree rooted at the given node to the left.

        Parameters:
            node (Node): The root node of the subtree to rotate.
                    X                      Y
                   / \                    / \
                  A   Y                  X   C
                     / \      -->       / \
                    B   C              A   B
        """
        x = node
        y = node.right
        if not y:
            raise ValueError('Node has no right child')

        # Turn y's left subtree into x's right subtree
        x.right = y.left

        # If y's left subtree is not empty, set its parent to x
        if y.left:
            y.left.parent = x

        # Link x's parent to y
        y.parent = x.parent

        # If x is the root, set y to be the new root
        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            # If x is the left child of its parent, set y to be the new left child
            x.parent.left = y
        else:
            # If x is the right child of its parent, set y to be the new right child
            x.parent.right = y

        # Put x on y's left
        y.left = x
        x.parent = y