import socket
import time
import threading
# from threading import join
import json
from poker import *
from player import *

s = socket.socket()
host = socket.gethostname()
port = 2432
s.bind((host,port))
s.listen(5)
record = []

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
    
         
        # thread_array={}
        # t=Thread(target=sendMes(self.threadID,self.socket))
        # t.start()
        # t.join()
        # sleep(1)        


# thread_array={}
# t=Thread(target=sendMes)
# t.start()


def sendMsg(threadID, socket):
    a = False
    isReceive = False
    while a==False:
        stringYourTurn = "your turn"
        socket.send(bytes((json.dumps(stringYourTurn)).encode()))
        data = socket.recv(1024)
        if data == b'pass' or data ==b'':
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
            return
        data = json.loads(data)

        # print(data.decode(),"from", threadID)
        a = play(threadID,socket,data)
        # if a == False:
        #     word = "please re-try"
        #     socket.send(bytes(json.dumps(word).encode()))
        # print('threadId=' + str(threadID))
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
    # print (data)             
    data = data.split(",")
    print(data)
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
    
    if check == True:      
        res = isLegal(card)
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
            return True
    else:
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


while (len(card1)!=0 or len(card2)!=0 or len(card3)!=0):
            sendMsg(thread1.threadID,c)            
            sendMsg(thread2.threadID,c2)
            sendMsg(thread3.threadID,c3)  


# socket.close()

# s.listen(20)
# while True:
#     c,addr = s.accept()
#     # data = c.recv
#     print ("连接地址：", addr)
#     string = ("欢迎访问！")
#     st = string.encode()
#     c.send(st)



















    # record = []

    # while True:
    #     data = c.recv(1024)
        # data = data.split(",".encode('utf-8'))
        # card = []


        # for i in range(len(data)):
        #     string = str(data[i],'utf-8')
        #     # print(string)
        #     count = 0
        #     if (string!="A" and string!="J" and string!="Q" and string!="K" and string!="joker" and string!="Joker"):
        #         for j in range(len(record)):
        #             if (record[j]==int(string)):
        #                 count = count+1

        #         record.append(int(string))
        #         card.append(int(string))
        #     else:
        #         for j in range(len(record)):
        #             if (record[j]==string):
        #                 count = count+1

        #         record.append(string)
        #         card.append(string)
            
        #     if (count>=4):
        #         c.send("it is illegal".encode('utf-8'))
        
        # # print (card)
        
        # res = isLegal(card)
        # print('receive:',data)
        # if data == b'exit':
        #     break
        # # c.send()
        # # print(res)
        # c.send(res.encode('utf-8'))

#         # reply = input("reply:").strip()
#         # if not reply:
#         #     break
#         # msg = time.strftime('%Y-%m-%d %x')
#         # msg1 = '[%s]:%s'%(msg,data)
#         # c.send(msg1.encode('utf-8'))
#     # c.close()




















# sel = selectors.DefaultSelector()
# # port = 2432

# lsock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# lsock.bind((host, port))
# lsock.listen(5)
# print("listening on",(host,port))
# lsock.setblocking(False)
# sel.register(lsock,selectors.EVENT_READ,data=None)

# def accept_wrapper(sock):
#     conn, addr = sock.accept()
#     print('accepted connection from', addr)
#     conn.setblocking(False)
#     data = types.SimpleNamespace(addr=addr, inb=b'', outb=b'')
#     events = selectors.EVENT_READ | selectors.EVENT_WRITE
#     sel.register(conn,events,data = data)

# def service_connection(key, mask):
#     sock = key.fileobj
#     data = key.data
#     if mask & selectors.EVENT_READ:
#         recv_data = sock.recv(1024)
#         if recv_data:
#             data.outb += recv_data
#         else:
#             print('closing connection to', data.addr)
#             sel.unregister(sock)
#             sock.close()
#     if mask & selectors.EVENT_WRITE:
#         if data.outb:
#             print('echoing', repr(data.outb),'to',data.addr)
#             sent = sock.send(data.outb)
#             data.outb = data.outb[sent:]


# while True:
#     events = sel.select(timeout=None)
#     for key, mask in events:
#         if key.data is None:
#             accept_wrapper(key.fileobj)
#         else:
#             service_connection(key,mask)

