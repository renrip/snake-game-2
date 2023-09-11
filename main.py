"""
Using this project to practice Git usage and for Python coding practice
"""
# TODO figure out how to "flash" messages to the player -or- mod scoreboard to also display current speed

# external modules
from turtle import Screen
import time
from snake_logging import logger_main

# project modules
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Constants
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
    """adjust speed globals faster if not already 'fastest'"""
    global game_speed, game_delay

    if game_speed == "slow":
        game_speed = "normal"
    elif game_speed == "normal":
        game_speed = "fast"

    game_delay = GAME_SPEED_DELAY[game_speed]
    print(f"In speed_up() - now {game_speed}/{game_delay}")


def speed_down():
    """adjust speed globals slower if not already 'slowest'"""
    global game_speed, game_delay

    if game_speed == "fast":
        game_speed = "normal"
    elif game_speed == "normal":
        game_speed = "slow"

    game_delay = GAME_SPEED_DELAY[game_speed]
    print(f"In speed_down() - now {game_speed}/{game_delay}")


# create project objects
snake = Snake(screen)
food = Food(screen, snake)
scoreboard = Scoreboard()

# handle game control keys
screen.listen()
# TODO enhance key handlers to only apply one direction change per cycle. build queue of dir changes
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# handle non-control keys
screen.onkey(speed_up, "Prior") #PgUp
screen.onkey(speed_down, "Next") #PgDn

game_is_on = True

logger_main.info(f"Starting main game loop")

while game_is_on:
    screen.update()
    scoreboard.refresh()
    time.sleep(game_delay)

    # check if snake is out of bounds
    if snake.out_of_bounds():
        logger_main.debug("Snake is out of bounds")
        game_is_on = False
        scoreboard.game_over()

    # Check if snake has "eaten" the food
    if snake.head.distance(food) < 1:
        logger_main.debug("Snake ate some food")
        food.refresh()
        snake.extend()
        scoreboard.bump()

    # check if snake is hitting itself
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 1:
            logger_main.debug("Snake ran into itself")
            game_is_on = False
            scoreboard.game_over()

    snake.move()

logger_main.info("Exited main game loop")

# Leave screen up until user clicks
screen.exitonclick()
