import socket as Socket
from connection import Connection
from game.game import Game

player_size = 1

server = Socket.socket()
server.bind((Socket.gethostname(), 2222))
server.listen(5)

connections = {}

game = Game(player_size)

for i in range(player_size):
    socket, address = server.accept()
    connection = Connection(i, socket, game)
    connection.start()
    connections[i] = connection

# 此时玩家都已就位


for connection in connections.values():
    connection.join()
