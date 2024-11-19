from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        """
        Initialize the ball with random movement direction and speed.
        """
        super().__init__()
        self.penup()
        self.color("red")
        self.shape("circle")
        self.goto(0, 0)  # Start position
        self.shapesize(1, 1)  # Set the size of the ball
        self.setheading(random.randint(2, 358))  # Random direction on spawn
        self.speed("fast")  # Set initial speed
        self.move_speed = 0.1  # Initial move speed

    def move_ball(self):
        """
        Move the ball forward by 10 units in the current direction.
        """
        self.forward(10)

    def bounce_y(self):
        """
        Bounce the ball in the opposite Y direction.
        """
        current_heading = int(self.heading())
        self.setheading(360 - current_heading)  # Invert the Y-axis heading

    def bounce_x(self):
        """
        Bounce the ball in the opposite X direction and increase the speed.
        """
        current_heading = int(self.heading())
        self.setheading(180 - current_heading)  # Invert the X-axis heading
        self.move_speed *= 0.9  # Increase speed gradually

    def reset_ball_x(self):
        """
        Reset the ball's position and direction on the X-axis.
        """
        self.goto(0, 0)  # Reset position
        self.setheading(random.randint(2, 358))  # Random direction
        self.move_speed = 0.1  # Reset speed

    def reset_ball_y(self):
        """
        Reset the ball's position and direction on the Y-axis.
        """
        self.goto(0, 0)  # Reset position
        self.setheading(random.randint(2, 358))  # Random direction
        self.move_speed = 0.1  # Reset speed
