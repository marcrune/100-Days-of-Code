from turtle import Turtle

# Creating the Scoreboard class inheriting from the Turtle class, setting it as a text and its position
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.teleport(x=-270, y=250)
        self.write(f"Level = {self.level}", align="left", font=("Courier", 20, "bold"))
    

    def update_score(self):
        """Adds one to the score and updates the scoreboard"""
        self.level += 1
        self.clear()
        self.write(f"Level = {self.level}", align="left", font=("Courier", 20, "bold"))


    def game_over(self):
        """Prints the game over screen"""
        self.home()
        self.write(f"Game Over!", align="center", font=("Courier", 20, "bold"))


