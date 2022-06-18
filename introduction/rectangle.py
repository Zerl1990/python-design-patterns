import turtle


class Rectangle:
    def __init__(self, trl: turtle.Turtle, height: int, width: int, color: str):
        self._turtle = trl
        self._height = height
        self._width = width
        self._color = color

    def draw(self):
        self._turtle.color(self._color)

        self._turtle.forward(self._width)
        self._turtle.left(90)

        self._turtle.forward(self._height)
        self._turtle.left(90)

        self._turtle.forward(self._width)
        self._turtle.left(90)

        self._turtle.forward(self._height)
        self._turtle.left(90)
