from turtle import Turtle
from snake_logging import logger_scoreboard

HIGH_SCORE_FILENAME: str = "snake_high_score.txt"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        logger_scoreboard.info("Initializing a Scoreboard object")
        self.score = 0

        # Get existing high score from file if it exists
        try:
            with open(HIGH_SCORE_FILENAME) as file:
                contents = file.read()
                if contents.isdigit():
                    self.high_score = int(contents)
                else:
                    self.high_score = 0
        except OSError:
            self.high_score = 0
        except:
            self.high_score = 0

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
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=('Arial', 16, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(HIGH_SCORE_FILENAME, mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER!", align="center", font=('Arial', 16, 'normal'))
