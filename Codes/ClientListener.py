from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter
import select, socket
from subprocess import Popen
import json
import time
import ipaddress



def readUsername():# return the host name from json file
    with open('ChatData.json') as fp:
        Hostname = json.load(fp)
        return Hostname.get('username')

def readIP():# return the host ip from json file
    with open('ChatData.json') as fp:
        Hostip = json.load(fp)
        
        #return Hostip.get('ip')

        return '127.0.0.1'


def receiveM():
    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        print ("received message:", data)
        return data





targetIP = readIP()
PORT = 5000
BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1',PORT))
sock.listen(4)

conn, addr = sock.accept()

print ('Connection address:', addr)
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print ("received data:", data)
    conn.send(data)
conn.close
