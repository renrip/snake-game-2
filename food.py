from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        rand_x = randint(-280, 280)
        rand_y = randint(-280, 280)
        centered_x = int(rand_x - (rand_x % 20))
        centered_y = int(rand_y - (rand_y % 20))
        self.goto_centered_spot()

    def goto_centered_spot(self):
        rand_x = randint(-280, 280)
        rand_y = randint(-280, 280)
        centered_x = int(rand_x - (rand_x % 20))
        centered_y = int(rand_y - (rand_y % 20))
        self.goto(centered_x, centered_y)

    def refresh(self):
        self.goto_centered_spot()