import turtle


class Runner:
    def __init__(self, x: int, y: int, color: str):
        self._x = x
        self._y = y
        self._position = 0
        self._steps = 0
        self._trl = turtle.Turtle()
        self._trl.color(color)
        self._trl.hideturtle()
        self._trl.penup()
        self._trl.goto(x, y)
        self._trl.showturtle()
        self._trl.pendown()

    def run(self):
        pass

    @property
    def position(self):
        return self._position
