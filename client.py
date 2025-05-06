import socket
import sys
HEADER = 64
PORT = 5050
SERVER = "192.168.0.101" #SERVER IPv4
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
ADDR = (SERVER,PORT)#address format 
t_bool=False

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#Socket contruction
try:
    client.connect(ADDR)
#Error Handling if Server is not available but client is starting,
#sys used to stop the program
except:
    print("SERVER UNAVAILABLE")
    sys.exit()

def receive(client):
    message = client.recv(HEADER).decode(FORMAT)
    msg_length =len(message)
    if msg_length:
        msg_length = int(msg_length)
        msg=client.recv(msg_length).decode(FORMAT)
        print(msg)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length =len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length = send_length + b' ' * (HEADER - len(send_length))#encoding space character i.e b' ', to fill out empty spaces in message, hello as'
    client.send(send_length)#                                      hello as b'hello                                                           '
    client.send(message)

def talk():
    print(client.recv(HEADER).decode(FORMAT))
    global t_bool
    print("To exit talk mode, type 'talk over'")
    f_time=True
    while t_bool:
        msg=input("MESSAGE: ")
        if msg.lower()=="talk over":
            t_bool=False
            send(msg)
            return
        send(msg)
        receive(client)
        
ip=input("MESSAGE:")
if ip.lower() == 'talk':
    ip = "!TALK"
    send(ip)
    t_bool=True
    talk()
input()#for user to press enter and exit the program
send(DISCONNECT_MESSAGE)
