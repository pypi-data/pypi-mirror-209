from pygredients.node.node import Node
from typing import Any


class Stack:
    """
    This class represents a Stack data structure, implemented as a singly linked list of Node objects.
    The stack has a size property, which keeps track of the number of nodes in the list,
    and a limit property, which sets the maximum number of nodes allowed in the list.
    The stack supports standard stack operations like push (i.e., add to the top),
    pop (i.e., remove from the top), peeking, and checking whether a particular value exists in the list.
    """

    def __init__(self, limit=None) -> None:
        """
        Constructs a new stack.
        If a limit is not provided, the stack will have no fixed size limit.
        :param limit: The maximum number of nodes allowed in the stack.
                      Defaults to None, in which case the stack can grow indefinitely.
        """
        if not limit:
            self._limit = float("inf")
        else:
            self._limit = limit
        self._size: int = 0
        self.head = None

    def __str__(self) -> str:
        """
        Returns a string representation of the stack, detailing its size and the items it contains.
        :return: str
        """
        data = []
        current = self.head
        while current is not None:
            data.append(current.data)
            current = current.next
        return "Stack has a size of {} and contains the following items:\n{}.".format(self._size, data)

    def __repr__(self) -> str:
        """
        Returns a technical string representation of the stack, useful for debugging.
        :return: str
        """
        return "Stack({})".format(self._size)

    @property
    def limit(self) -> int:
        """
        Getter for the limit of the stack.
        The limit represents the maximum number of nodes that can be stored in the stack.
        :return: The maximum number of nodes allowed in the stack.
        """
        return self._limit

    @limit.setter
    def limit(self, value: int) -> None:
        """
        Setter for the limit of the stack.
        The new limit must be a positive integer and greater than or equal to the current size of the stack.
        :param value: The new maximum number of nodes allowed in the stack.
        """
        if not value > 0:
            raise ValueError("Cannot set the limit to {} as it is not a valid value.".format(value))
        elif value < self._size:
            raise ValueError(
                "Cannot set the limit to {} as it is smaller than the current size of the stack.".format(value))
        self._limit = value

    def push(self, data: Any) -> None:
        """
        Adds a new node with the provided data to the top of the stack.
        If the stack has reached its size limit, an IndexError is raised.
        :param data: The data to be stored in the new node. Must not be None.
        """
        if data is None:
            raise ValueError("Cannot push {} to the Stack.".format(data))
        if self._size == self._limit:
            raise IndexError("Cannot push {} to Stack as it is full.".format(data))
        self.head = Node(data, self.head)
        self._size += 1

    def pop(self) -> Any:
        """
        Removes the node at the top of the stack and returns its data.
        If the stack is empty, an IndexError is raised.
        :return: The data of the popped node.
        """
        if self.is_empty():
            raise IndexError("Cannot pop from an empty Stack.")
        data = self.head.data
        self.head = self.head.next
        self._size -= 1
        return data

    def peek(self) -> Any:
        """
        Returns the data of the node at the top of the stack.
        If the stack is empty, an IndexError is raised.
        :return: The data of the top node.
        """
        if self.is_empty():
            raise IndexError("Cannot peek an empty Stack.")
        return self.head.data

    def contains(self, data: Any) -> bool:
        """
        Checks if the provided data exists in any node in the stack.
        If the stack is empty, an IndexError is raised.
        :param data: The data to search for in the stack.
        :return: True if the data exists in the stack, False otherwise.
        """
        if self.is_empty():
            raise IndexError("Cannot search an empty Stack.")
        if data is None:
            raise ValueError("Cannot search for {} in the Stack.".format(data))
        current = self.head
        while current is not None:
            if data == current.data:
                return True
            current = current.next
        return False

    def size(self) -> int:
        """
        Returns the current number of nodes in the stack.
        :return: The size of the stack.
        """
        return self._size

    def is_empty(self) -> bool:
        """
        Checks if the stack is currently empty (i.e., contains no nodes).
        :return: True if the stack is empty, False otherwise.
        """
        return self._size == 0
