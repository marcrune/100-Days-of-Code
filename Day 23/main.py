from scoreboard import Scoreboard
from turtle import Screen
from player import Player
from cars import Car
import time

# Setting up the Screen object and its attributes
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Creating the player, scoreboard and cars objects
player = Player()
scoreboard = Scoreboard()
cars = Car()

# Listening for keystrokes
screen.listen()
screen.onkeypress(player.move_up, "Up")

# Game logic
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_forward()

    # Updates the score when the player reaches the upper limit of the screen and resets player's position
    if player.reached_goal():
        scoreboard.update_score()
        cars.speed_up()

    # Detecting collision with the cars
    for car in cars.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()