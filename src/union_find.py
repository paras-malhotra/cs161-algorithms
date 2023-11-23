from typing import TypeVar, Dict

T = TypeVar('T')

class UnionFind:
    def __init__(self):
        """
        Initializes the Union-Find structure. The structure starts empty and elements are added as needed.

        Time complexity: O(1)
        """
        # Map each element to its root
        self.root: Dict[T, T] = {}

        # Map each element to its rank
        self.rank: Dict[T, int] = {}

    def make_set(self, x: T) -> None:
        """
        Creates a new set containing only the specified element x. Does nothing if the element already exists.

        Time complexity: O(1)

        Parameters:
            x (T): The element to create a set for.
        """
        if x not in self.root:
            self.root[x] = x
            self.rank[x] = 1

    def find(self, x: T) -> T:
        """
        Finds the root of the set that the element x is a part of. Implements path compression. Raises KeyError if the element is not found.

        Parameters:
            x (T): The element to find the root of.

        Returns:
            T: The root of the set that contains x.

        Time complexity: O(α(n)), where α(n) is the inverse Ackermann function, effectively constant.
        """
        if x not in self.root:
            raise KeyError("Element not found in the Union-Find structure.")

        if x != self.root[x]:
            # Path compression
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x: T, y: T) -> None:
        """
        Merges the set that contains x and the set that contains y (if they are different).

        Parameters:
            x (T): An element of the first set.
            y (T): An element of the second set.

        Time complexity: O(α(n)), where α(n) is the inverse Ackermann function, effectively constant.
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1

    def connected(self, x: T, y: T) -> bool:
        """
        Checks if elements x and y are in the same set.

        Parameters:
            x (T): The first element.
            y (T): The second element.

        Returns:
            bool: True if x and y are in the same set, False otherwise.

        Time complexity: O(α(n)), where α(n) is the inverse Ackermann function, effectively constant.
        """
        return self.find(x) == self.find(y)