import socket
import os
# Create a TCP/IP socket
class sInstance():
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        local = True
        if local:
            self.host = socket.gethostname()  # Get local machine name
            self.port = 10000  # Reserve a port for your service.
            self.server_address = (self.host, self.port)
        else:
            self.server_address = ('192.168.0.2', 10000)

    def recieveMessage(self):

        sock=self.sock
        sock.bind(self.server_address)
        sock.listen(1)
        # Find connections
        connection, client_address = sock.accept()
        try:
            data = connection.recv(999)
            if data:
                print(str(data))
                print(os.path.getsize(data))

        except:
            connection.close()


    def sendFile(self,fileName):
        sock=self.sock
        sock.listen(5)
        while True:
            c, addr = sock.accept()
            data = c.recv(1024)
            f=open(fileName,"rb")

            l=f.read(1024)
            while(l):
                c.send(l)
                l=f.read(1024)
            f.close()
            c.close()





a=sInstance()
a.recieveMessage()
a.sendFile("test.txt")




