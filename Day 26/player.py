from turtle import Turtle

# Creating the Player class inheriting from the Turtle class and setting its heading and position (the turtle can only move upwards)
class Player(Turtle):
    def __init__(self):
        super().__init__(shape="turtle")
        self.penup()
        self.setheading(90)
        self.teleport(x=0, y=-260)


    def move_up(self):
        """Moves the player object upwards (towards 90 degrees)"""
        self.forward(10)


    def reset_position(self):
        """Resets the player to the original position"""
        self.teleport(x=0, y=-260)