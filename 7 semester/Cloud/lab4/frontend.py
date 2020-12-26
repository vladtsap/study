import os

from flask import Flask
from redis import Redis

app = Flask(__name__)

REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
REDIS_PORT = os.environ.get('REDIS_PORT', '6379')
r = Redis(host=REDIS_HOST, port=REDIS_PORT)


@app.route('/')
def index():
    name = r.get("name")
    user = name.decode("utf-8") if name else 'visitor'

    visitors_count = r.get("visitors")
    counter = int(visitors_count) if visitors_count else 0

    return f'''
    <h1>Hello, {user}!</h1>
    <h2>You are #{counter} on this site</h2>
    '''


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
