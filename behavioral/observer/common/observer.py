from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def receive_observable_notification(self, *args, **kwargs):
        pass
