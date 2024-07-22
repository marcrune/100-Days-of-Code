from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title='Make a bet', prompt='Which turtle will win the race? Enter a color: ')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtles = []
starting_y = -100

for index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[index])
    new_turtle.goto(-230, starting_y)
    starting_y += 40
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() > 230:
            is_race_on = False
            if user_bet == turtle.pencolor():
                print(f"You've won! The {turtle.pencolor()} turtle was the winner!")
            else:
                print(f"You've lost! The {turtle.pencolor()} turtle was the winner!")
            
    

screen.exitonclick()