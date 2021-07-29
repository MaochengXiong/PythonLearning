import threading
import data as Data


class Connection(threading.Thread):

    def __init__(self, threadId, socket, listener):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.socket = socket
        self.listener = listener

        self.reader = Reader('reader' + str(threadId), socket, listener)
        self.reader.start()

        self.listener.registerPlayer(self)

    def run(self):
        while True:
            pass

    def send(self, json):
        self.socket.send(Data.json2Bytes(json))


class Reader(threading.Thread):

    def __init__(self, threadId, socket, listener):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.socket = socket
        self.listener = listener

    def run(self):
        while True:
            receivedBytes = self.socket.recv(1024)
            receivedJson = Data.unpack(receivedBytes)
            self.listener.onReceiveData(self.threadId, receivedJson)
