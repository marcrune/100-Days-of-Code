from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()
    

    def update_score(self):
        """Updates the scores"""
        self.clear()
        self.teleport(-100, 200)
        self.write(f"{self.l_score}", move=False, align="center", font=("Courier", 80, "normal"))
        self.teleport(100, 200)
        self.write(f"{self.r_score}", move=False, align="center", font=("Courier", 80, "normal"))


    def l_point(self):
        """Increases left score by one and updates the scores"""
        self.l_score += 1
        self.update_score()


    def r_point(self):
        """Increases right score by one and updates the scores"""
        self.r_score += 1
        self.update_score()