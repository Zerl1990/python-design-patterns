from abc import abstractmethod, ABC


class Villain(ABC):
    @abstractmethod
    def action(self):
        pass
