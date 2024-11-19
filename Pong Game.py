from turtle import Screen
from scoreboard import ScoreBoard
from bar import Bar
from ball import Ball
from net import Net
import time

# Set up the screen
screen = Screen()
screen.bgcolor("black")
screen.title("Pong Pong")
screen.setup(800, 500)
screen.tracer(0)  # Turn off automatic screen updates for smoother gameplay

# Create game components
ball = Ball()
net = Net()
net.make_net()
scoreboard = ScoreBoard()
bar1 = Bar()
bar1.goto(380, 0)  # Position player 1's paddle
bar2 = Bar()
bar2.goto(-387, 0)  # Position player 2's paddle

# Listen for key presses to control paddles
screen.listen()
screen.onkeypress(bar2.move_up, "q")
screen.onkeypress(bar2.move_down, "a")
screen.onkeypress(bar1.move_up, "o")
screen.onkeypress(bar1.move_down, "l")

counter = 0
game_on = True
while game_on:
    screen.update()  # Update the screen after every movement
    time.sleep(ball.move_speed)  # Adjust speed of the game loop
    if -230 < ball.ycor() < 230:  # If ball is within bounds, move it
        ball.move_ball()
    else:  # Bounce ball off top/bottom walls
        ball.bounce_y()
        ball.move_ball()

    # Ball collision with paddles
    if ball.distance(bar1) < 50 and ball.xcor() == 360:
        ball.bounce_x()
        ball.move_ball()
    if ball.distance(bar2) < 50 and ball.xcor() == -367:
        ball.bounce_x()
        ball.move_ball()

    # Ball out of bounds
    if ball.xcor() > 390:
        ball.reset_ball_x()
        scoreboard.score_increase(1)  # Player 2 scores
        counter += 1
    elif ball.xcor() < -390:
        ball.reset_ball_y()
        scoreboard.score_increase(0)  # Player 1 scores
        counter += 1

    # End game if score exceeds 9
    if counter > 9:
        game_on = False
        scoreboard.game_over()

screen.exitonclick()
