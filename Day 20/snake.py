from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# constant to facilitate changing the code if necessary or desired
MOVE_DISTANCE = 20

class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()


    def create_snake(self):
        """creates a snake with 3 segments of size 20, color white and square shaped"""
        for n in range(3):
            snake = Turtle(shape='square')
            snake.fillcolor('white')
            snake.penup()
            if n >= 1:
                snake.setx(snake.xcor()-20*n)
            self.segments.append(snake)
            

    def move(self):
        """moves the snake by MOVE_DISTANCE constant"""
        for n in range(len(self.segments)-1, 0, -1):
            self.segments[n].goto(self.segments[n-1].pos())
        self.segments[0].forward(MOVE_DISTANCE)


    def up(self):
        """moves the snake upwards (towards 90 degrees)"""
        if self.segments[0].heading() != DOWN:
            self.segments[0].seth(UP)

    def down(self):
        """moves the snake downwards (towards 270 degrees)"""
        if self.segments[0].heading() != UP:
            self.segments[0].seth(DOWN)

    def right(self):
        """moves the snake right (towards 0/360 degrees)"""
        if self.segments[0].heading() != LEFT:
            self.segments[0].seth(RIGHT)

    def left(self):
        """moves the snake left (towards 180 degrees)"""
        if self.segments[0].heading() != RIGHT:
            self.segments[0].seth(LEFT)