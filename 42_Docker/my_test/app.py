import time 
import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='localhost', port=6379, decode_responses=True)

def get_hit_count():
    try:
        count = cache.incr('hit_count')
    except redis.ConnectionError:
        count = 0
    return count

@app.route('/')
def home():
    count = get_hit_count()
    return f'Hello! You have hit this URL {count} times.'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
