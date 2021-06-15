# initialize
from socket import * #import socket
import sys

serverName = sys.argv[1]
serverPort = int(sys.argv[2])
file_name = sys.argv[3]


# Create socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# Connect to server
clientSocket.connect((serverName, serverPort))

# Read user message

message = 'GET /' + file_name
clientSocket.send(message.encode()) # send URL
header = clientSocket.recv(1024).decode()
messageRecv = clientSocket.recv(1024).decode()
finalMessage = ''
while messageRecv:
    finalMessage += messageRecv
    messageRecv = clientSocket.recv(1024).decode()

print(header+finalMessage)
clientSocket.close()    
    