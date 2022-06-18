import turtle
from introduction.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, trl: turtle.Turtle, size: int, color: str):
        super().__init__(trl, size, size, color)


if __name__ == '__main__':
    t1 = turtle.Turtle()
    t2 = turtle.Turtle()

    rectangle = Rectangle(t1, 40, 20, "red")
    square = Square(t2, 100, "blue")

    rectangle.draw()
    square.draw()

    input("Type any key to exit.")
