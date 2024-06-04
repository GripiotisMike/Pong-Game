from turtle import Screen
from scoreboard import ScoreBoard
from bar import Bar
from ball import Ball
from net import Net
import time


screen = Screen()
screen.bgcolor("black")
screen.title("Pong Pong")
screen.setup(800, 500)
screen.tracer(0)

ball = Ball()
net = Net()
net.make_net()
scoreboard = ScoreBoard()
bar1 = Bar()
bar1.goto(380, 0)
bar2 = Bar()
bar2.goto(-387, 0)

screen.listen()
screen.onkeypress(bar2.move_up, "q")
screen.onkeypress(bar2.move_down, "a")
screen.onkeypress(bar1.move_up, "o")
screen.onkeypress(bar1.move_down, "l")

counter = 0
game_on = True
while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    if -230 < ball.ycor() < 230:
        ball.move_ball()
    else:
        ball.bounce_y()
        ball.move_ball()
    if ball.distance(bar1) < 50 and ball.xcor() == 360:
        ball.bounce_x()
        ball.move_ball()
    if ball.distance(bar2) < 50 and ball.xcor() == -367:
        ball.bounce_x()
        ball.move_ball()
    if ball.distance(bar1) < 20 or ball.distance(bar2) < 20:
        ball.bounce_x()
        ball.move_ball()
    if ball.xcor() > 390:
        ball.reset_ball_x()
        scoreboard.score_increase(1)
        counter += 1
        screen.update()
    elif ball.xcor() < -390:
        ball.reset_ball_y()
        scoreboard.score_increase(0)
        counter += 1
        screen.update()
    if counter > 9:
        game_on = False


screen.exitonclick()
