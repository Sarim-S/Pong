from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.make_paddle(position)

    def make_paddle(self, position):
        self.shape("square")
        self.setheading(90)
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(position)

    def up(self):
        if self.ycor() <= 240:
            self.forward(25)

    def down(self):
        if self.ycor() >= -240:
            self.forward(-25)
