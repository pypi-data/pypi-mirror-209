from abc import abstractmethod, ABC
from typing import Any


class NodeInterface(ABC):
    """Defines the interface for the Node object."""

    @abstractmethod
    def __init__(self, data: Any, _next: 'Node') -> None:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass


class Node(NodeInterface):
    """
    Defines a Node object used in data structures.
    Contracted by the Node interface.
    """

    def __init__(self, data: Any, _next: 'Node' = None) -> None:
        """
        Constructor for the Node object.
        :param data: Any
        :param _next: Node
        """
        self._data = data
        self._next = _next

    def __str__(self) -> str:
        """
        Returns a string representation of the Node object to display.
        :return: str
        """
        return "Node has a value of {}\nIts next sibling has a value of {}".format(self._data, self._next._data)

    def __repr__(self) -> str:
        """
        Returns a string representation of the Node object to debug.
        :return: str
        """
        return "Node({})".format(self._data)

    @property
    def data(self) -> Any:
        """
        Returns the Node's data.
        :return: Any
        """
        return self._data

    @data.setter
    def data(self, value: Any) -> None:
        """
        Sets the Node's data
        :param value: Any
        :return: None
        """
        self._data = value

    @property
    def next(self) -> 'Node':
        """
        Returns the Node's next sibling.
        :return: 'Node
        """
        return self._next

    @next.setter
    def next(self, value: 'Node') -> None:
        """
        Sets the Node's next sibling.
        :param value: Node
        :return: None
        """
        self._next = value
