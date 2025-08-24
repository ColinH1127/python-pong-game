from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 250)
        self.write(self.l_score, align="center", font=("courier", 50, "normal"))
        self.goto(100, 250)
        self.write(self.r_score, align="center", font=("courier", 50, "normal"))

    def l_point(self):
        self.clear()
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.clear()
        self.r_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        if self.r_score >= 11:
            self.write(f"Game Over!\n Player 1 wins!", align="center", font=("courier", 50, "normal"))
        elif self.l_score >= 11:
            self.write(f"Game Over!\n Player 2 wins!", align="center", font=("courier", 50, "normal"))

