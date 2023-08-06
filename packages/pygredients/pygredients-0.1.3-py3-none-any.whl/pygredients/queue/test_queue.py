import unittest
from unittest import TestCase
from queue import Queue as Queue


class TestQueue(TestCase):
    """Tests the Queue data structure."""

    def setUp(self) -> None:
        """
        Sets up the test suite.
        :return: None
        """
        data = [1, 2, 3, 4, 5]
        self.queue = Queue()
        for item in data:
            self.queue.enqueue(item)

    def test_init(self) -> None:
        """
        Tests the initialization of the Queue data structure.
        :return: None
        """
        self.assertTrue(self.queue.head is not None)
        self.assertTrue(self.queue._size == 5)

    def test_limit(self) -> None:
        """
        Tests the limit property of the Queue data structure.
        :return: None
        """
        self.assertTrue(self.queue.limit == float("inf"))
        self.queue.limit = 10
        self.assertTrue(self.queue.limit == 10)
        self.assertRaises(ValueError, setattr, self.queue, "limit", -1)
        self.assertRaises(ValueError, setattr, self.queue, "limit", 4)

    def test_enqueue(self) -> None:
        """
        Tests the enqueue method of the Queue data structure.
        :return: None
        """
        self.queue.enqueue(6)
        self.assertTrue(self.queue._size == 6)
        self.assertTrue(self.queue.head.data == 1)
        self.assertRaises(ValueError, self.queue.enqueue, None)
        self.queue.limit = 6
        self.assertRaises(IndexError, self.queue.enqueue, 7)

    def test_dequeue(self) -> None:
        """
        Tests the dequeue method of the Queue data structure.
        :return: None
        """
        self.queue.dequeue()
        self.assertTrue(self.queue._size == 4)
        self.assertTrue(self.queue.head.data == 2)
        self.queue.dequeue()
        self.assertTrue(self.queue._size == 3)
        self.assertTrue(self.queue.head.data == 3)
        self.queue.dequeue()
        self.assertTrue(self.queue._size == 2)
        self.assertTrue(self.queue.head.data == 4)
        self.queue.dequeue()
        self.assertTrue(self.queue._size == 1)
        self.assertTrue(self.queue.head.data == 5)
        self.queue.dequeue()
        self.assertRaises(IndexError, self.queue.dequeue)

    def test_peek(self) -> None:
        """
        Tests the peek method of the Queue data structure.
        :return: None
        """
        self.assertTrue(self.queue.peek() == 1)
        self.assertTrue(self.queue._size == 5)
        for _ in range(5):
            self.queue.dequeue()
        self.assertRaises(IndexError, self.queue.peek)

    def test_contains(self) -> None:
        """
        Tests the contain method of the Queue data structure.
        :return: None
        """
        self.assertTrue(self.queue.contains(1))
        self.assertTrue(self.queue.contains(2))
        self.assertTrue(self.queue.contains(3))
        self.assertTrue(self.queue.contains(4))
        self.assertTrue(self.queue.contains(5))
        self.assertFalse(self.queue.contains(6))
        self.assertRaises(ValueError, self.queue.contains, None)
        for _ in range(5):
            self.queue.dequeue()
        self.assertRaises(IndexError, self.queue.contains, 1)

    def test_size(self) -> None:
        """
        Tests the size method of the Queue data structure.
        :return: None
        """
        self.assertTrue(self.queue.size() == 5)
        self.queue.enqueue(6)
        self.assertTrue(self.queue.size() == 6)

    def test_is_empty(self) -> None:
        """
        Tests the is_empty method of the Queue data structure.
        :return: None
        """
        self.assertFalse(self.queue.is_empty())
        self.queue.dequeue()
        self.queue.dequeue()
        self.queue.dequeue()
        self.queue.dequeue()
        self.queue.dequeue()
        self.assertTrue(self.queue.is_empty())


if __name__ == '__main__':
    unittest.main()
