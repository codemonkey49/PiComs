import socket
import sys


class cInstance():
    def __init__(self):
        self.sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = ("192.168.0.2", 10000)
        self.sock.connect(self.server_address)


    def sendMessage(self,message):
        sock=self.sock
        sock.send(message)

    def recieveFile(self,fileName):
        sock=self.sock
        with open(fileName,"wb") as f:
            while True:
                data=sock.recv(1024)
                if not data:
                    break
                f.write(data)
            f.close()
            print ("successfull file transfer")
    def close(self):
        self.sock.close()


c=cInstance()
c.sendMessage("this is a test of the emergency broadcast system")
c.recieveFile("test.txt")
c.close()
