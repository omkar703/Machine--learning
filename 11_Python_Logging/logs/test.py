from logger import logging
def add(a, b):
    logging.debug(f'Adding {a} and {b} is taking place.')
    return a + b

logging.debug('Starting the program.')
add(5, 3)