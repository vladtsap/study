import socket
from random import randrange
from time import sleep

while True:
    for port in (5001, 5002, 5003):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('nodered', port))
        s.send(str(randrange(100)).encode('utf-8'))
        s.close()

    sleep(5)
