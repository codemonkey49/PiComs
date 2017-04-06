import socket
import os
import time
# Create a TCP/IP socket
s=socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))

s.listen(5)
def send(message, c):
    message=message.encode("utf-8")
    c.send(message)

def recieve(c):
    return str(c.recv(1024).decode("utf-8"))

def sendFile(c,fileName):
    f=open(fileName,"r")

    data=f.read(1024)
    while data:
        send(data,c)
        data=f.read(1024)


while True:
    c,addr=s.accept()
    if c:
        print("connected to: "+str(addr))
        request=recieve(c)
        print ("request: "+request)
        send("response from server",c)
        sendFile(c,"sendData.txt")
        c.close()



