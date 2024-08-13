from turtle import Turtle
from random import choice, randint

# Creating a color list for the cars
color_list = ["red", "blue", "green", "yellow", "black", "violet", "orange"]

# Creating the Car class inheriting from the Turtle class
class Car(Turtle):
    def __init__(self):
        super().__init__(shape="square")
        self.penup()
        self.color(choice(color_list))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.teleport(320, y=randint(-260, 260))
        self.setheading(180)
    

    def move_forward(self):
        """Moves the cars forward (towards 180 degrees)"""
        self.forward(10)


    def speed_up(self):
        self.acceleration = 0.1
        return self.acceleration * 0.8