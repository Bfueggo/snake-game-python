from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake = []
        x_position = 0
        for i in range(3):
            created_turtle = Turtle()
            created_turtle.color("black")
            created_turtle.penup()
            created_turtle.shape("square")
            created_turtle.goto(x_position, 0)
            self.snake.append(created_turtle)
            x_position -= 20
        self.head = self.snake[0]

    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            x = self.snake[i - 1].xcor()
            y = self.snake[i - 1].ycor()
            self.snake[i].goto(x, y)

        self.snake[0].forward(MOVE_DISTANCE)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def add_segment(self):
        created_turtle = Turtle()
        created_turtle.color("black")
        created_turtle.penup()
        created_turtle.shape("square")
        tail = self.snake[-1]
        created_turtle.goto(tail.xcor(), tail.ycor())
        self.snake.append(created_turtle)

    def did_bite_tail(self):
        for i in range(1, len(self.snake)):
            if self.head.distance(self.snake[i]) < 15:
                return True
        return False
