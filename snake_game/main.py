from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Sanke Game")

snake = Snake()
food = Food()
board = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.update()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detection collision with food

    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        board.update_score()

    # Detection collision with wall
    if snake.head.xcor()>290 or snake.head.xcor() < -290 or snake.head.ycor() >290 or snake.head.ycor() <-290:
        board.game_over()
        game_is_on = False


    # Detect Collision with tail

    for segment in snake.segment[1::]:
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 10:
            board.game_over()
            game_is_on = False














screen.exitonclick()