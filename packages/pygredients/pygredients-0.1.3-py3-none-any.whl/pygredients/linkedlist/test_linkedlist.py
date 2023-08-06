import unittest
from unittest import TestCase
from linkedlist import LinkedList as LinkedList


class TestLinkedList(TestCase):
    """Tests the Linked List data structure."""

    def setUp(self) -> None:
        """
        Sets up the test suite.
        :return: None
        """
        self.linked_list = LinkedList()
        for item in range(1, 6):
            self.linked_list.append(item)

    def test_init(self) -> None:
        """
        Tests the initialization of the Linked List data structure.
        :return: None
        """
        self.assertTrue(self.linked_list.head is not None)
        self.assertTrue(self.linked_list._size == 5)

    def test_limit(self) -> None:
        """
        Tests the limit property of the Linked List data structure.
        :return: None
        """
        self.assertTrue(self.linked_list.limit == float("inf"))
        self.linked_list.limit = 10
        self.assertTrue(self.linked_list.limit == 10)
        self.assertRaises(ValueError, setattr, self.linked_list, "limit", -1)
        self.assertRaises(ValueError, setattr, self.linked_list, "limit", 4)

    def test_append(self):
        """
        Tests the append method of the Linked List data structure.
        :return: None
        """
        self.linked_list.append(6)
        self.assertTrue(self.linked_list._size == 6)
        self.assertTrue(self.linked_list.head.data == 6)
        self.assertRaises(ValueError, self.linked_list.append, None)
        self.linked_list.limit = 6
        self.assertRaises(IndexError, self.linked_list.append, 7)

    def test_remove(self) -> None:
        """
        Tests the remove method of the Linked List data structure.
        :return: None
        """
        self.linked_list.remove(5)
        self.assertTrue(self.linked_list._size == 4)
        self.assertTrue(self.linked_list.head.data == 4)
        self.linked_list.remove(1)
        self.assertTrue(self.linked_list._size == 3)
        self.assertTrue(self.linked_list.head.data == 4)
        self.linked_list.remove(4)
        self.assertTrue(self.linked_list._size == 2)
        self.assertTrue(self.linked_list.head.data == 3)
        self.linked_list.remove(2)
        self.assertRaises(ValueError, self.linked_list.remove, None)
        self.assertRaises(ValueError, self.linked_list.remove, 9)
        self.linked_list.remove(3)
        self.assertTrue(self.linked_list._size == 0)

    def test_peek(self) -> None:
        """
        Tests the peek method of the Linked List data structure.
        :return: None
        """
        self.assertTrue(self.linked_list.peek() == 5)
        self.assertTrue(self.linked_list._size == 5)
        for item in range(1, 6):
            self.linked_list.remove(item)
        self.assertRaises(IndexError, self.linked_list.peek)

    def test_contains(self) -> None:
        """
        Tests the contain method of the Linked List data structure.
        :return: None
        """
        self.assertTrue(self.linked_list.contains(5))
        self.assertTrue(self.linked_list.contains(1))
        self.assertTrue(self.linked_list.contains(3))
        self.assertFalse(self.linked_list.contains(6))
        self.assertFalse(self.linked_list.contains(0))
        self.assertRaises(ValueError, self.linked_list.contains, None)
        for item in range(1, 6):
            self.linked_list.remove(item)
        self.assertRaises(IndexError, self.linked_list.contains, 1)

    def test_size(self) -> None:
        """
        Tests the size method of the Linked List data structure.
        :return: None
        """
        self.assertTrue(self.linked_list.size() == 5)
        self.linked_list.append(6)
        self.assertTrue(self.linked_list.size() == 6)
        self.linked_list.remove(6)
        self.assertTrue(self.linked_list.size() == 5)

    def test_is_empty(self) -> None:
        """
        Tests the is_empty method of the Linked List data structure.
        :return: None
        """
        self.assertFalse(self.linked_list.is_empty())
        self.linked_list.remove(5)
        self.linked_list.remove(4)
        self.linked_list.remove(3)
        self.linked_list.remove(2)
        self.linked_list.remove(1)
        self.assertTrue(self.linked_list.is_empty())


if __name__ == '__main__':
    unittest.main()
