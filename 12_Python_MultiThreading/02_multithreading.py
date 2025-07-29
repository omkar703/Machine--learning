
# ThreadPool execution

import time
from concurrent.futures import ThreadPoolExecutor

def prime_numbers(n):
    time.sleep(1)  # simulate I/O operation
    return f"number is : {n}"

number = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53]

# create a ThreadPoolExecutor object with 3 worker threads
with ThreadPoolExecutor(max_workers = 3) as executor:
    results  = executor.map(prime_numbers, number)

for result in results:
    print(result)
    


# use all 3 thread that make code faster
