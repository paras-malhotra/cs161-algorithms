from typing import Optional, Iterator, TypeVar

T = TypeVar('T')

class Node:
    def __init__(self, data: T):
        self.data: T = data
        self.next: Optional['Node'] = None

class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def append(self, data):
        """
        Append a new node at the end of the list.
        Time complexity: O(1)
        """
        new_node = Node(data)
        # If the list is empty, the new node is the head and the tail
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data: T) -> None:
        """
        Prepend a new node at the beginning of the list.
        Time complexity: O(1)
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        if not self.tail:
            # Update the tail if the list was empty
            self.tail = new_node

    def delete_first(self) -> None:
        """
        Delete the first node (head) of the list.
        Time complexity: O(1)
        """
        if self.head:
            self.head = self.head.next
            if not self.head:
                # Update the tail if the list is empty
                self.tail = None

    def peek(self) -> Optional[T]:
        """
        Peek at the first element of the list without removing it.
        Time complexity: O(1)
        """
        if self.head:
            return self.head.data
        return None

    def __iter__(self) -> Iterator[T]:
        """
        Iterator to traverse the list.
        Time complexity: O(n)
        """
        current = self.head
        while current:
            yield current
            current = current.next

    def __str__(self) -> str:
        """ String representation of the list. """
        nodes = [str(node.data) for node in self]
        return ' -> '.join(nodes)