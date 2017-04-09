import socket
import os
import time
# Create a TCP/IP socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#host = socket.gethostname()
#port = 12345
server_address=("192.168.0.2",10000)
s.bind(server_address)

s.listen(5)
def send(message, c):
    #raspmessage=message.encode("utf-8")
    c.send(message)

def recieve(c):
    return str(c.recv(1024).decode("utf-8"))

def sendFile(c,fileName):
    f=open(fileName,"rb")#encoding="utf-8")
    size=os.path.getsize(fileName)
    data=str(size).encode(encoding="utf-8")
    print ("sentSize: "+str(size))
    while data:
        send(data,c)
        data=f.read(1024)





while True:
    c,addr=s.accept()
    if c:
        print("connected to: "+str(addr))
        request=recieve(c)
        print ("request: "+request)
        Storage="E:\movies"+'\\'
        for root, dirs, files in os.walk(Storage):
            for file in files:
                file=file.split(".")
                ext=file[1]
                file=file[0]
                #print (file)
                #print (request)
                if file==request:
                    file=(Storage+file+"."+ext)
                    #size=(os.path.getsize(file))
                    #sendSize(size)
                    #send("file Found, Sending",c)
                    print("begin file Sending")
                    sendFile(c, file)
                    #sendFile(c,"./Storage/sendData.txt")
                    print ("file finished sending")
                    break
            #send("file not found",c)




        c.close()



