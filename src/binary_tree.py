from typing import Optional, List
from tree_node import Node

class BinaryTree:
    def __init__(self, root: Optional[Node] = None):
        """ Initialize an empty binary tree. """
        self.root: Optional[Node] = root

    def height(self) -> int:
        """ Return the height of the tree. """
        return self.height_subtree(self.root)
    
    def height_subtree(self, node: Optional[Node]) -> int:
        """ Return the height of the subtree rooted at the given node. """
        if node is None:
            return -1
        return 1 + max(self.height_subtree(node.left), self.height_subtree(node.right))
    
    def depth_node(self, node: Optional[Node]) -> int:
        """ Return the depth of the given node. """
        if node is None:
            return -1
        return 1 + self.depth_node(node.parent)
    
    def size(self) -> int:
        """ Return the number of nodes in the tree. """
        return self.size_subtree(self.root)

    def size_subtree(self, node: Optional[Node]) -> int:
        """ Return the number of nodes in the subtree rooted at the given node. """
        if node is None:
            return 0
        return 1 + self.size_subtree(node.left) + self.size_subtree(node.right)

    def inorder_traversal(self) -> List[int]:
        """ Perform in-order traversal of the tree. """
        return [node.key for node in self._inorder_traversal_generator(self.root)]
    
    def preorder_traversal(self) -> List[int]:
        """ Perform pre-order traversal of the tree. """
        return [node.key for node in self._preorder_traversal_generator(self.root)]
    
    def postorder_traversal(self) -> List[int]:
        """ Perform post-order traversal of the tree. """
        return [node.key for node in self._postorder_traversal_generator(self.root)]
    
    def successor(self, node: Node) -> Optional[Node]:
        """
        Find the successor of the given node in the tree.
        """
        # The successor is the smallest key greater than node.key
        if node.right:
            return self.subtree_first(node.right)
        # If no right subtree, the successor is one of the ancestors
        while node.parent and node == node.parent.right:
            node = node.parent
        return node.parent

    def predecessor(self, node: Node) -> Optional[Node]:
        """
        Find the predecessor of the given node in the tree.
        """
        # The predecessor is the largest key smaller than node.key
        if node.left:
            return self.subtree_last(node.left)
        # If no left subtree, the predecessor is one of the ancestors
        while node.parent and node == node.parent.left:
            node = node.parent
        return node.parent

    def subtree_first(self, node: Node) -> Node:
        """
        Find the first node (in-order) in the subtree rooted at the given node.
        """
        current = node
        while current.left is not None:
            current = current.left
        return current

    def subtree_last(self, node: Node) -> Node:
        """
        Find the last node (in-order) in the subtree rooted at the given node.
        """
        current = node
        while current.right is not None:
            current = current.right
        return current

    def insert_after(self, node: Node, new_node: Node):
        """
        Insert a new node after the given node.
        """
        if node.right is None:
            node.right = new_node
            new_node.parent = node
        else:
            self.insert_before(self.subtree_first(node.right), new_node)

    def insert_before(self, node: Node, new_node: Node):
        """
        Insert a new node before the given node.
        """
        if node.left is None:
            node.left = new_node
            new_node.parent = node
        else:
            self.insert_after(self.subtree_last(node.left), new_node)

    def delete(self, node: Node):
        """
        Delete the given node from the tree.
        """
        # if node is the root and has no children, simply remove it
        if node.parent is None and node.left is None and node.right is None:
            self.root = None
            return

        # if node is a leaf, simply remove it
        if node.left is None and node.right is None:
            if node.parent.left == node:
                node.parent.left = None
            else:
                node.parent.right = None
        else:
            # else if node has a left child, swap it with its predecessor and delete the predecessor
            if node.left is not None:
                predecessor = self.predecessor(node)
                node.key = predecessor.key
                self.delete(predecessor)
            # else if node has a right child, swap it with its successor and delete the successor
            else:
                successor = self.successor(node)
                node.key = successor.key
                self.delete(successor)

    def _inorder_traversal_generator(self, node):
        """ Generator for in-order traversal. """
        if node is not None:
            yield from self._inorder_traversal_generator(node.left)
            yield node
            yield from self._inorder_traversal_generator(node.right)

    def _preorder_traversal_generator(self, node):
        """ Generator for pre-order traversal. """
        if node is not None:
            yield node
            yield from self._preorder_traversal_generator(node.left)
            yield from self._preorder_traversal_generator(node.right)

    def _postorder_traversal_generator(self, node):
        """ Generator for post-order traversal. """
        if node is not None:
            yield from self._postorder_traversal_generator(node.left)
            yield from self._postorder_traversal_generator(node.right)
            yield node

    def __iter__(self):
        """ Iterator for in-order traversal of the tree. """
        return (node.key for node in self._inorder_traversal_generator(self.root))