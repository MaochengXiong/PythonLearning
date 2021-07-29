import socket
import json

s = socket.socket()
host = socket.gethostname()
port = 2222

s.connect((host, port))
data = s.recv(1024)
print(data)

while True:
    text = input()
    s.send(bytes(json.dumps({'content': text}).encode()))
