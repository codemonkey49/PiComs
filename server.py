import socket
import os

s=socket.socket()
host=socket.gethostname()
port=12345
s.bind((host,port))

s.listen(5)

print "server listening"
while True:
        c,addr=s.accept()
        print "connection from "+ str(addr)
        data=c.recv(1024)
        #print('Server received', repr(data))

        filename='sendData.txt'
        size=os.path.getsize("sendData.txt")
        f = open(filename,'rb')
        l = f.read(1024)
        processed=0
        while (l):

            c.send(l)
            #print('Sent ',repr(l))
            l = f.read(1024)
            processed+=1024
            print ("progress: "+str(int(100*(float(processed/float(size))))))+"%"


        f.close()
        print('Done sending')
        #c.send('Thank you for connecting')
        c.close()
