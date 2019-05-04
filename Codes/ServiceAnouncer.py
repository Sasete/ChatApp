from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter
import select, socket
from subprocess import Popen
import json
import time

data = {}

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def writeToJson(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)


def setUsernameIP(Event = None):
    path = './'
    fileName = 'BroadcastFile'


    data['username'] = username_box.get()
    data['ip'] = get_ip()
    writeToJson(path,fileName,data)
    


def brdcst(msg, destination, prefix=""):

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.settimeout(0.2)
    
    sock.bind(("",44444))
    
    while True:
        a = b"message"
        
        sock.sendto(a, (get_ip(), int('5000')))
        
        print("Broadcast working...")
        
        time.sleep(0.2)

def broadcast():

    UDP_IP = get_ip()
    UDP_PORT = '5000'
    message = data
    ADDR = (UDP_IP, UDP_PORT)
    print("UDP target IP: ", UDP_IP)
    print("UDP target port: ", UDP_PORT)
    print("Message: ", message)
    print(data)

    brdcst(message,"utf8", (UDP_IP,UDP_PORT))



# Mainloop will broadcast
broadcast()
