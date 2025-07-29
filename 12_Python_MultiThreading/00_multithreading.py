# multithreading
# when to use
# 1. IO bound tasks - read/write files, network requests, database queries
# 2. CPU bound tasks - mathematical calculations, complex algorithms (imprive by nature)

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)  # I/O application is used
        print(f"Number : {i}")

def print_letters():
    for i in range(3):
        time.sleep(2)
        print(f"Letter : {chr(i + 65)}")




t = time.time()  # Corrected: Use time.time() instead of time.now()
print_letters()
print_numbers()
finished_time = time.time() - t  # Corrected: Use time.time() again

print(f"Time taken : {finished_time:.4f} seconds")  # Formatted output

# here when 1 task is running, other task is waiting due to single thread execution
