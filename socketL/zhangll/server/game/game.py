import random
import data as Data
from game.player import Player
import time
import game.poker as poker

class Game:
    def __init__(self, playerSize):
        self.previousCards = None
        self.playCards = None
        self.playerSize = playerSize
        self.__shuffle__()
        self.connections = {}
        self.players = {}

    def __shuffle__(self):
        number = ['2', '3', '4', '5', '6', '7', '8', '9', '10']
        deck = []
        for i in range(4):
            for j in range(len(number)):
                deck.append(number[j])
            deck.append("J")
            deck.append("Q")
            deck.append("K")
            deck.append("A")
        deck.append("joker")
        deck.append("Joker")
        random.shuffle(deck)
        self.deck = deck

    def __checkStartCondition__(self):
        return len(self.connections) == self.playerSize

    def __startGame__(self):
        # 发牌
        for connection in self.connections.values():
            cards = self.deck[:17]
            self.deck = self.deck[17:]
            self.players[str(connection.threadId)] = Player(cards, connection)
            connection.send(Data.pack_cards_of_self(cards))

        # 循环游戏 退出条件暂时留白
        index = 0
        while True:
            time.sleep(1)
            index = index % self.playerSize
            self.currentOne = self.players[str(index)]
            self.currentOne.connection.send(Data.pack_your_turn())
            self.__waitingPlay__()

            if self.__checkCards__():
                self.previousCards = self.playCards
                self.currentOne.connection.send(Data.pack_play_legal())

                # 通知全员出牌
                for c in self.connections.values():
                    c.send(Data.pack_play_cards(self.playCards['cards']))

                index += 1
                pass
            else:
                self.currentOne.connection.send(Data.pack_play_illegal())
                pass
            self.playCards = None

    def __waitingPlay__(self):
        while self.playCards is None:
            pass

    def __checkCards__(self):
        return self.__checkContain__() and self.__checkCompare__()

    def __checkContain__(self):
        threadId = self.playCards['threadId']
        cards = self.playCards['cards']
        if str(threadId) == str(self.currentOne.connection.threadId):
            allContain = True
            cardPool = self.players[str(threadId)].cards
            for card in cards:
                print(card)
                if card not in cardPool:
                    allContain = False
                    break

            return allContain
        return False

    def __checkCompare__(self):
        if self.previousCards is None:
            return True

        previousCards = self.previousCards['cards']
        cards = self.playCards['cards']

        previousValues = poker.getValuesOfCards(previousCards)
        values = poker.getValuesOfCards(cards)

        if poker.isSame(previousValues, values):
            return poker.getPointOfValues(previousValues) < poker.getPointOfValues(values)
        else:
            return False

    def onReceiveData(self, threadId, data):
        print(threadId + ' received data: ' + str(data))
        if data['code'] == 3:
            # threadId 取最后一位的数字
            self.playCards = {'threadId': threadId[-1], 'cards': data['content']}
        pass

    def registerPlayer(self, connection):
        self.connections[connection.threadId] = connection
        length = len(self.connections)

        statusNotifyStr = 'Wait players to start a new game: ' + str(length) + '/' + str(self.playerSize)
        for c in self.connections.values():
            c.send(Data.pack_text(statusNotifyStr))

        if self.__checkStartCondition__():
            self.__startGame__()

    pass
