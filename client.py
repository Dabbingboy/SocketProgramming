import socket
import sys
HEADER = 64
PORT = 5050
SERVER = "X.X.X.X" #SERVER IPv4
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
ADDR = (SERVER,PORT)#address format 


client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#Socket contruction
try:
    client.connect(ADDR)
#Error Handling if Server is not available but client is starting,
#sys used to stop the program
except:
    print("SERVER UNAVAILABLE")
    sys.exit()
def send(msg):
    message = msg.encode(FORMAT)
    msg_length =len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length = send_length + b' ' * (HEADER - len(send_length))#encoding space character i.e b' ', to fill out empty spaces in message, hello as'
    client.send(send_length)#                                      hello as b'hello                                                           '
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

print("MESSAGE:",end=' ')
ip=input("")
if ip.lower() == 'talk':
    ip == "!TALK"
send(ip)
input()#for user to press enter and exit the program
send(DISCONNECT_MESSAGE)
