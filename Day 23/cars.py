from turtle import Turtle
from random import choice, randint

# Creating a color list for the cars
color_list = ["red", "blue", "green", "yellow", "black", "violet", "orange"]

# Creating the Car class inheriting from the Turtle class
class Car:
    def __init__(self):
        self.all_cars = []
        self.move_speed = 10


    def create_car(self):
        """Creates a car that is a Turtle object."""
        if randint(1, 6) == 1:
            car = Turtle(shape="square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(choice(color_list))
            car.teleport(320, y=randint(-230, 230))
            car.setheading(180)
            self.all_cars.append(car)

    def move_forward(self):
        """Moves the cars forward (towards 180 degrees)."""
        for car in self.all_cars:
            car.forward(self.move_speed)

    
    def speed_up(self):
        """Speeds up the cars' movement speed by 10 units."""
        self.move_speed += 10