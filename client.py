import socket
from threading import Thread
from tkinter import *

# Ask for username from the player
#username = input("Enter your username: ")

# Create a client with a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the client to the server
ip_address = '127.0.0.1'
port = 8000

sock.connect((ip_address, port))

# Create a class for the GUI
class GUI:
    def __init__(self):
        self.Window = Tk()
        self.Window.withdraw()

        self.login = Toplevel()
        self.login.title("Login")
        self.login.resizable(width=False, height=False)
        self.login.configure(width=400, height=300)

        self.label = Label(self.login, text="Please login to continue", justify=CENTER, font="Helvetica 14 bold")
        self.label.place(relheight=0.15, relx=0.2, rely=0.07)

        self.labelName = Label(self.login, text="Name: ", font="Helvetica 12")
        self.labelName.place(relheight=0.2, relx=0.1, rely=0.2)

        self.entryName = Entry(self.login, font="Helvetica 14")
        self.entryName.place(relwidth=0.4, relheight=0.12, relx=0.35, rely=0.2)
        self.entryName.focus()

        self.go = Button(self.login, text="CONTINUE", font="Helvetica 14 bold", command=lambda: self.goAhead(self.entryName.get()))
        self.go.place(relx=0.4, rely=0.55)

        self.Window.mainloop()
    
    def goAhead(self, name):
        self.login.destroy()
        self.name = name
        rcv = Thread(target=self.receive)
        rcv.start()
    
    def receive(self):
        while True:
            try:
                message = sock.recv(2048).decode('utf-8')
                if message == 'NICKNAME':
                    sock.send(self.name.encode('utf-8'))
                else:
                    pass
            except:
                print("An error occurred!")
                sock.close()
                break

# Create a GUI object
g = GUI()

#def write():
#    while True:
#        message = '{}'.format(input(''))
#        sock.send(message.encode('utf-8'))

#receive_thread = Thread(target=receive)
#receive_thread.start()

#write_thread = Thread(target=write)
#write_thread.start()