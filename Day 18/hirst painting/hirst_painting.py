# import colorgram

# colors = colorgram.extract('E:/Downloads/Programação/Python/100 Days of Code/Day 18/hirst painting/hirst_painting.jpg', 10)

# rgb_colors = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append(tuple([r, g, b]))
    
# print(rgb_colors)
from turtle import Turtle, Screen
from random import choice

screen = Screen()
screen.colormode(255)

colors_rgb = [(1, 13, 31), (52, 25, 17), (219, 127, 106), (9, 105, 160), (242, 214, 69), (150, 84, 39)]

# painting has to be 10x10; dots have size 20 and must be spaced apart by 50 units
turtle = Turtle()
turtle.pu()
turtle.teleport(-200, -200)
turtle.hideturtle()
print(turtle.position())

def hirst_painting(x, y):
    for _ in range(10):
        turtle.dot(20, choice(colors_rgb))
        turtle.teleport(turtle.xcor() + x)
    turtle.teleport(-200, turtle.ycor() + y)
    if turtle.position() == (-200, 300):
        return
    hirst_painting(x, y)

hirst_painting(50, 50)
screen.exitonclick()