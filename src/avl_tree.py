from binary_search_tree import BinarySearchTree, Node
from binary_tree import Node

class AVLTree(BinarySearchTree):
    def update_heights(self, node: Node):
        """
        Update the heights of the nodes in the subtree rooted at the given node.
        """
        current = node
        while current:
            self.update_height(current)
            current = current.parent

    def update_height(self, node: Node):
        """
        Update the height of the given node.
        """
        node.height = max(node.left.height if node.left else -1, node.right.height if node.right else -1) + 1

    def is_balanced(self) -> bool:
        """
        Check if the tree is balanced.
        """
        return self.is_balanced_subtree(self.root)

    def is_balanced_subtree(self, node: Node) -> bool:
        """
        Check if the subtree rooted at the given node is balanced.
        """
        return abs(self.skew(node)) <= 1

    def skew(self, node: Node) -> bool:
        """
        Get the skew of the given node.
        """
        return (node.right.height if node.right else -1) - (node.left.height if node.left else -1)

    def insert(self, node: Node):
        """
        Insert a new node into the tree.
        """
        super().insert(node)
        self.rebalance(node)

    def delete(self, node: Node):
        """
        Delete the given node from the tree.
        """
        super().delete(node)
        if node.left is None and node.right is None:
            # If the node is a leaf, rebalance the parent node
            self.rebalance(node.parent)
        else:
            # If the node is not a leaf, rebalance the node
            self.rebalance(node)

    def delete_by_key(self, key: int):
        """
        Delete the node with the given key from the tree.
        """
        node = self.search(key)
        self.delete(node)

    def rotate_left(self, node: Node):
        """
        Rotate the subtree rooted at the given node to the left.
        """
        super().rotate_left(node)
        self.update_heights(node)

    def rotate_right(self, node: Node):
        """
        Rotate the subtree rooted at the given node to the right.
        """
        super().rotate_right(node)
        self.update_heights(node)

    def rebalance(self, node: Node):
        """
        Rebalance the tree starting from the given node upwards.
        """
        while node:
            self.update_height(node)
            balance = self.skew(node)

            # Left-Left (LL) Case
            if balance < -1 and self.skew(node.left) <= 0:
                self.rotate_right(node)

            # Right-Right (RR) Case
            elif balance > 1 and self.skew(node.right) >= 0:
                self.rotate_left(node)

            # Left-Right (LR) Case
            elif balance < -1 and self.skew(node.left) > 0:
                self.rotate_left(node.left)
                self.rotate_right(node)

            # Right-Left (RL) Case
            elif balance > 1 and self.skew(node.right) < 0:
                self.rotate_right(node.right)
                self.rotate_left(node)

            # Move to the parent node in case further balancing is required up the tree
            node = node.parent
