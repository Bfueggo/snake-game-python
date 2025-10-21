from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.goto(-110, 270)
        with open("data.txt", mode="r") as data_reader:
            self.high_score = int(data_reader.read())
        self.score = 0
        self.update_board()

    def update_board(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", font=("Arial", 16, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_board()

    def reset(self):
        if self.high_score < self.score:
            with open("data.txt", mode="w") as data_writer:
                data_writer.write(str(self.score))
                self.high_score=self.score
        self.score = 0
        self.update_board()

    def game_over(self):
        new_turtle=Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        new_turtle.color("white")
        new_turtle.speed("fastest")
        new_turtle.write("Game Over.", align="center", font=("Arial", 24, "normal"))
        self.reset()
