"""
Hello World Server.
Binds REP Socket to tcp://*:5555
Receives "Hello" from Client and replies with "World"
"""
import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    message = socket.recv()
    print("Received request: %s ", message)
    time.sleep(1)

    socket.send(b"World")
