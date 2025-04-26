from turtle import Screen
from paddles import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

delay_time = 0.1

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

l_score = 0
r_score = 0

dotted_lines = Scoreboard()
dotted_lines.draw_dotted_line()
scoreboard = Scoreboard()
scoreboard.write_score()

r_paddle = Paddle((370, 0))
l_paddle = Paddle((-370, 0))
ball = Ball()

screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")
screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")
game_on = True

while game_on:
    ball.move()
    screen.update()
    time.sleep(delay_time)

    if ball.ycor() >= 285 or ball.ycor() <= -280:
        ball.bounce()

    if ball.xcor() > 345 and ball.distance(r_paddle) < 58:
        ball.paddle_bounce()
        if delay_time > 0.005:
            delay_time -= 0.005

    if ball.xcor() < -345 and ball.distance(l_paddle) < 58:
        ball.paddle_bounce()
        if delay_time > 0.005:
            delay_time -= 0.01

    if ball.xcor() > 380:
        ball.generate_ball()
        l_score += 1
        scoreboard.write_score(l_score, r_score)
        r_paddle.goto(370, 0)
        l_paddle.goto(-370, 0)
        delay_time = 0.1
        time.sleep(1)

    if ball.xcor() < -390:
        ball.generate_ball()
        r_score += 1
        scoreboard.write_score(l_score, r_score)
        r_paddle.goto(370, 0)
        l_paddle.goto(-370, 0)
        delay_time = 0.1
        time.sleep(1)

    if l_score == 10:
        dotted_lines.clear()
        scoreboard.winner("Left")
        break
    elif r_score == 10:
        dotted_lines.clear()
        scoreboard.winner("Right")
        break

screen.exitonclick()
