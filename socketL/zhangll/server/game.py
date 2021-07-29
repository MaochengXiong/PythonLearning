class Game:
    def __init__(self):
        pass

    def onReceiveData(self, threadId, data):
        print(threadId + ' received data: ' + str(data))
        pass
    pass
