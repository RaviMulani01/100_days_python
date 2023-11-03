import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
car_manager = CarManager()
score_board = Scoreboard()


screen.listen()
screen.onkey(player.turtle_move_upside, "Up")


game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()

    car_manager.create_car() 
    car_manager.car_move()


    # Detect collition with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score_board.game_over()


    # detect car cross the finish line
    if player.is_player_at_finish_line():
        score_board.update_point()
        player.start_postion()
        car_manager.level_up()

  
screen.exitonclick()