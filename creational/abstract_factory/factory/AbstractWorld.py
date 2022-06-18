from abc import abstractmethod


class AbstractWorld:

    @abstractmethod
    def create_hero(self):
        pass

    @abstractmethod
    def create_villain(self):
        pass
