from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.teleport(0, 260)
        self.color("white")
        self.write(f"Score = {self.score}", move=False, align="center", font=("Arial", 20, "normal"))
        self.hideturtle()


    def update_score(self):
        """clears the score and writes it again updating both the score and high score"""
        self.clear()
        self.write(f"Score = {self.score} High Score = {self.high_score}", move=False, align="center", font=("Arial", 20, "normal"))


    def reset(self):
        """updates high score if needed and resets the scoreboard"""
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_score()


    def increase_score(self):
        """increases score by 1 and calls the update_score() function"""
        self.score += 1
        self.update_score()


    # def game_over(self):
    #     self.teleport(0, 0)
    #     self.write("GAME OVER", move=False, align="center", font=("Arial", 20, "normal"))