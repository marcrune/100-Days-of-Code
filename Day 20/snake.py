from turtle import Turtle

# constant to facilitate changing the code if necessary or desired
MOVE_DISTANCE = 20

class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        """creates a snake with 3 segments of size 20 and color white"""
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