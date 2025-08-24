from turtle import Screen
import time
from src.game import Ball, Paddle, Scoreboard



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
scoreboard = Scoreboard()

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
    time.sleep(0.07)
    screen.update()
    if paddle1.distance(ball) < 60 and ball.xcor() < -540 or paddle2.distance(ball) < 60 and ball.xcor() > 540:
        ball.paddle_bounce()
    if ball.xcor() > 590:
        scoreboard.l_point()
        time.sleep(2)
        ball.reset_ball()
        score1 += 1
    elif ball.xcor() < -590:
        scoreboard.r_point()
        time.sleep(2)
        ball.reset_ball()
        score2 += 1
    if ball.ycor() >= 380:
        ball.bounce()
    if ball.ycor() <= -380:
        ball.bounce()

    if score1 >= 11 or score2 >= 11:
        scoreboard.game_over()
        game_is_on = False



















screen.exitonclick()
