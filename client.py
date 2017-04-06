import socket
import os

s = socket.socket()
host = socket.gethostname()
port = 12345
s.connect((host,port))

def send(s,message):
    message=message.encode("utf-8")
    s.send(message)

def recieve(s):
    return str(s.recv(1024).decode("utf-8"))

def recieveFile(s,fileName):
    f=open(fileName,"w")
    data=recieve(s)
    while data:
        f.write(data)
        data=recieve(s)

send(s,"Message from Client")
print(recieve(s))
recieveFile(s,"received.txt")
