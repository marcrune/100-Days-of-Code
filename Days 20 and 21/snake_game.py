from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=800)
screen.tracer(0)
screen.bgcolor('black')
screen.title('My Snake Game')

segments = []

for i in range(3):
    turtle = Turtle(shape='square')
    turtle.penup()
    turtle.color('white')
    if i > 0:
        turtle.setx(turtle.xcor() - i * 20)
    segments.append(turtle)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segments)-1, 0, -1):
        segments[seg_num].goto(segments[seg_num-1].xcor(), segments[seg_num-1].ycor())
    segments[0].forward(20)
    segments[0].left(90)
        












screen.exitonclick()