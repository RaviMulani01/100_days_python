from turtle import Turtle, Screen
import random
turtle = Turtle()
screen = Screen()

screen.colormode(255)
turtle.speed("fastest")
turtle.penup()
turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)
turtle.hideturtle()

color = [(226, 229, 235), (244, 237, 222), (243, 234, 240), 
        (232, 242, 237), (192, 165, 115), (138, 166, 190), 
        (56, 102, 140), (141, 91, 50), (12, 23, 55), 
        (222, 207, 123), (182, 154, 42), (61, 22, 11), 
        (182, 146, 165), (142, 177, 151), (72, 117, 81), 
        (58, 15, 26), (126, 79, 102), (130, 30, 16), 
        (15, 39, 23), (24, 53, 127), (177, 188, 215), 
        (164, 104, 134), (115, 31, 46), (97, 150, 100), (98, 121, 172)]

# for i in range(11):
#     turtle.pendown()
#     for j in range(10):
#         turtle.dot(20, random.choice(color))
#         turtle.penup()
#         turtle.forward(50)

#     turtle.setheading(90)
#     turtle.forward(50)
#     turtle.setheading(180)
#     turtle.forward(500)
#     turtle.setheading(0)

number_of_dots = 100

for i in range(1,number_of_dots+1):
    turtle.pendown()

    turtle.dot(20, random.choice(color))
    turtle.penup()
    turtle.forward(50)

    if i % 10 == 0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)


screen.exitonclick()
