from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.goto(-45, 270)
        self.score = 0
        self.update_board()

    def update_board(self):
        self.clear()
        self.write(f"Score: {self.score}", font=("Arial", 16, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_board()

    def game_over(self):
        self.home()
        self.write("Game Over.", align="center", font=("Arial", 24, "normal"))
