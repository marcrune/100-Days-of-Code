from turtle import Screen
from paddle import Paddle
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800, height=600)
screen.tracer(0)

# First paddle
first_paddle = Paddle(350, 0)
second_paddle = Paddle(-350, 0)

screen.listen()
screen.onkey(first_paddle.up, "Up")
screen.onkey(first_paddle.down, "Down")
screen.onkey(second_paddle.up, "w")
screen.onkey(second_paddle.down, "s")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()