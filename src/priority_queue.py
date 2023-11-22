from typing import Dict, Optional, TypeVar
from binary_heap import MinHeap

T = TypeVar('T')

class PriorityQueue(MinHeap):
    """
    Priority queue implemented as a binary heap. Note that this implementation is not as efficient as a Fibonacci heap for Dijkstra's algorithm.
    """

    def __init__(self):
        super().__init__()
        self.position_map: Dict[T, int] = {}

    def insert(self, item: T):
        """
        Inserts an item into the priority queue and updates the position map for the new item.

        Time complexity: O(log n) where n is the number of items in the priority queue.
        """
        self.position_map[item] = len(self.heap)
        super().insert(item)

    def decrease_key(self, item: T, new_value: T):
        """
        Decreases the key (value) of an item in the priority queue.

        Parameters:
            item (T): The item whose key is to be decreased.
            new_value (T): The new value for the key.

        Time complexity: O(log n) where n is the number of items in the priority queue.
        """
        if item not in self.position_map:
            raise ValueError("Invalid operation")

        if self.comparator(item, new_value):
            # The new value is greater than the current value, so we don't need to do anything
            return

        index = self.position_map[item]
        self.heap[index] = new_value
        self.position_map[new_value] = index
        del self.position_map[item]
        self.heapify_up(index)

    def extract_min(self) -> T:
        """
        Extracts the minimum item from the priority queue and updates the position map accordingly.

        Time complexity: O(log n) where n is the number of items in the priority queue.
        """
        if self.size() == 0:
            raise IndexError("Extract from empty heap")

        del self.position_map[self.peek()]
        min = super().extract_min()
        if self.size() > 0:
            self.position_map[self.peek()] = 0
        return min

    def swap(self, i: int, j: int):
        """
        Swaps two elements in the heap using their indices.

        Time complexity: O(1)
        """
        self.position_map[self.heap[i]] = j
        self.position_map[self.heap[j]] = i
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]