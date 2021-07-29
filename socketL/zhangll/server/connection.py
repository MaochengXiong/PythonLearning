import threading
import data


class Connection(threading.Thread):

    def __init__(self, threadId, socket, listener):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.socket = socket
        self.listener = listener

        socket.send(data.json2Bytes(data.pack_text('欢迎来斗地主')))

        self.reader = Reader('reader'+str(threadId), socket, listener)
        self.reader.start()

    def run(self):
        while True:
            pass


class Reader(threading.Thread):

    def __init__(self, threadId, socket, listener):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.socket = socket
        self.listener = listener

    def run(self):
        while True:
            receivedBytes = self.socket.recv(1024)
            receivedJson = data.unpack(receivedBytes)
            self.listener.onReceiveData(self.threadId, receivedJson)
