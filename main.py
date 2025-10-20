from turtle import Screen
import time

from food import Food
from score_board import ScoreBoard
from snake import Snake

# ---------------------------------------------------------
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("green")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.turn_left, "a")
screen.onkey(snake.turn_right, "d")

screen.update()
game_over = False
while not game_over:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        score_board.increase_score()
        snake.add_segment()
        food.spawn()
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        game_over = True
        score_board.game_over()
    if snake.did_bite_tail():
        game_over = True
        score_board.game_over()

screen.exitonclick()
