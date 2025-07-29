## multiprocessing with processpoolExecutor

from concurrent.futures import ProcessPoolExecutor
import time

# Function to simulate a CPU-intensive task

def square(n):
    time.sleep(1)  # Simulating CPU-intensive task
    return f"Square of {n} is: {n**2}"

numbers = [1, 2, 3, 4, 5]

if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square, numbers)

    for result in results:
        print(result)