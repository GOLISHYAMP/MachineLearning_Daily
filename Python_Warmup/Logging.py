
import timeit

# Configure the logging
code_snip = '''
import logging
logging.basicConfig(
    level=logging.WARNING,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)



# Log some messages
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

# Log messages with variable values
name = 'John'
age = 30
logging.info('User %s is %d years old', name, age)

# Log an exception stack trace
try:
    result = 10 / 0
except Exception as e:
    logging.error('An error occurred: %s', str(e))

# Log messages with different levels
for i in range(5):
    if i < 3:
        logging.debug('Iteration %d', i)
    elif i == 3:
        logging.info('Iteration %d', i)
    else:
        logging.warning('Iteration %d', i)

# Log messages from different modules
logger = logging.getLogger('custom')
logger.setLevel(logging.WARNING)
logger.addHandler(logging.StreamHandler())

logger.info('This is a custom log message')
logger.warning('This is a custom warning message')

# Log messages with custom formatting
formatter = logging.Formatter('%(levelname)s - %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(formatter)

logger = logging.getLogger('custom2')
logger.setLevel(logging.WARNING)
logger.addHandler(handler)

logger.debug('This is a custom debug message')
logger.info('This is a custom info message')
logger.error('This is a custom error message')
'''

execution_time = timeit.timeit(code_snip,number=1)

print(f"The time took for execution using default logging is : {round(execution_time,5)}")