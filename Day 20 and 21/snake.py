from turtle import Turtle

# constants to facilitate changing the code if necessary or desired
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
MOVE_DISTANCE = 20
STARTING_POSITIONS = [(20, 0), (0, 0), (-20, 0)]

class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()


    def create_snake(self):
        """creates a snake with 3 segments of size 20, color white and square shaped"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """adds a new segment to the snake after it eats a food piece to the position argument"""
        new_segment = Turtle(shape='square')
        new_segment.fillcolor('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """extends the snake by adding the newer segment to the last position of the segments list"""
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

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