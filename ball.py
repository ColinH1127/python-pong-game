from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

        self.goto(-580, -380)
        self.ball_speed = 5
        self.speed(self.ball_speed)
        self.x_move = 10
        self.y_move = 10


    def ball_move(self):

        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)






    def bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1



