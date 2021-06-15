# initialize
from socket import * #import socket

serverName = "127.0.0.1"
serverPort = 12000

while True:
# Create socket
    clinetSocket = socket(AF_INET, SOCK_STREAM)

# Connect to server
    clinetSocket.connect((serverName, serverPort))

# Read user message

    message = input("Input string:")
    clinetSocket.send(message.encode())
    modifiedMessage = clinetSocket.recv(2048)
    print(modifiedMessage.decode())
    clinetSocket.close()    
    




