from behavioral.memento.common.memento import Memento


class Originator:
    def save(self):
        memento = Memento()
        memento.value = self
        return memento

    def restore(self, memento):
        for name, value in vars(memento.value).items():
            self.__setattr__(name, value)
