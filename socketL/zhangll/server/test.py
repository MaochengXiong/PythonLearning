# from server import data as Data
#
# text = Data.pack_text(['1', '2', 'J'])
# print(text)
from game.game import Game
game = Game(3)
# print(game.deck)

deck = game.deck
c1 = deck[:17]
deck = deck[17:]

c2 = deck[:17]
deck = deck[17:]

c3 = deck[:17]
deck = deck[17:]

print(c1)
print(c2)
print(c3)
print(deck)
