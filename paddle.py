from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, paddle_num):
        super().__init__()
        self.shape("square")
        self.shapesize(6, 1)
        self.penup()
        self.color("white")
        self.y_axis = 0
        if paddle_num == 1:
            self.x_axis = -560
            self.goto(self.x_axis, 0)
        else:
            self.x_axis = 560
            self.goto(self.x_axis, 0)

    def up(self):
        self.y_axis += 20
        self.goto(self.x_axis, self.y_axis)

    def down(self):
        self.y_axis -= 20
        self.goto(self.x_axis, self.y_axis)

