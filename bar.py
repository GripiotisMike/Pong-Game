from turtle import Turtle

class Bar(Turtle):
    def __init__(self):
        """
        Initialize the bar (paddle) with position and size.
        """
        super().__init__()
        self.penup()
        self.shape("square")  # Use square shape for the paddle
        self.shapesize(1, 4)  # Size of the paddle (height, width)
        self.color("white")
        self.left(90)  # Rotate to make it vertical
        self.segment_list = [self]  # List to store segments of the paddle

    def move_up(self):
        """
        Move the paddle up by 20 units.
        """
        self.forward(20)

    def move_down(self):
        """
        Move the paddle down by 20 units.
        """
        self.backward(20)
