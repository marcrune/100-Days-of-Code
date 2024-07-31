from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__(shape="circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    
    def move(self):
        """Ball moves towards right paddle"""
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    
    def bounce_y(self):
        """Reverses y coordinate direction"""
        self.y_move *= -1
            

    def bounce_x(self):
        """Reverses x coordinate direction and increases ball speed"""
        self.x_move *= -1
        self.move_speed *= 0.9

    
    def reset_position(self):
        """Resets ball position to the center of the screen (0, 0) and sends it towards the opposite x coordinate direction"""
        self.home()
        self.bounce_x()
        self.move_speed = 0.1