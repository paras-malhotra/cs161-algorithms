from typing import Optional, List
from tree_node import Node

class BinaryTree:
    def __init__(self):
        """ Initialize an empty binary tree. """
        self.root: Optional[Node] = None

    def height(self) -> int:
        """ Return the height of the tree. """
        return self.height_subtree(self.root)
    
    def height_subtree(self, node: Optional[Node]) -> int:
        """ Return the height of the subtree rooted at the given node. """
        if node is None:
            return 0
        return 1 + max(self.height_subtree(node.left), self.height_subtree(node.right))
    
    def depth_node(self, node: Optional[Node]) -> int:
        """ Return the depth of the given node. """
        if node is None:
            return 0
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
        result = []
        self._inorder_traversal_recursive(self.root, result)
        return result
    
    def preorder_traversal(self) -> List[int]:
        """ Perform pre-order traversal of the tree. """
        result = []
        self._preorder_traversal_recursive(self.root, result)
        return result
    
    def postorder_traversal(self) -> List[int]:
        """ Perform post-order traversal of the tree. """
        result = []
        self._postorder_traversal_recursive(self.root, result)
        return result
    
    def _inorder_traversal_recursive(self, node: Optional[Node], result: List[int]):
        """ Helper method for in-order traversal. """
        if node is not None:
            self._inorder_traversal_recursive(node.left, result)
            result.append(node.key)
            self._inorder_traversal_recursive(node.right, result)

    def _preorder_traversal_recursive(self, node: Optional[Node], result: List[int]):
        """ Helper method for pre-order traversal. """
        if node is not None:
            result.append(node.key)
            self._preorder_traversal_recursive(node.left, result)
            self._preorder_traversal_recursive(node.right, result)

    def _postorder_traversal_recursive(self, node: Optional[Node], result: List[int]):
        """ Helper method for post-order traversal. """
        if node is not None:
            self._postorder_traversal_recursive(node.left, result)
            self._postorder_traversal_recursive(node.right, result)
            result.append(node.key)