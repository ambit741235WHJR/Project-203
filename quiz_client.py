import socket
from threading import Thread

# Ask for username from the player
username = input("Enter your username: ")

# Create a client with a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the client to the server
ip_address = '127.0.0.1'
port = 8000

sock.connect((ip_address, port))

def receive():
    while True:
        try:
            message = sock.recv(2048).decode('utf-8')
            if message == 'NICKNAME':
                sock.send(username.encode('utf-8'))
            else:
                print(message)
        except:
            print("An error occurred!")
            sock.close()
            break

def write():
    while True:
        message = '{}'.format(input(''))
        sock.send(message.encode('utf-8'))

receive_thread = Thread(target=receive)
receive_thread.start()

write_thread = Thread(target=write)
write_thread.start()