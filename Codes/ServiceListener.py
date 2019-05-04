from socket import *
import json


port = 5000
UDPsocket = socket(AF_INET, SOCK_DGRAM)
UDPsocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

UDPsocket.bind(('',port))

buffSize =1024 








def readHostName(JSONname):# return the host name from json file
    with open(JSONname) as jison_file:
        Hostname = json.load(json_file)
        return Hostname.get('username')


def recvbroadcast():
     
    
    while True:
      
        # take the client address and the message
        
        message, clientAdress = UDPsocket.recvfrom(buffSize)
        message = message.decode("utf8")
        #Host = readHostName(message)
       ## print(message,clientAdress)

        print(message,clientAdress)
        #writeInTo(message,clientAdress) #write the adresses and username in a txt file

       
        
    


def writeInTo(host,adress):
    #save the adress in a txt file
    info = 'USERNAME:',host,', ipADRESS:',adress
    file = open('AdressList.txt','a')
    file.write(str(info))
    file.close
    

recvbroadcast()

