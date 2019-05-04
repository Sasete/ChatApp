from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter
import select, socket
from subprocess import Popen
import json
import time

#Keeping data that will broadcasted
data = {}



# Gets ip of our computer
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


# This function writes data into Json file
def writeToJson(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)
        

# Sets Username and IP data's into data and save it into Json later
def setUsernameIP(Event = None):
    path = './'
    fileName = 'BroadcastFile'


    data['username'] = username_box.get()
    data['ip'] = get_ip()
    writeToJson(path,fileName,data)
    

def refresh():
    null
    # TODO


def merge():
    null
    # TODO

    
def broadcast():
    Popen('python ServiceAnouncer.py')


# FRONT END STARTS HERE
    

main = tkinter.Tk()
main.title("Server")

user_frame = tkinter.Frame(main)

scrollbar = tkinter.Scrollbar(user_frame)

userlist = tkinter.Listbox(user_frame, height=20, width=40, yscrollcommand=scrollbar.set)


scrollbar.pack(side =tkinter.RIGHT, fill=tkinter.Y)
userlist.pack(side=tkinter.LEFT,fill=tkinter.BOTH)
userlist.pack()
user_frame.pack()

port_var = tkinter.IntVar()
port_var.set(5000)

username_var = tkinter.StringVar()
username_var.set("")


port_box = tkinter.Entry(main, textvariable = port_var, width = 5)
username_box = tkinter.Entry(main, textvariable = username_var, justify = tkinter.CENTER)
username_box.bind("<Return>", setUsernameIP)


setUser_button = tkinter.Button(main, text = "Set Username", command = setUsernameIP)

broadcast_button = tkinter.Button(main, text = "Broadcast", command = broadcast)

refresh_button = tkinter.Button(main, text = "Refresh", command = refresh)

merge_button = tkinter.Button(main, text = "Merge", command = merge)


broadcast_button.pack(side = tkinter.BOTTOM, fill=tkinter.X)
port_box.pack(side = tkinter.BOTTOM, fill=tkinter.Y)
setUser_button.pack(side = tkinter.BOTTOM, fill = tkinter.X)
username_box.pack(side = tkinter.BOTTOM, fill = tkinter.X)
refresh_button.pack(side = tkinter.BOTTOM,fill=tkinter.X)
merge_button.pack(side = tkinter.BOTTOM,fill=tkinter.X)

merge_button.pack()
refresh_button.pack()
username_box.pack()
setUser_button.pack()
port_box.pack()
broadcast_button.pack()

main.resizable(False,False)

Popen('python ServiceListener.py')
tkinter.mainloop()

