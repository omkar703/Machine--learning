## configuring logging
import logging
logging.basicConfig(
    level= logging.DEBUG,  
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-m-d %H:%M:%S',
    filename='app_test.log',  # specify log file path
    filemode='w'  # write mode (overwrite if file exists)
)