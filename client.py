import socket
import os

request=raw_input("what movie do you want to watch?")
s = socket.socket()
host = "192.168.0.2"#socket.gethostname()
port = 10000
s.connect((host,port))

def send(s,message):
    message=message.encode("utf-8")
    s.send(message)

def recieve(s):
    return str(s.recv(1024).decode("utf-8"))

def recieveFile(s,fileName):
    f=open(fileName,"wb+")
    fileSize=int(s.recv(1024))
    print fileSize
    data=s.recv(1024)
    recieved=0
    lastDone=0
    while data:
        f.write(data)
        data=s.recv(1024)
        recieved+=1024

        done=int(90* (float(recieved)/float(fileSize)))
        if (done>100):
            done=100
        if done>lastDone:
            print "%"+str(done)
            lastDone=done

    print "done recieving: "+fileName
    print "total recieved: "+str(recieved)
   # print "filesize: "+str(os.path.getsize("/home/pi/PiComs/"+fileName))


send(s,request)
recieveFile(s,request+".mp4")
