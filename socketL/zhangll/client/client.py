import socket
import json
import status
from reader import Reader

s = socket.socket()
host = socket.gethostname()
port = 2222

s.connect((host, port))

reader = Reader(0, s)
reader.start()

while True:
    def error(str):
        print(str)

    if status.status:
        text = input()
        if ',' in text:
            text = text.strip(' ')
            cards = text.split(',')
            if cards.count('') > 0:
                error('invalid input')
            else:
                s.send(bytes(json.dumps({'code': 3, 'content': cards}).encode()))
                status.status = False
        else:
            error('invalid input')

