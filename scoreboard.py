from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.speed("fastest")
        self.goto(0, 265)
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def add_point(self):
        self.score += 1
        self.update_scoreboard()
