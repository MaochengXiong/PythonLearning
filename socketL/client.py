import socket
# import sys
# import selectors
# from player import *
# import time
import json


s = socket.socket()
host = socket.gethostname()
port = 2432

s.connect((host,port))
data = s.recv(1024)
print(json.loads(data))
data2 = s.recv(1024)
print(data2.decode(),"\nnow, start!")
# msg_input = input("your choice?")
# s.send(msg_input.encode())
# data3 = s.recv(1024)
# print("your cards:", data3.decode())

# # s.close()
while True: 
    receive = s.recv(1024)
    if receive ==b'':
        continue

    data = json.loads(receive)
    if data =="your turn":
        print(data)
        msg_input = input()
        s.send(bytes((json.dumps(msg_input)).encode()))
        if msg_input == 'exit':
            break
    else:
        print(data)
    # print(data.decode()) 
    # msg_input = input()
    # s.send(msg_input.encode())
    # if msg_input =="exit":
    #     break
    
    # data2 = s.recv(1024)
    # # print(data2)
    # # print(data2.decode())
    # print(json.loads(data2))









    # data = input('>>').strip()
    # if not data:
    #     break
    # s.send(data.encode('utf-8'))
    # print (s.recv(1024).decode('utf-8'))
    # time.sleep(5)
    # msg =s.recv(1024)
    # if not msg:
    #     break
    # print(msg.decode('utf-8'))
    # data = input('>>').strip()
    # s.send(data.encode('utf-8'))





















# messages = [b'Message 1 from client.', b'Message 2 from client.']

# def start_connection(host, post, num_conns):
#     server_addr = (host, port)
#     for i in range(0, num_conns):
#         connid = i+1
#         print('starting connection', connid, 'to', server_addr)
#         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         sock.setblocking(False)
#         sock.connect_ex(server_addr)
#         events = selectors.EVENT_READ | selectors.EVENT_WRITE
#         data = types.SimpleNamespace(connid=connid,msg_total=sum(len(m) for m in messages), recv_total = 0, messages=list(messages), outb=b'')
#         sel.register(sock,events,data=data)

# def service_connection(key,mask):
#     sock = key.fileobj
#     data = key.data
#     if mask & selectors.EVENT_READ:
#         recv_data = sock.recv(1024)
#         if recv_data:
#             print('received', repr(recv_Data),'from connection',data.connid)
#             data.recv_total += len(recv_data)
#         if not recv_data or data.recv_total == data.msg_total:
#             print('closing connection', data.connid)
#             sel.unregister(sock)
#             sock.close()
#     if mask & selectors.EVENT_WRITE:
#         if not data.outb and data.messages:
#             data.outb = data.messages.pop(0)
#         if data.outb:
#             print('sending',repr(data.oub),'to connection', data.connid)
#             sent = sock.send(data.outb)
#             data.outb = data.outb[sent:]

