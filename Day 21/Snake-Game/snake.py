from turtle import Turtle


START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
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


    def create_snake(self):
        for position in START_POSITION:
            self.add_segment(position)


    def add_segment(self, position):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.turtle_list.append(new_turtle)


    def reset(self):
        for seg in self.turtle_list:
            seg.goto(1000,1000)
        self.turtle_list.clear()
        self.create_snake()
        self.head = self.turtle_list[0]


    def extend(self):
        self.add_segment(self.turtle_list[-1].position())


    def move(self):
        for snake_number in range(len(self.turtle_list)-1, 0, -1):
            new_x = self.turtle_list[snake_number - 1].xcor()
            new_y = self.turtle_list[snake_number - 1].ycor()
            self.turtle_list[snake_number].goto(new_x, new_y)

        self.turtle_list[0].forward(MOVE_DISTANCE)


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