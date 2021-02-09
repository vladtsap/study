import json

from flask import Flask, Response, request
from redis import Redis

app = Flask(__name__)
r = Redis(host='redis')


@app.route('/')
def index():
    return f'''
    <p>Speed: {int(speed) if (speed := r.get("speed")) else 0}</p>
    <p>Distance: {int(distance) if (distance := r.get("distance")) else 0}</p>
    <p>Temperature: {int(temp) if (temp := r.get("temp")) else 0}</p>
    '''


@app.route('/data', methods=['POST'])
def data():
    content = json.loads(request.data.decode('utf-8'))

    r.mset({
        "speed": content['speed'],
        "distance": content['distance'],
        "temp": content['temp'],
    })

    return Response(status=200)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
