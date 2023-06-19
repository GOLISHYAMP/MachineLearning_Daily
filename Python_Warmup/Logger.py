from loguru import logger

# Configure the logging
logger.add(lambda msg: print(msg, end=''), level="DEBUG", format="{level} {message}")

# Log some messages
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

# Log messages with variable values
name = 'John'
age = 30
logger.info(f'User {name} is {age} years old')

# Log an exception stack trace
try:
    result = 10 / 0
except Exception as e:
    logger.error(f'An error occurred: {str(e)}')

# Log messages with different levels
for i in range(5):
    if i < 3:
        logger.debug(f'Iteration {i}')
    elif i == 3:
        logger.info(f'Iteration {i}')
    else:
        logger.warning(f'Iteration {i}')

# Log messages from different modules
logger.level("INFO")

logger.info('This is a custom log message')
logger.warning('This is a custom warning message')

# Log messages with custom formatting
# logger.add(lambda msg: print(msg, end=''), format="{level} {message}")

logger.level("DEBUG")

logger.debug('This is a custom debug message')
logger.info('This is a custom info message')
logger.error('This is a custom error message')
