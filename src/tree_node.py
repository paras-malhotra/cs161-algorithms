from typing import TypeVar, Optional

class Node:
    def __init__(self, key: int, left: Optional['Node'] = None, right: Optional['Node'] = None, parent: Optional['Node'] = None):
        self.key: int = key
        self.left: Optional['Node'] = left
        self.right: Optional['Node'] = right
        self.parent: Optional['Node'] = parent
        if left is not None:
            left.parent = self
        if right is not None:
            right.parent = self