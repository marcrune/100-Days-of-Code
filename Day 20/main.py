from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')

# snake = Turtle(shape='square')
# snake.fillcolor('white')
# snake.penup()
# snake_body = Turtle(shape='square')
# snake_body.fillcolor('white')
# snake_body.penup()
# snake_body.setx(snake.xcor()-20)
# snake_tail = Turtle(shape='square')
# snake_tail.fillcolor('white')
# snake_tail.penup()
# snake_tail.setx(snake_body.xcor()-20)

for n in range(3):
    snake = Turtle(shape='square')
    snake.fillcolor('white')
    snake.penup()
    if n >= 1:
        snake.setx(snake.xcor()-20 * n)


screen.exitonclick()