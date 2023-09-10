from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self, screen, snake):
        super().__init__()
        self.screen = screen
        self.screen_width = screen.window_width()
        self.screen_height = screen.window_height()
        self.snake = snake
        self.move_distance = snake.move_distance
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.goto_centered_spot()

    def goto_centered_spot(self):
        """Place food at new random location on screen"""
        # TODO ensure that new food position is not on top of any of the snake

        # calc extents that align exactly with where snake segments can be
        # ( these will have to be multiplied by the move_distance )
        x_extent = (self.screen_width / 2 / self.move_distance) - 1
        y_extent = (self.screen_height / 2 / self.move_distance) - 1
        # print(f"x_extent: {x_extent}, y_extent: {y_extent}")

        # generate positions that will stay 1 back from the screen edge
        rand_x = randint(-1 * x_extent, x_extent)
        rand_y = randint(-1 * y_extent, y_extent)
        # print(f"rand_x: {rand_x}, rand_y: {rand_y}")

        # expand by move_distance and move self
        self.goto(rand_x * self.move_distance, rand_y * self.move_distance)

    def refresh(self):
        """Move food to new random location"""
        self.goto_centered_spot()
