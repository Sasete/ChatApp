from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter
import select, socket
from subprocess import Popen
import json
import time
import ipaddress
from ClientListener import receiveM


def readUsername():# return the host name from json file
    with open('ChatData.json') as fp:
        Hostname = json.load(fp)
        return Hostname.get('username')

def readIP():# return the host ip from json file
    with open('ChatData.json') as fp:
        Hostip = json.load(fp)
        return Hostip.get('ip')


targetIP = readIP()

def receive(msg):
    message_list.insert(tkinter.END,readUsername() + ":" + str(msg))

def send(event=None):

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    #sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    #sock.settimeout(0.2)
    
    sock.bind(('',5001))
    
    if message.get() != "":

        a = message.get()
        sock.sendto(bytes(a,"utf8"), (targetIP, int('5000')))
      
        message_list.insert(tkinter.END,"You:" + message.get())
        message.set("")



def leave(event=None):
    clientChat.quit()


clientChat = tkinter.Tk()
clientChat.title(readUsername())

message_frame = tkinter.Frame(clientChat)
message = tkinter.StringVar()
message.set(" ... ")
scrollbar = tkinter.Scrollbar(message_frame)

message_list = tkinter.Listbox(message_frame, height = 20, width = 60, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
message_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
message_list.pack()
message_frame.pack()

quit_button = tkinter.Button(clientChat, text="Quit",command=leave)
quit_button.pack(side=tkinter.BOTTOM,fill=tkinter.BOTH)
quit_button.pack()

send_button = tkinter.Button(clientChat, text="Send", command=send)
send_button.pack(side=tkinter.BOTTOM,fill=tkinter.BOTH)
send_button.pack()

entry_field = tkinter.Entry(clientChat, textvariable = message)
entry_field.bind("<Return>", send)
entry_field.pack(side=tkinter.BOTTOM,fill=tkinter.BOTH)
entry_field.pack()


clientChat.protocol("WM_DELETE_WINDOW", leave)


#BUFSIZ = 1024
#ADDR = (HOST, PORT)


#client_socket = socket(AF_INET, SOCK_STREAM)
#client_socket.connect(ADDR)

#receive_thread = Thread(target = receive)
#receive_thread.start()


print("Chat has been started with ", readUsername(),readIP())


tkinter.mainloop()

recieve(ClientListener.receiveM())
