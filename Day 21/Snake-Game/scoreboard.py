from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 16, "normal")

class ScoreBoard(Turtle):
    
    
    def __init__(self):
        super().__init__()
        self.score = 0

        with open("data.txt") as data:
            self.high_score = int(data.read())

        self.color("white")
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.goto(0, 270)
        self.update_scoreboard()
     

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score}, High Score: {self.high_score}", align=ALIGNMENT, font=FONT)


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

            with open("data.txt", mode='w') as data:
                # new_high_score = str(self.high_score)
                data.write(f"{self.high_score}")

        self.score = 0
        self.update_scoreboard()


    def increse_score(self):
        self.score += 1
        self.update_scoreboard()
        
