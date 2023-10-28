from turtle import Turtle


START_POSTION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snack:


    def __init__(self):
        self.turtle_list = []
        self.create_snake()
        self.head = self.turtle_list[0]


    def move(self):
        for snake_number in range(len(self.turtle_list)-1, 0, -1):
            new_x = self.turtle_list[snake_number - 1].xcor()
            new_y = self.turtle_list[snake_number - 1].ycor()
            self.turtle_list[snake_number].goto(new_x, new_y)

        self.turtle_list[0].forward(MOVE_DISTANCE)


    def create_snake(self):
        for postion in START_POSTION:
            new_turtle = Turtle(shape="square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(postion)
            self.turtle_list.append(new_turtle)

    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)