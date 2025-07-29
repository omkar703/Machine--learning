# Multiprocessing For CPU Bound Tasks

'''
Scenario: Factorial Calculation
For large numbers, calculating factorial can be CPU-bound task.
'''
import multiprocessing
import time
import math
import sys

# Increse the maximum number of degits for integer conversion

sys.set_int_max_str_digits(1000000)

# funtion to compute factorials of a given number
def compute_factorial(n):
    print(f'Computing factorial of {n}')
    result = math.factorial(n)
    return result 

if __name__ == '__main__':
    numbers = [50000,6000,22222,111,24242]
    start_time = time.time()
    
    # using for loop instide we use pool 
    # Create a pool of worker processes
    pool = multiprocessing.Pool()
    
    # Use pool.map to apply the compute_factorial function to each number in the list
    results = pool.map(compute_factorial, numbers)
    
    # Close the pool and wait for all processes to finish
    pool.close()
    pool.join()

    
    end_time = time.time()
    
    print('Total time taken:', end_time - start_time)
    print('Results:', results)
