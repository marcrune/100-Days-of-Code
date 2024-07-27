from turtle import Turtle

class Paddle(Turtle):
    
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.teleport(x, y)
    
    def up(self):
        """Move upwards (towards 90 degrees)"""
        self.sety(self.ycor() + 20)

    def down(self):
        """move downwards (towards 270 degrees)"""
        self.sety(self.ycor() - 20)
