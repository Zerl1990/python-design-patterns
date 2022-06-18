from creational.factory.runner import Runner


class RTurtle(Runner):
    _DELTA = 2
    _COLOR = 'blue'

    def __init__(self, x: int, y: int):
        super().__init__(x, y, RTurtle._COLOR)

    def run(self):
        self._steps += 1
        self._position += RTurtle._DELTA
        self._trl.forward(RTurtle._DELTA)
