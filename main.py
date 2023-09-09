"""
Using this project to practice Git usage and for Python coding practice
"""
# TODO research how to do configurable debug prints and instrument code with debug output
# TODO figure out how to "flash" messages to the player

# external modules
from turtle import Screen
import time

# project modules
from snake import Snake
from food import Food
from scoreboard import Scoreboard

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_BG_COLOR = "black"

GAME_TITLE = "My Snake Game V1.0"
GAME_SPEED_DELAY = {"fast": 0.1, "normal": 0.3, "slow": 0.5}
GAME_DEFAULT_SPEED = "normal"

# create and initialize the screen
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(SCREEN_BG_COLOR)
screen.title(GAME_TITLE)
screen.tracer(0)

# setup default game delay
game_speed = GAME_DEFAULT_SPEED
game_delay = GAME_SPEED_DELAY[game_speed]
print(f"Starting speed/delay: {game_speed}/{game_delay}")


# non-control handler functions
def speed_up():
    # TODO refactor to use current state and globals to avoid hard coding values
    global game_speed, game_delay

    if game_speed == "slow":
        game_speed = "normal"
    elif game_speed == "normal":
        game_speed = "fast"

    game_delay = GAME_SPEED_DELAY[game_speed]
    print(f"In speed_up() - now {game_speed}/{game_delay}")


def speed_down():
    # TODO refactor to use current state and globals to avoid hard coding values
    global game_speed, game_delay

    if game_speed == "fast":
        game_speed = "normal"
    elif game_speed == "normal":
        game_speed = "slow"

    game_delay = GAME_SPEED_DELAY[game_speed]
    print(f"In speed_down() - now {game_speed}/{game_delay}")


# create project objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# handle game control keys
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# handle non-control keys
screen.onkey(speed_up, "Prior")
screen.onkey(speed_down, "Next")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(game_delay)
    snake.move()
    scoreboard.refresh()

    # TODO add Snake method that makes this cleaner - Snake.head_on_food()?
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.bump()
    # TODO clean this up by adding a Snake method - Snake.out_of_bounds()?
    if snake.head.xcor() > 280 or \
       snake.head.xcor() < -280 or \
       snake.head.ycor() > 280 or \
       snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

# Leave screen up until user clicks
screen.exitonclick()
