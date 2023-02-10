from abc import ABC, abstractmethod

from behavioral.observer.common.observer import Observer


class Observable(ABC):
    @abstractmethod
    def subscribe(self, observer: Observer):
        pass

    @abstractmethod
    def unsubscribe(self, observer: Observer):
        pass

    @abstractmethod
    def notify_all_subscriber(self, *args, **kwargs):
        pass
