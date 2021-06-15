# -*- coding: utf-8 -*-
# Initialize

from socket import * #import socket

serverPort = 12000 #server is listening port:12000

# Create socket

serverSocket = socket(AF_INET, SOCK_STREAM) #(address family, socket type) 
# AF_INET # underlying networkd is using IPv4
# SOCK_STREAM # TCP socket

# Bind with a port and listen

serverSocket.bind(('', serverPort)) # 1200 포트의 request만 listen 하겠다는 뜻

serverSocket.listen(1)
print("The server is ready to receive.") # listen queue에 하나 이상 request 존재하면 받을 준비가 됐다고 출력

# Start loop to wait for a client connection and its message*

try:
    while True:
        connectionSocket, clinetAdress = serverSocket.accept()
        message = connectionSocket.recv(2048)
        #return number of character
        message = message.decode()
        numMessage = len(message)
        message = message[::-1]
        modifiedMessage = 'The number of characters:'+str(numMessage)+'\nThe reversed string(s):'+'"'+message+'"'
        connectionSocket.send(modifiedMessage.encode()) #string -> byte
        connectionSocket.close()

except KeyboardInterrupt:
    print("Press Ctrl-C to terminate while statement")
    pass
