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
        return Hostip.get('ip')


targetIP = readIP()
TCP_PORT = 5001
sockt = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # TCP
sockt.bind(('', TCP_PORT))
    
def receiveM():
    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        print ("received message:", data)
        return data



