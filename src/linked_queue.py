from typing import TypeVar, Optional
from linked_list import LinkedList

T = TypeVar('T')

class Queue():
    def __init__(self):
        self._linked_list = LinkedList()

    def enqueue(self, item: T) -> None:
        """
        Add an item to the end of the queue.
        Time complexity: O(1)
        """
        self._linked_list.append(item)

    def dequeue(self) -> Optional[T]:
        """
        Remove and return the first item from the queue.
        Time complexity: O(1)
        """
        if self.is_empty():
            return None
        first_item = self._linked_list.peek()
        self._linked_list.delete_first()
        return first_item

    def peek(self) -> Optional[T]:
        """
        Return the first item from the queue without removing it.
        Time complexity: O(1)
        """
        return self._linked_list.peek()

    def is_empty(self) -> bool:
        """
        Check if the queue is empty.
        Time complexity: O(1)
        """
        return self._linked_list.head is None

    def __iter__(self):
        """
        Iterator to traverse the queue.
        Time complexity: O(n)
        """
        return iter(self._linked_list)

    def __str__(self):
        """ String representation of the queue. """
        return str(self._linked_list)
