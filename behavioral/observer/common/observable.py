from abc import ABC, abstractmethod


class Observable(ABC):
    @abstractmethod
    def subscribe(self, observer):
        pass

    @abstractmethod
    def unsubscribe(self, observer):
        pass

    @abstractmethod
    def notify(self, *args, **kwargs):
        pass
