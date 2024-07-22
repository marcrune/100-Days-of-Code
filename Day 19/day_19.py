# etch-a-sketch
from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

def move_forward():
    turtle.forward(10)

def move_backwards():
    turtle.backward(10)

def turn_left():
    turtle.left(5)

def turn_right():
    turtle.right(5)

def clear_drawing():
    turtle.reset()

screen.listen()

# função onkeypress() é uma higher order function porque recebe outra função como parâmetro
screen.onkeypress(fun=move_forward, key='Up')
screen.onkeypress(fun=move_backwards, key='Down')
screen.onkeypress(fun=turn_left, key='Left')
screen.onkeypress(fun=turn_right, key='Right')
screen.onkeypress(fun=clear_drawing, key='c')

screen.exitonclick()