from turtle import Turtle
from snake_logging import logger_snake

MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-1 * MOVE_DISTANCE, 0), (-2 * MOVE_DISTANCE, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self, screen):
        logger_snake.info("Initializing a Snake object")
        self.screen = screen
        self.screen_width = screen.window_width()
        self.screen_height = screen.window_height()

        self.move_distance = MOVE_DISTANCE
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

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
    def move(self):
        # move all but head to the position closer to the head
        for s in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[s - 1].xcor()
            new_y = self.segments[s - 1].ycor()
            self.segments[s].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def add_segment(self, position):
        t = Turtle("square")
        t.color("white")
        t.penup()
        t.goto(position)
        self.segments.append(t)

    def out_of_bounds(self):
        x_limit = self.screen_width / 2 - self.move_distance
        y_limit = self.screen_height / 2 - self.move_distance
        # print(f"out_of_bounds() - x_limit: {x_limit}, y_limit: {y_limit}")

        if abs(self.head.xcor()) > x_limit or \
           abs(self.head.ycor()) > y_limit:
            return True
        else:
            return False
