from scoreboard import Scoreboard
from turtle import Screen
from player import Player
from cars import Car
import time

# Setting up the Screen class and its attributes
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Creating the player, scoreboard and cars objects
player = Player()
scoreboard = Scoreboard()
car = Car()

# Listening for keystrokes
screen.listen()
screen.onkeypress(player.move_up, "Up")

# Game logic
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    car.move_forward()

    # Defining the upper limit of the screen and updating score when player reaches the limit
    if player.ycor() > 280:
        player.reset_position()
        scoreboard.update_score()
        # increase cars' speed (change sleeping time)


screen.exitonclick()