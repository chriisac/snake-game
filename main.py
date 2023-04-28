from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_over = False
while not game_over:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # detect collision with food.
    if snake.head.distance(food) < 15:
        scoreboard.add_point()
        snake.extend()
        food.refresh()

    # Detect Collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # detect collision with tail.
    for segment in snake.segments[1:-1]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
