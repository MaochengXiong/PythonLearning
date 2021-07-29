from poker import getDeck
number = [2,3,4,5,6,7,8,9,10]

deck1 = getDeck(number)

def player(name):
    name = name
    card = deck1[0:17]
    del deck1[0:17]
    return {"name": name, "card":card}

# def isLord(player):
#     if(deck1 == []):
#         return False
#     for i in range(3,10,1):
#         count = 0
#         if (i not in player['card']):
#             return True
#     if(player['name']=="player3"):
#         return True
#     return False

def getLastThree(player):
    # if(isLord(player)):
    if player["name"]=="player3":
        for i in deck1:
            player["card"].append(i)
        del deck1[0:3]
    

# player1 = player("player1")
# player2 = player("player2")
# player3 = player("player3")
# getLastThree(player1)
# getLastThree(player2)
# getLastThree(player3)

# print(player1)
# print(player2)
# print(player3)
# print(deck1)

