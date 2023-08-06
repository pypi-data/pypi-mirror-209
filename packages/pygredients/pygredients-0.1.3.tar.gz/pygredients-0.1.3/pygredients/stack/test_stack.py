import unittest
from unittest import TestCase
from stack import Stack as Stack


class TestStack(TestCase):
    """Tests the Stack data structure."""

    def setUp(self) -> None:
        """
        Sets up the test suite.
        :return: None
        """
        data = [1, 2, 3, 4, 5]
        self.stack = Stack()
        for item in data:
            self.stack.push(item)

    def test_init(self) -> None:
        """
        Tests the initialization of the Stack data structure.
        :return: None
        """
        self.assertTrue(self.stack.head is not None)
        self.assertTrue(self.stack._size == 5)

    def test_limit(self) -> None:
        """
        Tests the limit property of the Stack data structure.
        :return: None
        """
        self.assertTrue(self.stack.limit == float("inf"))
        self.stack.limit = 10
        self.assertTrue(self.stack.limit == 10)
        self.assertRaises(ValueError, setattr, self.stack, "limit", -1)
        self.assertRaises(ValueError, setattr, self.stack, "limit", 4)

    def test_push(self) -> None:
        """
        Tests the push method of the Stack data structure.
        :return: None
        """
        self.stack.push(6)
        self.assertTrue(self.stack._size == 6)
        self.assertTrue(self.stack.head.data == 6)
        self.assertRaises(ValueError, self.stack.push, None)
        self.stack.limit = 6
        self.assertRaises(IndexError, self.stack.push, 7)

    def test_pop(self) -> None:
        """
        Tests the pop method of the Stack data structure.
        :return: None
        """
        self.stack.pop()
        self.assertTrue(self.stack._size == 4)
        self.assertTrue(self.stack.head.data == 4)
        self.stack.pop()
        self.assertTrue(self.stack._size == 3)
        self.assertTrue(self.stack.head.data == 3)
        self.stack.pop()
        self.assertTrue(self.stack._size == 2)
        self.assertTrue(self.stack.head.data == 2)
        self.stack.pop()
        self.assertTrue(self.stack._size == 1)
        self.assertTrue(self.stack.head.data == 1)
        self.stack.pop()
        self.assertRaises(IndexError, self.stack.pop)

    def test_peek(self) -> None:
        """
        Tests the peek method of the Stack data structure.
        :return: None
        """
        self.assertTrue(self.stack.peek() == 5)
        self.assertTrue(self.stack._size == 5)
        for _ in range(5):
            self.stack.pop()
        self.assertRaises(IndexError, self.stack.peek)

    def test_contains(self) -> None:
        """
        Tests the contain method of the Stack data structure.
        :return: None
        """
        self.assertTrue(self.stack.contains(5))
        self.assertTrue(self.stack.contains(4))
        self.assertTrue(self.stack.contains(3))
        self.assertTrue(self.stack.contains(2))
        self.assertTrue(self.stack.contains(1))
        self.assertFalse(self.stack.contains(6))
        self.assertRaises(ValueError, self.stack.contains, None)
        for _ in range(5):
            self.stack.pop()
        self.assertRaises(IndexError, self.stack.contains, 1)

    def test_size(self) -> None:
        """
        Tests the size method of the Stack data structure.
        :return: None
        """
        self.assertTrue(self.stack.size() == 5)
        self.stack.push(6)
        self.assertTrue(self.stack.size() == 6)
        self.stack.pop()
        self.assertTrue(self.stack.size() == 5)

    def test_is_empty(self) -> None:
        """
        Tests the is_empty method of the Stack data structure.
        :return: None
        """
        self.assertFalse(self.stack.is_empty())
        for _ in range(5):
            self.stack.pop()
        self.assertTrue(self.stack.is_empty())


if __name__ == '__main__':
    unittest.main()
