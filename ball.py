from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(600, 0)
        self.ball_speed = "fastest"
        self.speed(self.ball_speed)
        self.ball_heading = 150

    def ball_move(self):
        self.showturtle()
        self.setheading(self.ball_heading)
        self.forward(10)
        if self.ycor() >= 380:
            self.ball_bounce()
        if self.ycor() <= -380:
            self.ball_bounce()


    def ball_bounce(self):
        self.ball_heading = 360 - self.ball_heading
        self.setheading(self.ball_heading)

