from abc import ABC, abstractmethod


class Strategy(ABC):

    @abstractmethod
    def execute(self, distance: int):
        pass
