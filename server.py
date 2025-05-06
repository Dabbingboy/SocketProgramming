import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())#Automatically gets IP for server
ADDR = (SERVER,PORT)#address format 
FORMAT = 'utf-8'
#utf-8 is used to encode because it formats the string into its ascii value,
#further converted in binary form.
DISCONNECT_MESSAGE = "!DISCONNECT"
TALK_MESSAGE="!TALK"


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#socket construction
server.bind(ADDR)
def handle_client(conn, addr):
    print(f"\nNEW CONNECTION {addr} connected.")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == TALK_MESSAGE:
                T_bool=True
                t=threading.Thread(target=talk, args=(conn,addr,T_bool))
                t.start()
                t.join()
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"{addr} {msg.rstrip()}")
            conn.send("MESSAGE RECEIVED".encode(FORMAT))
    conn.close()
    print(f"DISCONNECTING {addr[0]}....")
def talk(conn,addr,T_bool):
    while T_bool:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg.lower=="talk over":
                T_bool=False
                conn.send("T4LK_0V3R")
        print(conn[0],' port ',conn[1],':',msg.rstrip())
        conn.send(input("ENTER: ").encode())
def start():
    server.listen()
    print(f"LISTENING, the server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()
        print(f"\nACTIVE CONNECTION ,{threading.active_count()-2}")
        
#each time handle_client as a thread is started it is because a new client has connected
#Threading is used to branch out the flow of the code from the main code to just a function,
#optimal in handling multiple clients for a single server 
print("STARTING, the server is starting...")
start() 
