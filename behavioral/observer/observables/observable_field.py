from behavioral.observer.common.observable import Observable
from behavioral.observer.common.observer import Observer


class ObservableField(Observable):
    def __init__(self, name: str, field_type: object):
        self._subscribers = set()
        self._name = name
        self._value = None
        self._type = field_type

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value: object):
        if value.__class__ is self._type:
            self._value = value
            self.notify(name=self._name, value=self._value, type=self._type)
        else:
            raise ValueError(f"Invalid type provided, valid data type is {self._type}")

    def subscribe(self, observer: Observer):
        self._subscribers.add(observer)

    def unsubscribe(self, observer: Observer):
        self._subscribers.remove(observer)

    def notify(self, *args, **kwargs):
        for subscriber in self._subscribers:
            subscriber: Observer
            subscriber.notify(*args, **kwargs)
