from pygredients.node.node import Node
from typing import Any

class LinkedList:
    """
    This class represents a singly linked list data structure, consisting of Node objects.
    The list has a size property, which keeps track of the number of nodes in the list,
    and a limit property, which sets the maximum number of nodes allowed in the list.
    The list supports standard operations like appending, removing, peeking (i.e., getting the head node),
    and checking whether a particular value exists in the list.
    """

    def __init__(self, limit=None) -> None:
        """
        Constructs a new linked list.
        If a limit is not provided, the list will have no fixed size limit.
        :param limit: The maximum number of nodes allowed in the list.
                      Defaults to None, in which case the list can grow indefinitely.
        """
        if not limit: self._limit = float("inf")
        else: self._limit = limit
        self._size: int = 0
        self.head = None

    def __str__(self) -> str:
        """
        Returns a string representation of the linked list, detailing its size and the items it contains.
        :return: str
        """
        data = []
        current = self.head
        while current is not None:
            data.append(current.data)
            current = current.next
        return "Linked List has a size of {} and contains the following items:\n{}".format(self._size, data)

    def __repr__(self) -> str:
        """
        Returns a technical string representation of the linked list, useful for debugging.
        :return: str
        """
        return "LinkedList({})".format(self._size)

    @property
    def limit(self) -> int:
        """
        Getter for the limit of the linked list.
        The limit represents the maximum number of nodes that can be stored in the list.
        :return: The maximum number of nodes allowed in the list.
        """
        return self._limit

    @limit.setter
    def limit(self, value: int) -> None:
        """
        Setter for the limit of the linked list.
        The new limit must be a positive integer and greater than or equal to the current size of the list.
        :param value: The new maximum number of nodes allowed in the list.
        """
        if not value > 0:
            raise ValueError("Cannot set the limit to {} as it is not a valid value.".format(value))
        elif value < self._size:
            raise ValueError("Cannot set the limit to {} as it is smaller than the current size of the Linked List.".format(value))
        self._limit = value

    def append(self, data: Any) -> None:
        """
        Adds a new node with the provided data to the beginning of the list.
        If the list has reached its size limit, an IndexError is raised.
        :param data: The data to be stored in the new node. Must not be None.
        """
        if data is None:
            raise ValueError("Cannot append {} to the Linked List.".format(data))
        if self._size == self._limit:
            raise IndexError("Cannot append {} to Linked List as it is full.".format(data))
        self.head = Node(data, self.head)
        self._size += 1

    def remove(self, data: Any) -> Any:
        """
        Removes the first node in the list that contains the provided data and returns its data.
        If the data does not exist in the list or the list is empty, an error is raised.
        :param data: The data of the node to remove from the list.
        :return: The data of the removed node.
        """
        if self.is_empty():
            raise IndexError("Cannot remove {} from an empty Linked List.".format(data))
        if data is None:
            raise ValueError("Cannot remove {} from the Linked List.".format(data))
        current = self.head
        previous = None
        while current is not None:
            if data == current.data:
                if previous is not None:
                    previous.next = current.next
                else:
                    self.head = current.next
                self._size -= 1
                return current.data
            previous = current
            current = current.next
        raise ValueError("Cannot remove {} from Linked List as it does not exist.".format(data))

    def peek(self) -> Any:
        """
        Returns the data of the first node in the list.
        If the list is empty, an error is raised.
        :return: First node's data.
        """
        if self.is_empty():
            raise IndexError("Cannot peek an empty Linked List.")
        return self.head.data

    def contains(self, data: Any) -> bool:
        """
        Checks if the provided data exists in any node in the list.
        If the list is empty, an error is raised.
        :param data: The data to search for in the list.
        :return: True if the data exists in the list, False otherwise.
        """
        if self.is_empty():
            raise IndexError("Cannot search an empty Linked List.")
        if data is None:
            raise ValueError("Cannot search for {} in the Linked List.".format(data))
        current = self.head
        while current is not None:
            if data == current.data:
                return True
            current = current.next
        return False

    def size(self) -> int:
        """
        Returns the current number of nodes in the list.
        :return: the size of the list.
        """
        return self._size

    def is_empty(self) -> bool:
        """
        Checks if the list is currently empty (i.e., contains no nodes).
        :return: True if the list is empty, False otherwise.
        """
        return self._size == 0
