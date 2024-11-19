from turtle import Turtle

ALIGN = "center"
FONT = ("VCR OSD Mono", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        """
        Initialize the scoreboard with both players' scores.
        """
        super().__init__()
        self.score = [0, 0]  # [Player 1, Player 2]
        self.penup()
        self.hideturtle()
        self.goto(0, 217)  # Position the scoreboard
        self.speed("fastest")
        self.color("white")
        self.shapesize(3, 3)
        self.update_score()

    def update_score(self):
        """
        Update the scoreboard with the current score.
        """
        self.clear()  # Clear previous score
        self.write(f"{self.score[0]}   {self.score[1]}", align=ALIGN, font=FONT)

    def score_increase(self, player):
        """
        Increase the score of a player (0 for player 1, 1 for player 2).
        """
        self.score[player] += 1
        self.update_score()

    def game_over(self):
        """
        Display 'Game Over' message when the game ends.
        """
        self.goto(0, 0)
        self.write("Game Over!", align=ALIGN, font=FONT)
