import threading
import json
import status


class Reader(threading.Thread):

    def __init__(self, threadId, socket):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.socket = socket

    def run(self):
        while True:
            receivedBytes = self.socket.recv(1024)
            print(str(receivedBytes))
            receivedJson = json.loads(receivedBytes)
            code = receivedJson['code']
            if code == 3 or code == 5:
                status.status = True
            print(receivedJson['data'])