from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.ht()

    def draw_dotted_line(self):
        self.up()
        self.goto(0, -290)
        self.setheading(90)
        self.down()
        while self.ycor() < 250:
            self.forward(10)
            self.up()
            self.forward(20)
            self.down()

    def write_score(self, left=0, right=0):
        self.clear()
        self.up()
        self.goto(0, 260)
        self.write(f"{left}   :   {right}", align="center", font=("Comic Sans", 25, "normal"))

    def winner(self, winner):
        self.clear()
        self.up()
        self.home()
        self.write(f"{winner} won !", align="center", font=("Arial", 20, "normal"))
