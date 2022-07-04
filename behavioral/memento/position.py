from behavioral.memento.common.originator import Originator


class Position(Originator):
    def __init__(self):
        self.x = 0
        self.y = 0

    def __str__(self):
        return f"({self.x}, {self.y})"
