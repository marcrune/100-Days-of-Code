from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.teleport(0, 260)
        self.color("white")
        self.write(f"Score = {self.score}", move=False, align="center", font=("Arial", 20, "normal"))
        self.hideturtle()


    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score = {self.score}", move=False, align="center", font=("Arial", 20, "normal"))


    def game_over(self):
        self.teleport(0, 0)
        self.write("GAME OVER", move=False, align="center", font=("Arial", 20, "normal"))