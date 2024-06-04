from turtle import Turtle


class Bar(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(1, 4)
        self.color("white")
        self.left(90)
        self.segment_list = [self]

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)
