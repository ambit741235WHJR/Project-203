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
    
    def layout(self, name):
        self.name = name
        self.Window.deiconify()
        self.Window.title("QUIZROOM")
        self.Window.resizable(width=False, height=False)
        self.Window.configure(width=470, height=550, bg="#17202A")

        self.labelHead = Label(self.Window, bg="#17202A", fg="#EAECEE", text=self.name, font="Helvetica 13 bold", pady=5)
        self.labelHead.place(relwidth=1)

        self.line = Label(self.Window, width=450, bg="#ABB2B9")
        self.line.place(relwidth=1, rely=0.07, relheight=0.012)

        self.textCons = Text(self.Window, width=20, height=2, bg="#17202A", fg="#EAECEE", font="Helvetica 14", padx=5, pady=5)
        self.textCons.place(relheight=0.745, relwidth=1, rely=0.08)

        self.labelBottom = Label(self.Window, bg="#ABB2B9", height=80)
        self.labelBottom.place(relwidth=1, rely=0.825)

        self.entryMsg = Entry(self.labelBottom, bg="#2C3E50", fg="#EAECEE", font="Helvetica 13")
        self.entryMsg.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.entryMsg.focus()

        self.buttonMsg = Button(self.labelBottom, text="Send", font="Helvetica 10 bold", width=20, bg="#ABB2B9", command=lambda: self.sendButton(self.entryMsg.get()))
        self.buttonMsg.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)
        
        self.scrollbar = Scrollbar(self.textCons)
        self.scrollbar.place(relheight=1, relx=0.974)
        self.scrollbar.config(command=self.textCons.yview)
        self.textCons.config(state=DISABLED)
    
    def goAhead(self, name):
        self.login.destroy()
        #self.name = name
        self.layout(name)
        rcv = Thread(target=self.receive)
        rcv.start()
    
    def sendButton(self, message):
        self.textCons.config(state=DISABLED)
        self.msg = message
        self.entryMsg.delete(0, END)
        snd = Thread(target=self.write)
        snd.start()
    
    def show_message(self, message):
        self.textCons.config(state=NORMAL)
        self.textCons.insert(END, message + '\n\n')
        self.textCons.config(state=DISABLED)
        self.textCons.see(END)
    
    def write(self):
        self.textCons.config(state=DISABLED)
        while True:
            message = '{}'.format(self.msg)
            #message = (f"{self.name}: {self.msg}")
            sock.send(message.encode('utf-8'))
            self.show_message(message)
            break

    def receive(self):
        while True:
            try:
                message = sock.recv(2048).decode('utf-8')
                if message == 'NICKNAME':
                    sock.send(self.name.encode('utf-8'))
                else:
                    self.show_message(message)
            except:
                print("An error occurred!")
                sock.close()
                break

# Create a GUI object
g = GUI()

#receive_thread = Thread(target=receive)
#receive_thread.start()

#write_thread = Thread(target=write)
#write_thread.start()