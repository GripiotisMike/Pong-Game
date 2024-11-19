from turtle import Turtle

class Net(Turtle):
    def __init__(self):
        """
        Initialize the net that divides the playing field into two parts.
        """
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.hideturtle()
        self.color("white")
        self.goto(0, 250)  # Start at the top-center

    def make_net(self):
        """
        Draw a dashed line (net) in the middle of the screen.
        """
        self.right(90)
        self.pensize(5)
        for i in range(20):  # 20 segments to create the dashed line
            self.pendown()
            self.forward(15)
            self.penup()
            self.forward(15)
