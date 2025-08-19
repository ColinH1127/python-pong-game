from turtle import Screen
from src.game import Ball, Paddle



SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("pong")

ball = Ball()
paddle1 = Paddle(1)
paddle2 = Paddle(2)
screen.onkey(paddle1.up, "w")
screen.onkey(paddle2.up, "Up")
screen.onkey(paddle1.down, "s")
screen.onkey(paddle2.down, "Down")

score1 = 0
score2 = 0


def game_loop():
    game_is_on = True
    while game_is_on:
        ball.ball_move()
        if paddle1.distance(ball) < 20 or paddle2.distance(ball) < 20:
            ball.ball_bounce()
        if ball.xcor() > 590 or ball.xcor() < -590:
            game_is_on = False




screen.listen()
screen.onkey(game_loop, "Return")









screen.exitonclick()
