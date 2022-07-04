from behavioral.memento.common.originator import Originator


class CareTaker:
    def __init__(self, originator: Originator):
        self._originator = originator
        self._history = []

    def backup(self):
        self._history.append(self._originator.save())

    def undo(self):
        if len(self._history):
            self._originator.restore(self._history.pop())
        else:
            raise IndexError("We don´t have more backups.")
