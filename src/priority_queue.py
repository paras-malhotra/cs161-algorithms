from typing import Dict, Optional, TypeVar
from binary_heap import MinHeap

T = TypeVar('T')

class PriorityQueue(MinHeap):
    """
    A priority queue implemented as a min heap.
    This class extends the MinHeap and provides additional functionality
    needed for algorithms like Dijkstra's.
    """

    def __init__(self):
        super().__init__()
        self.position_map: Dict[T, int] = {}

    def insert(self, item: T):
        """
        Inserts an item into the priority queue.
        Updates the position map for the new item.
        """
        self.position_map[item] = len(self.heap)
        super().insert(item)

    def decrease_key(self, item: T, new_value: T):
        """
        Decreases the key (value) of an item in the priority queue.

        Parameters:
            item (T): The item whose key is to be decreased.
            new_value (T): The new value for the key.
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
        Extracts the minimum item from the priority queue.
        Updates the position map accordingly.
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
        """
        self.position_map[self.heap[i]] = j
        self.position_map[self.heap[j]] = i
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]