from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter

def receive():
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            msg_list.insert(tkinter.END, msg)
        except OSError:  # Possibly client has left the chat.
            break

    

def send(event=None):
    if message.get() != "":
        message_list.insert(tkinter.END,"You:" + message.get())
        message.set("")
#        client_socket.send(bytes(msg, "utf8"))



def leave(event=None):
    clientChat.quit()


clientChat = tkinter.Tk()
clientChat.title("Chat")

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

tkinter.mainloop()
