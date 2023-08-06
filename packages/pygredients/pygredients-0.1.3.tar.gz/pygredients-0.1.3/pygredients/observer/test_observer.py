import unittest
from observer import Observer, Observable

class TestObserver(Observer):
    """
    Concrete implementation of Observer class for testing purposes.
    Stores the value it was notified with, so we can check it in the tests.
    """

    def __init__(self, name=None) -> None:
        """
        Initialize the TestObserver object.

        :param name: Optional identifier for the observer.
        """
        super().__init__(name)
        self.notified_value = None

    def notify(self, *args, **kwargs) -> None:
        """
        Implementation of the abstract notify method.
        Stores the value it was notified with in the notified_value attribute.

        :param args: Additional arguments to pass to the method.
        :param kwargs: Additional keyword arguments to pass to the method.
        :return: None
        """
        self.notified_value = args[0]


class ObserverObservableTest(unittest.TestCase):
    """
    A class for unit-testing the Observer and Observable classes.
    """

    def setUp(self) -> None:
        """
        Method that is run before each test. Sets up the test environment.
        Initializes an Observable and two TestObservers.
        :return: None
        """
        self.observable = Observable()
        self.observer1 = TestObserver("observer1")
        self.observer2 = TestObserver("observer2")

    def test_register_observer(self) -> None:
        """
        Tests the register_observers method of the Observable class.
        :return: None
        """
        self.observable.register_observers(self.observer1)
        self.assertIn(self.observer1, self.observable.observers)
        self.assertTrue(self.observer1.is_subscribed)

    def test_remove_observer(self) -> None:
        """
        Tests the remove_observers method of the Observable class.
        :return: None
        """
        self.observable.register_observers(self.observer1)
        self.observable.remove_observers(self.observer1)
        self.assertNotIn(self.observer1, self.observable.observers)
        self.assertFalse(self.observer1.is_subscribed)

    def test_notify_observers(self) -> None:
        """
        Tests the notify_observers method of the Observable class.
        :return: None
        """
        self.observable.register_observers(self.observer1)
        self.observable.register_observers(self.observer2)
        self.observable.state = {'data': 'test'}
        self.assertEqual(self.observer1.notified_value, {'data': 'test'})
        self.assertEqual(self.observer2.notified_value, {'data': 'test'})

    def test_unsubscribe(self) -> None:
        """
        Tests the unsubscribe method of the Observer class.
        :return: None
        """
        self.observable.register_observers(self.observer1)
        self.observable.register_observers(self.observer2)
        self.observer1.unsubscribe()
        self.observable.state = {'data': 'test'}
        self.assertEqual(self.observer1.notified_value, None)
        self.assertEqual(self.observer2.notified_value, {'data': 'test'})


if __name__ == '__main__':
    unittest.main()
