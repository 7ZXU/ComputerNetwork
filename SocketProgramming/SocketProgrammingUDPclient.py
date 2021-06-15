# 1.1 initialize
from socket import * #import socket

serverName = "127.0.0.1"
serverPort = 12000

# 1.2 Create socket

clinetSocket = socket(AF_INET, SOCK_DGRAM)

# 1.3 Read user message
message = input("Input losercase sentence:")

# 1.4 send message to server
clinetSocket.sendto(message.encode(), (serverName,serverPort))

# 1.5 Receive modified message from server
modifiedMessage, serverAddress = clinetSocket.recvfrom(2048)

# 1.6 Print the modified message and finish
print(modifiedMessage.decode())
clinetSocket.close()