from turtle import Turtle


class Net(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.hideturtle()
        self.color("white")
        # self.shapesize(5, 5)
        self.goto(0, 250)

    def make_net(self):
        self.right(90)
        self.pensize(5)
        for i in range(20):
            self.pendown()
            self.forward(15)
            self.penup()
            self.forward(15)
