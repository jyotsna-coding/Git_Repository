"""
Hello World Client
Connects REQ socket to tcp://localhost:5555
Sends "Hello" to Server and expects "World" back.
"""
import zmq

context = zmq.Context()
print("Connecting to Server")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

print("Sending Request")
socket.send(b"Hello")
message =socket.recv()
print("Recieved Reply %s" % message)
