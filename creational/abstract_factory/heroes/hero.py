from abc import abstractmethod
from creational.abstract_factory.villains.villain import Villain


class Hero:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

    @abstractmethod
    def interact_with(self, villain: Villain):
        pass
