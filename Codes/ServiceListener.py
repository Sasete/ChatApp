from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter
import select, socket
from subprocess import Popen
import json
import time
import ipaddress

#port = 5000
#UDPsocket = socket(AF_INET, SOCK_DGRAM)
#UDPsocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

#UDPsocket.bind(('',port))

#buffSize = 1024


def readBroadcastIP(JSONname):# return the host name from json file
    with open(JSONname) as fp:
        Hostname = json.load(fp)
        return Hostname.get('globalip')

    
def readHostName(JSONname):# return the host name from json file
    with open(JSONname) as fp:
        Hostname = json.load(fp)
        return Hostname.get('username')

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


def tryRecieveBRDCST():
    UDP_IP = get_ip()
    UDP_PORT = 5000
    
    sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    sock.bind((UDP_IP, UDP_PORT))
    
    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        print ("received message:", data)


        newdata = str(data).split('\'')
        usernameData = newdata[3]
        ipData = newdata[7]

        saveUserAdress(data,usernameData,ipData)
        
        



def saveUserAdress(data,usernameData,ipData):
    path = './Users/'
    fileName = usernameData
    newData = {}
    newData['username'] = usernameData
    newData['ip'] = ipData
    writeToJson(path, fileName,newData)
    

# This function writes data into Json file
def writeToJson(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)
     


def recvbroadcast():
     
    
    while True:
      
        # take the client address and the message
        
        (message, clientAdress) = UDPsocket.recvfrom(buffSize)
        message = message.decode("utf8")
        #Host = readHostName(message)
       ## print(message,clientAdress)

        print(message,clientAdress)
        #writeInTo(message,clientAdress) #write the adresses and username in a txt file

       
        
    


def writeInTo(data):
    #save the adress in a txt file
    info = data
    file = open('AdressList.txt','a')
    file.write(str(info))
    file.close



while True:
    tryRecieveBRDCST()
#recvbroadcast()

