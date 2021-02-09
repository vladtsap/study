import os

from flask import Flask, Response, request
from redis import Redis

app = Flask(__name__)

REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
REDIS_PORT = os.environ.get('REDIS_PORT', '6379')
r = Redis(host=REDIS_HOST, port=REDIS_PORT)


@app.route('/')
def index():
    return '''
    <h1>Hello!</h1>
    <h3>This is backend app</h3>
    '''


@app.route('/login', methods=['POST'])
def login():
    if not (content := request.json):
        return Response(status=400)

    if 'name' not in content:
        return Response(status=400)

    r.set("name", content['name'])
    r.incr("visitors")
    return Response(status=200)


@app.route('/user', methods=['GET'])
def user():
    if name := r.get("name"):
        name = name.decode("utf-8")

    if counter := r.get("visitors"):
        counter = int(counter)

    response = {
        'name': name,
        'counter': counter
    }
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
