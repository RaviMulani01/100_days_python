from turtle import Turtle, Screen
import random
turtle = Turtle()
screen = Screen()
# turtle.shape("turtle")


# # draw dash line using turtle
# for line in range(20):
#     turtle.forward(10)
#     turtle.color("white")
#     turtle.forward(10)
#     turtle.color("black")
# for _ in range(20):
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(10)
#     turtle.pendown()

# print different shape   
# shape = {
#     "triangle":{
#         "range": 3,
#         "angle": 120
#     },
#     "square":{
#         "range": 4,
#         "angle": 90 
#     }, 
#     "pentagone":{
#         "range": 5,
#         "angle": 72
#     }, 
#     "hetagon":{
#         "range": 6,
#         "angle": 60
#     }, 
#     "heptagon":{
#         "range": 7,
#         "angle": 51.43
#     },
#     "octagon":{
#         "range": 8,
#         "angle": 45
#     }, 
#     "nonagon":{
#         "range": 9,
#         "angle": 40
#     }, 
#     "decagon":{
#         "range": 10,
#         "angle": 36
#     }}

# color=["CornflowerBlue","MidnightBlue","GreenYellow","AliceBlue","Lime","SkyBlue","DarkOrange"]
# angle = [0, 90, 180, 270]
# for i in shape:
#     for _ in range(shape[i]["range"]):
#         turtle.forward(100)
#         turtle.right(shape[i]["angle"])
     
# def draw_shape(num_side):
#     angle = 360 / num_side
#     for _ in range(num_side):
#         turtle.forward(100)
#         turtle.right(angle)

# for i in range(3,11):
#    turtle.color(random.choice(color))
#    draw_shape(i)

# # random color genretor (RGB COLOR)
screen.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)

# # random walk pattern using turtle

# turtle.pensize(15)
# turtle.speed("fastest")
# for i in range(200):

#     # generate different RGB COLOR
#     turtle.pencolor(random_color())
#     turtle.forward(30)
#     turtle.setheading(random.choice(angle))

turtle.speed("fastest")

# draw spirograph
for i in range(0,360,5):
    turtle.setheading(i)
    turtle.color(random_color())
    turtle.circle(100)



screen.exitonclick()