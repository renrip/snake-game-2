from turtle import Turtle
from snake_logging import logger_scoreboard

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        logger_scoreboard.info("Initializing a Scoreboard object")
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.refresh()

    def bump(self):
        self.score +=1
        self.refresh()


    def refresh(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=('Arial', 16, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", align="center", font=('Arial', 16, 'normal'))
