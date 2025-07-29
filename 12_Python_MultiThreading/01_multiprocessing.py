## Multiprocessing
# --> It allow to run processes simultaneously
# CPU bound tasks can be parallelized using multiprocessing
# Parallel execution allows for faster execution of multiple tasks at the same time (use all cores)

import multiprocessing
import time
def square_number():
    for i in range(10):
        time.sleep(1)
        print(f'Square of {i} is {i**2} \n')

def cube_number():
    for i in range(10):
        time.sleep(1.5)
        print(f'Cube of {i} is {i**3} \n')

# Main program starts here. If this script is run directly, it starts the main program.
if __name__ == '__main__':
## Create processes
    square_process = multiprocessing.Process(target=square_number)
    cube_process = multiprocessing.Process(target=cube_number)

    t = time.time()
    ## Start processes

    square_process.start()
    cube_process.start()

    # wait for process completion

    square_process.join()
    cube_process.join()

    finished_time = time.time() - t
    print('Both processes have completed their execution.',finished_time)

