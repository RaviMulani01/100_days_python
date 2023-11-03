from turtle import Screen
import time
from snake import Snack
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
food = Food()
score_board = ScoreBoard()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

screen.tracer(0) 

snake = Snack()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increse_score()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_board.reset()
        snake.reset()
       
        

    # detect collision with tail
    for segment in snake.turtle_list[1:]:
        if snake.head.distance(segment) < 18:
            score_board.reset()
            snake.reset()
      

screen.exitonclick()