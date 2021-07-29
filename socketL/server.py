import socket
import threading
import json
from poker import *
from player import *

s = socket.socket()
host = socket.gethostname()
port = 2432
s.bind((host,port))
s.listen(5)
record = []
previous = []
passCount = 0

player1 = player("player1")
player2 = player("player2")
player3 = player("player3")
getLastThree(player1)
getLastThree(player2)
getLastThree(player3)
# print(player1,player2,player3)
card1 = player1["card"]
card2 = player2["card"]
card3 = player3["card"]


def sortCard(card):
    card = changeNumToCard(sorted(changeCardToNum(card)))
    return card

card1 = sortCard(card1)
card2 = sortCard(card2)
card3 = sortCard(card3)
cardSend1 = json.dumps(card1)
cardSend2 = json.dumps(card2)
cardSend3 = json.dumps(card3)

# def wannaLord(player,socket):
    
#     socket.send("Do you want to be the lord?".encode())
#     data = socket.recv(1024)
#     if (data == b'yes' or data ==b'Yes'):
#         if(len(deck1)==0):
#             print("you don't have this chance")
#             return
#         else:
#             getLastThree(player)
    

class MyThread(threading.Thread):
    def __init__(self, threadID, socket):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.socket = socket
    def run(self):
        print("start",self.threadID)
        if(self.threadID==1):
            self.socket.send(bytes(cardSend1.encode()))
            # wannaLord(player1, self.socket)
            # card = player1["card"]
            # self.socket.send(bytes(json.dumps(sortCard(card)).encode()))
        elif(self.threadID==2):
            self.socket.send(bytes(cardSend2.encode()))
            # wannaLord(player2, self.socket)
            # card = player2["card"]
            # self.socket.send(bytes(json.dumps(sortCard(card)).encode()))
        else:
            self.socket.send(bytes(cardSend3.encode()))
            # wannaLord(player3, self.socket)
            # card = player3["card"]
            # self.socket.send(bytes(json.dumps(sortCard(card)).encode()))
        string = "the lord is player3 and you are player"+ str(self.threadID)
        self.socket.send(bytes(json.dumps(string).encode()))
    


def sendMsg(threadID, socket):
    global passCount
    a = False
    isReceive = False
    while a==False:
        stringYourTurn = "your turn"
        socket.send(bytes((json.dumps(stringYourTurn)).encode()))
        data = socket.recv(1024)
        # print(data)
        if data == b'"pass"' or data ==b'""':
            passCount=passCount+1
            if(threadID==1):
                cardSend1 = json.dumps(card1)
            # print(cardSend1)
                socket.send(bytes(cardSend1.encode()))
            elif(threadID==2):
                cardSend2 = json.dumps(card2)
                socket.send(bytes(cardSend2.encode()))
            elif(threadID==3):
                cardSend3 = json.dumps(card3)
                socket.send(bytes(cardSend3.encode()))
            if passCount == 3:
                passCount = 0
            return
        data = json.loads(data)

        # print(data.decode(),"from", threadID)
        a = play(threadID,socket,data)
 
        if(threadID==1):
            cardSend1 = json.dumps(card1)
            # print(cardSend1)
            socket.send(bytes(cardSend1.encode()))
        elif(threadID==2):
            cardSend2 = json.dumps(card2)
            socket.send(bytes(cardSend2.encode()))
        elif(threadID==3):
            cardSend3 = json.dumps(card3)
            socket.send(bytes(cardSend3.encode()))
   


def play(threadID,socket,data):  
    global passCount
    # print (data) 
    global previous            
    data = data.split(",")
    # print(data)
    # for i in range(len(data)):
    #     if data[i]==',':
    #         data.pop(i)     
    #         i = i-1
    # print(data)
    card = []
    
    check = True
    size = len(record)

    for i in range(len(data)):
        string = data[i]
        count = 0
        if(string == ""or string ==" "):
            continue
        if (string!="A" and string!="J" and string!="Q" and string!="K" and string!="joker" and string!="Joker"):
            for j in range(len(record)):
                if (record[j]!="A" and record[j]!="J" and record[j]!="Q" 
                    and record[j]!="K" and record[j]!="joker" and record[j]!="Joker"                       
                    and record[j]==int(string)):
                        count = count+1
            record.append(int(string))
            card.append(int(string))
        else:
            for j in range(len(record)):
                if (record[j]==string):
                    count = count+1
            record.append(string)
            card.append(string)
        if (count>=4):
            check = False
    print('receive:',card,"from",threadID)
    if passCount == 2:
        tempCard = []
        previous = []
        passCount = 0

    if(len(previous)!=0):
        if(not isSame(previous, card)):
            check = False

        com1 = comparison(card)
        com2 = comparison(previous)
        if(com1<=com2):
            
            check = False


    tempCard = previous.copy()
    previous = card.copy()
    
    if check == True:      
        res = isLegal(card)
        # changeNumToCard(card)
        if (res == None or res =="it is illegal"):
            del record [size:]
            return False
        else:
            print(res)
            # socket.send(res.encode('utf-8'))
            for i in range(len(card)):
                if(threadID==1):
                    if(card[i] not in card1):
                        print(card[i])
                        return False
                    card1.remove(card[i])
                    print ("after: ",card1)
                if(threadID==2):
                    if(card[i] not in card2):
                        return False
                    card2.remove(card[i])
                if(threadID==3):
                    if(card[i] not in card3):
                        return False
                    card3.remove(card[i])
            showPlayingCards = "player"+str(threadID)+" played "+", ".join(data)
            c.send(bytes(json.dumps(showPlayingCards).encode()))
            c2.send(bytes(json.dumps(showPlayingCards).encode()))
            c3.send(bytes(json.dumps(showPlayingCards).encode()))
            passCount = 0
            return True
    else:
        previous = tempCard.copy()
        # socket.send("it is illegal，\n请重新出牌".encode('utf-8'))
        print("it is illegal")
        del record [size:]
        return False                    

         

c,addr = s.accept()
print ("连接地址：", addr)
thread1 = MyThread(1,c)
thread1.start()

c2,addr = s.accept()
print ("连接地址：", addr)
thread2 = MyThread(2,c2)
thread2.start()

c3,addr = s.accept()
print ("连接地址：", addr)
thread3 = MyThread(3,c3)
thread3.start()


while (len(card1)!=0 and len(card2)!=0 and len(card3)!=0):
            sendMsg(thread1.threadID,c)            
            sendMsg(thread2.threadID,c2)
            sendMsg(thread3.threadID,c3)  

print("end")
