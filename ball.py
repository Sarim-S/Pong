import random
from turtle import Turtle
from random import randint


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.generate_ball()
        self.x_move = 10
        self.y_move = 10

    def generate_ball(self):
        self.shape("circle")
        self.home()
        self.penup()
        self.color("white")

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1

