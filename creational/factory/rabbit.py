import turtle
from creational.factory.runner import Runner


class Rabbit(Runner):
    _DELTA = 150
    _COLOR = 'red'

    def __init__(self, x: int, y: int):
        super().__init__(x, y, Rabbit._COLOR)

    def run(self):
        if self._steps % Rabbit._DELTA == 0:  # Rabbit has to get some sleep
            self._position += Rabbit._DELTA
            self._trl.forward(Rabbit._DELTA)
        self._steps += 1

