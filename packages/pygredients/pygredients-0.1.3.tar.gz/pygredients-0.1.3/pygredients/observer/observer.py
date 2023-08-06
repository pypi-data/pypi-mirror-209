from abc import abstractmethod
from typing import Optional, List


class Observer:
    """
    Abstract class representing an observer in the observer design pattern.
    An observer is an object that wishes to be informed about events happening in the system.
    The events are typically changes in state of other objects.
    """

    def __init__(self, name=None) -> None:
        """
        Initialize the Observer object.

        :param name: Optional identifier for the observer.
        """
        self.name = name
        self.is_subscribed = False

    @abstractmethod
    def notify(self, *args, **kwargs) -> None:
        """
        Abstract method to notify the observer.

        :param args: Additional arguments to pass to the method.
        :param kwargs: Additional keyword arguments to pass to the method.
        :return: None
        """
        pass

    def unsubscribe(self) -> None:
        """
        Unsubscribes the Observer. After calling this method, the observer will not receive any notifications.

        :return: None
        """
        self.is_subscribed = False


class Observable:
    """
    Class representing an observable in the observer design pattern.
    An observable is an object that other objects (observers) can subscribe to.
    When an event occurs, the observable notifies all of its subscribers.
    """

    def __init__(self) -> None:
        """
        Initialize the Observable object.
        """
        self._observers: Optional[List[Observer]] = []
        self._state = None

    @property
    def state(self) -> dict:
        """
        Property that represents the current state of the observable object.
        :return: The current state of the observable.
        """
        return self._state

    @state.setter
    def state(self, value: dict) -> None:
        """
        Setter for the state property. When the state changes, all observers are notified.

        :param value: The new state.
        :return: None
        """
        self._state = value
        self.notify_observers(value)

    @property
    def observers(self) -> list[Observer]:
        """
        Property that represents the list of observers that are currently subscribed.
        :return: The list of observers.
        """
        return self._observers

    def register_observers(self, observer: Observer) -> None:
        """
        Registers an observer. After an observer is registered, it will receive notifications of state changes.

        :param observer: The observer to register.
        :return: None
        """
        observer.is_subscribed = True
        self._observers.append(observer)

    def remove_observers(self, observer: Observer) -> None:
        """
        Removes an observer. After an observer is removed, it will no longer receive notifications.

        :param observer: The observer to remove.
        :return: None
        """
        observer.is_subscribed = False
        self._observers.remove(observer)

    def notify_observers(self, *args, **kwargs) -> None:
        """
        Notifies all registered observers about a state change.

        :param args: Additional arguments to pass to the method.
        :param kwargs: Additional keyword arguments to pass to the method.
        :return: None
        """
        for observer in self._observers:
            if observer.is_subscribed:
                observer.notify(*args, **kwargs)
