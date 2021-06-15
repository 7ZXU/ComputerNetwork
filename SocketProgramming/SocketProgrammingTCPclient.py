"""#**2 Socket Programing example : TCPclient**
##**2.1 Initialize**
"""
from socket import * #import socket

serverName = "127.0.0.1"
serverPort = 12000

"""##**2.2 Create socket**"""

clinetSocket = socket(AF_INET, SOCK_STREAM)

"""##**2.3 Connect to server**"""

clinetSocket.connect((serverName, serverPort))

"""##**2.4 Read user message**"""

message = input("Input losercase sentence:")

clinetSocket.send(message.encode())

modifiedMessage = clinetSocket.recv(2048)

print(modifiedMessage.decode())

clinetSocket.close()