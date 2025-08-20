from turtle import Screen
import time
from src.game import Ball, Paddle



SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)
ball = Ball()
paddle1 = Paddle(1)
paddle2 = Paddle(2)

screen.listen()
screen.onkey(paddle1.up, "w")
screen.onkey(paddle2.up, "Up")
screen.onkey(paddle1.down, "s")
screen.onkey(paddle2.down, "Down")

score1 = 0
score2 = 0



game_is_on = True
while game_is_on:
    ball.ball_move()
    time.sleep(0.1)
    screen.update()
    if paddle1.distance(ball) < 20 or paddle2.distance(ball) < 20:
        ball.paddle_bounce()
    if ball.xcor() > 590:
        score1 += 1
    elif ball.xcor() < -590:
        score2 += 1
    if ball.ycor() >= 380:
        ball.bounce()
    if ball.ycor() <= -380:
        ball.bounce()

















screen.exitonclick()
