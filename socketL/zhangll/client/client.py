import socket
import json
import status
from reader import Reader

standardCards = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2', 'joker', 'Joker']

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
        text = text.strip(' ')
        if ',' in text:
            text = text.strip(' ')
            cards = text.split(',')
            if cards.count('') > 0:
                error('invalid input')
            else:
                s.send(bytes(json.dumps({'code': 3, 'content': cards}).encode()))
                status.status = False
        elif text in standardCards:
            s.send(bytes(json.dumps({'code': 3, 'content': [text]}).encode()))
        elif 'pass' == text:
            s.send(bytes(json.dumps({'code': 3, 'content': []}).encode()))
        else:
            error('invalid input')

