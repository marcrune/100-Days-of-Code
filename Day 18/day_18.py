from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.colormode(255)

timmy_the_turtle = Turtle()
timmy_the_turtle.shape('turtle')
timmy_the_turtle.color('red')

x = 100
turn = 90

# square
# for _ in range(4):
#     timmy_the_turtle.forward(x)
#     timmy_the_turtle.right(turn)

# dotted line
# for _ in range (10):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()

# shapes with different colors
# sides = 3
# iteration = 0
# drawing = True
# timmy_the_turtle.pencolor(randint(1, 255), randint(1, 255), randint(1, 255))

# while drawing:
#     for _ in range(sides): 
#         timmy_the_turtle.right(360/sides)
#         timmy_the_turtle.forward(100)
#         iteration += 1
#         if iteration == 10:
#             drawing = False
#         elif iteration == sides:
#             sides += 1
#             iteration = 0
#             timmy_the_turtle.pencolor(randint(1, 255), randint(1, 255), randint(1, 255))

# timmy_the_turtle.width(4)
timmy_the_turtle.speed(0)

# random walk
# def walk_east(turtle):
#     turtle.forward(100)


# def walk_west(turtle):
#     turtle.left(180)
#     turtle.forward(100)
#     turtle.right(180)


# def walk_north(turtle):
#     turtle.left(90)
#     turtle.forward(100)
#     turtle.right(90)


# def walk_south(turtle):
#     turtle.right(90)
#     turtle.forward(100)
#     turtle.left(90)


# random_walk = [walk_east, walk_north, walk_west, walk_south]

# count = 0
# while count < 50:
#     random_walk[randint(0, 3)](timmy_the_turtle)
#     timmy_the_turtle.pencolor(randint(1, 255), randint(1, 255), randint(1, 255))
#     count += 1

# other method - needs a list of colors and importing the choice method from the random library
# directions = [0, 90, 180, 270]
# timmy_the_turtle.pensize(15)
# timmy_the_turtle.speed("fastest")

# for _ in range(200):
#     timmy_the_turtle.color(random.choice(colours))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

# spirograph
# while timmy_the_turtle.heading() <= 355:
#     timmy_the_turtle.pencolor(randint(1, 255), randint(1, 255), randint(1, 255))
#     timmy_the_turtle.circle(100)
#     timmy_the_turtle.left(5)
#     if timmy_the_turtle.heading() == 0:
#         break


screen.exitonclick()