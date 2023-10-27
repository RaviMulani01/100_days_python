from turtle import Turtle, Screen
import random

screen = Screen()
# set up the screen size
screen.setup(width=500, height=400)

is_race_on = False

# taking input from user
user_bet = screen.textinput(title="Make Your Bat", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)

def turtle_move(turtle_name):
    turtle_name.forward(random.randint(0,10))


colors = ["red", "orange", "yellow", "green", "blue", "pink"]
y_postioin = [150, 100, 50, 0, -50, -100]

turtle_list = []

for turtle_index in range (6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.setposition(-240,y_postioin[turtle_index])
    turtle_list.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtle_list:

        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()

            if user_bet == winning_color:
                print(f"You've won! The  {winning_color} turtle is the winner!")

            else:
                print(f"You've lose! The  {winning_color} turtle is the winner!")

            break
        else:
            turtle_move(turtle)

screen.exitonclick()
