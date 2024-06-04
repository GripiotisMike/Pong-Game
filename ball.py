from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("red")
        self.shape("circle")
        self.goto(0, 0)
        self.shapesize(1, 1)
        self.setheading(random.randint(2, 358))
        self.speed("fast")
        self.move_speed = 0.1

    def move_ball(self):
        self.forward(10)

    def bounce_y(self):
        current_heading = int(self.heading())
        self.setheading(360 - current_heading)

    def bounce_x(self):
        current_heading = int(self.heading())
        self.setheading(180 - current_heading)
        self.move_speed *= 0.9

    def reset_ball_x(self):
        self.goto(0, 0)
        self.setheading(random.randint(2, 358))
        self.move_speed = 0.1

    def reset_ball_y(self):
        self.goto(0, 0)
        self.setheading(random.randint(2, 358))
        self.move_speed = 0.1
