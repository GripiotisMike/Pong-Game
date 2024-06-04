from turtle import Turtle

ALIGN = "center"
FONT = ("VCR OSD Mono", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = [0, 0]
        self.penup()
        self.hideturtle()
        self.goto(0, 217)
        self.speed("fastest")
        self.color("white")
        self.shapesize(3, 3)
        self.write(f"{self.score[0]}   {self.score[1]}", align=ALIGN, font=FONT)

    def score_increase(self, x):
        self.score[x] += 1
        self.clear()
        self.write(f"{self.score[0]}   {self.score[1]}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game  Over!", align=ALIGN, font=FONT)
