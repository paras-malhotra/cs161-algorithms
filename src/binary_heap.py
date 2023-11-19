from typing import List, Callable, TypeVar

T = TypeVar('T')

class BinaryHeap:
    """
    A generic binary heap implementation.

    The BinaryHeap can be either a min heap or a max heap, depending on the comparator function provided.

    Attributes:
        heap (List[T]): The heap list where elements are stored.
        comparator (Callable[[T, T], bool]): Function to compare two heap elements.
    """

    def __init__(self, comparator: Callable[[T, T], bool]):
        """
        Initializes the BinaryHeap.

        Parameters:
            comparator (Callable[[T, T], bool]): The comparison function defining the heap order.
        """
        self.heap: List[T] = []
        self.comparator: Callable[[T, T], bool] = comparator

    def parent(self, i: int) -> int:
        """
        Returns the index of the parent of the given index.
        """
        return (i - 1) // 2

    def left_child(self, i: int) -> int:
        """
        Returns the index of the left child of the given index.
        """
        return 2 * i + 1

    def right_child(self, i: int) -> int:
        """
        Returns the index of the right child of the given index.
        """
        return 2 * i + 2

    def has_left_child(self, i: int) -> bool:
        """
        Checks if the given index has a left child.
        """
        return self.left_child(i) < len(self.heap)

    def has_right_child(self, i: int) -> bool:
        """
        Checks if the given index has a right child.
        """
        return self.right_child(i) < len(self.heap)

    def has_parent(self, i: int) -> bool:
        """
        Checks if the given index has a parent.
        """
        return self.parent(i) >= 0

    def swap(self, i: int, j: int):
        """
        Swaps two elements in the heap using their indices.
        """
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, item: T):
        """
        Inserts an item into the heap.

        Parameters:
            item (T): The item to be inserted.

        Running Time:
            O(log n)

        >>> h = BinaryHeap(lambda x, y: x < y)
        >>> h.insert(3)
        >>> h.insert(1)
        >>> h.insert(4)
        >>> h.heap
        [1, 3, 4]
        """
        self.heap.append(item)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, i: int):
        """
        Heapifies (restores heap order) the heap from the given index upwards.

        Parameters:
            i (int): The index to start the heapify from.

        Running Time:
            O(log n)
        """
        while self.has_parent(i) and self.comparator(self.heap[i], self.heap[self.parent(i)]):
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def extract_top(self) -> T:
        """
        Removes and returns the top element from the heap.

        Running Time:
            O(log n)

        Returns:
            T: The top element of the heap.

        >>> h = BinaryHeap(lambda x, y: x < y)
        >>> h.insert(3)
        >>> h.insert(1)
        >>> h.insert(4)
        >>> h.extract_top()
        1
        >>> h.heap
        [3, 4]
        """
        if not self.heap:
            raise IndexError("Extract from empty heap")

        top = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify_down(0)
        return top

    def heapify_down(self, i: int):
        """
        Heapifies (restores heap order) the heap from the given index downwards.

        Parameters:
            i (int): The index to start the heapify from.

        Running Time:
            O(log n)
        """
        while self.has_left_child(i):
            target_child_index = self.left_child(i)
            if self.has_right_child(i) and self.comparator(self.heap[self.right_child(i)], self.heap[target_child_index]):
                target_child_index = self.right_child(i)

            if self.comparator(self.heap[target_child_index], self.heap[i]):
                self.swap(i, target_child_index)
            else:
                break

            i = target_child_index

    def build(self, items: List[T]) -> None:
        """
        Builds a heap from an existing list of items.

        Parameters:
            items (List[T]): A list of items to be turned into a heap.

        Running Time:
            O(n)

        >>> h = BinaryHeap(lambda x, y: x < y)
        >>> h.build([3, 1, 4])
        >>> h.heap
        [1, 3, 4]
        """
        self.heap = items.copy()
        # The nodes with indices [len(self.heap)//2, len(self.heap)) are all leaves, so we start from one level above them
        # The heapify down results in O(n) time complexity as opposed to O(nlogn) if we heapify up
        for i in reversed(range(len(self.heap)//2)):
            self.heapify_down(i)

    def peek(self) -> T:
        """
        Returns the top element of the heap without removing it.

        Running Time:
            O(1)

        Returns:
            T: The top element of the heap.

        >>> h = BinaryHeap(lambda x, y: x < y)
        >>> h.insert(3)
        >>> h.peek()
        3
        >>> h.insert(1)
        >>> h.peek()
        1
        """
        if not self.heap:
            raise IndexError("Peek from empty heap")
        return self.heap[0]

    def size(self) -> int:
        """
        Returns the number of elements in the heap.
        """
        return len(self.heap)

class MinHeap(BinaryHeap):
    """
    MinHeap is a specialized BinaryHeap where the smallest element is always at the top.
    """

    def __init__(self):
        super().__init__(lambda x, y: x < y)

    def extract_min(self) -> T:
        """
        Removes and returns the smallest element from the heap.

        Running Time:
            O(log n)

        Returns:
            T: The smallest element of the heap.

        >>> h = MinHeap()
        >>> h.insert(3)
        >>> h.insert(1)
        >>> h.insert(4)
        >>> h.extract_min()
        1
        >>> h.heap
        [3, 4]
        """
        return self.extract_top()

class MaxHeap(BinaryHeap):
    """
    MaxHeap is a specialized BinaryHeap where the largest element is always at the top.
    """

    def __init__(self):
        super().__init__(lambda x, y: x > y)

    def extract_max(self) -> T:
        """
        Removes and returns the largest element from the heap.

        Running Time:
            O(log n)

        Returns:
            T: The largest element of the heap.

        >>> h = MaxHeap()
        >>> h.insert(3)
        >>> h.insert(1)
        >>> h.insert(4)
        >>> h.extract_max()
        4
        >>> h.heap
        [1, 3]
        """
        return self.extract_top()