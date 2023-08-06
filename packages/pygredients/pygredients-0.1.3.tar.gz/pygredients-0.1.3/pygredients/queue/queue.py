from pygredients.node.node import Node
from typing import Any

class Queue:
    """
    This class represents a Queue data structure, implemented as a singly linked list of Node objects.
    The queue has a size property, which keeps track of the number of nodes in the list,
    and a limit property, which sets the maximum number of nodes allowed in the list.
    The queue supports standard queue operations like enqueue (i.e., add to the end),
    dequeue (i.e., remove from the front), peeking, and checking whether a particular value exists in the list.
    """

    def __init__(self, limit=None) -> None:
        """
        Constructs a new queue.
        If a limit is not provided, the queue will have no fixed size limit.
        :param limit: The maximum number of nodes allowed in the queue.
                      Defaults to None, in which case the queue can grow indefinitely.
        """
        if not limit:
            self._limit = float("inf")
        else:
            self._limit = limit
        self._size: int = 0
        self.head = None

    def __str__(self) -> str:
        """
        Returns a string representation of the queue, detailing its size and the items it contains.
        :return: str
        """
        data = []
        current = self.head
        while current is not None:
            data.append(current.data)
            current = current.next
        return "Queue has a size of {} and contains the following items:\n{}".format(self._size, data)

    @property
    def limit(self) -> int:
        """
        Getter for the limit of the queue.
        The limit represents the maximum number of nodes that can be stored in the queue.
        :return: The maximum number of nodes allowed in the queue.
        """
        return self._limit

    @limit.setter
    def limit(self, value: int) -> None:
        """
        Setter for the limit of the queue.
        The new limit must be a positive integer and greater than or equal to the current size of the queue.
        :param value: The new maximum number of nodes allowed in the queue.
        """
        if not value > 0:
            raise ValueError("Cannot set the limit to {} as it is not a valid value.".format(value))
        elif value < self._size:
            raise ValueError(
                "Cannot set the limit to {} as it is smaller than the current size of the queue.".format(value))
        self._limit = value

    def __repr__(self) -> str:
        """
        Returns a technical string representation of the queue, useful for debugging.
        :return: str
        """
        return "Queue({})".format(self._size)

    def enqueue(self, data: Any) -> None:
        """
        Adds a new node with the provided data to the end of the queue.
        If the queue has reached its size limit, an IndexError is raised.
        :param data: The data to be stored in the new node. Must not be None.
        """
        if data is None:
            raise ValueError("Cannot enqueue {} in the Queue.".format(data))
        if self._size == self._limit:
            raise IndexError("Cannot append {} to the Queue as it is full.".format(data))
        if self.head is None:
            self.head = Node(data)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(data)
        self._size += 1

    def dequeue(self) -> Any:
        """
        Removes the node at the front of the queue and returns its data.
        If the queue is empty, an IndexError is raised.
        :return: The data of the dequeued node.
        """
        if self.is_empty():
            raise IndexError("Cannot dequeue an empty Queue.")
        current = self.head
        self.head = current.next
        self._size -= 1
        return current.data

    def peek(self) -> Any:
        """
        Returns the data of the node at the front of the queue.
        If the queue is empty, an IndexError is raised.
        :return: The data of the front node.
        """
        if self.is_empty():
            raise IndexError("Cannot peek an empty Queue.")
        return self.head.data

    def contains(self, data: Any) -> bool:
        """
        Checks if the provided data exists in any node in the queue.
        If the queue is empty, an IndexError is raised.
        :param data: The data to search for in the queue.
        :return: True if the data exists in the queue, False otherwise.
        """
        if self.is_empty():
            raise IndexError("Cannot search an empty Queue.")
        if data is None:
            raise ValueError("Cannot search for {} in the Queue.".format(data))
        current = self.head
        while current is not None:
            if data == current.data:
                return True
            current = current.next
        return False

    def size(self) -> int:
        """
        Returns the current number of nodes in the queue.
        :return: the size of the queue.
        """
        return self._size

    def is_empty(self) -> bool:
        """
        Checks if the queue is currently empty (i.e., contains no nodes).
        :return: True if the queue is empty, False otherwise.
        """
        return self._size == 0
