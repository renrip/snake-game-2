import logging
import logging.config

logging.config.fileConfig('snake_logging.config')

# create loggers
logger_main = logging.getLogger('snake_main')
logger_snake = logging.getLogger('snake_snake')
logger_scoreboard = logging.getLogger('snake_scoreboard')
logger_food = logging.getLogger('snake_food')