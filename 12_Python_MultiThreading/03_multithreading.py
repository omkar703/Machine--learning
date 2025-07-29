'''
Real world example: Multhreaded file I/O Bound task
senario : web scraping multiple pages concurrently (fetch data wait for I/o)
web scraping is make an IO bound task because it involves making multiple HTTP requests to fetch data from websites.

'''

import threading

# use bs4 for web scraping

import requests
from bs4 import BeautifulSoup

urls = ['https://classroom.google.com/?lfhs=2','https://open.spotify.com/','https://www.google.com/']
def fetch_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f'Feteched data length {len(soup.text)} , all characters in url {url}' )

threads = []

for url in urls:
    thread = threading.Thread(target=fetch_data, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join() # wait for all threads to finish before moving forward

print("All web scraping tasks completed.")

# Output

# Feteched data length 268 , all characters in url https://www.google.com/
# Feteched data length 898 , all characters in url https://classroom.google.com/?lfhs=2
# Feteched data length 2911 , all characters in url https://open.spotify.com/
# All web scraping tasks completed.

