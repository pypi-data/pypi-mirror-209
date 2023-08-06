import unittest
from unittest import TestCase
from node import Node


class TestNode(TestCase):
    """Tests the Node data structure."""

    def setUp(self) -> None:
        """
        Sets up the test suite.
        :return: None
        """
        self.one = Node(1)
        self.two = Node(2, self.one)

    def test_init(self) -> None:
        """
        Tests the initialization of the Node data structure.
        :return: None
        """
        self.assertTrue(self.one.data == 1)
        self.assertTrue(self.one.next is None)
        self.assertTrue(self.two.data == 2)
        self.assertTrue(self.two.next is self.one)

    def test_data(self) -> None:
        """
        Tests the data property of the Node data structure.
        :return: None
        """
        self.assertTrue(self.one.data == 1)
        self.assertTrue(self.two.data == 2)

    def test_next(self) -> None:
        """
        Tests the next property of the Node data structure.
        :return: None
        """
        self.assertTrue(self.one.next is None)
        self.assertTrue(self.two.next is self.one)


if __name__ == '__main__':
    unittest.main()
