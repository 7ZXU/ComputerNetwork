#1.1 initialize
from socket import * #import socket
serverPort = 12000 #server is listening port:12000

#1.2 create socket
serverSocket = socket(AF_INET, SOCK_DGRAM) #(address family, socket type) 
serverSocket.bind(('', serverPort)) # 1200 포트의 request만 listen 하겠다는 뜻
print("The server is ready to receive.") # listen queue에 하나 이상 request 존재하면 받을 준비가 됐다고 출력

#1.3 start loop to wait for a packet to arrive
try:
    while True:
        message, clientAddress = serverSocket.recvfrom(2048) # packet data -> message
        modifiedMessage = message.decode().upper() # decode # message string -> byte
        serverSocket.sendto(modifiedMessage.encode(),clientAddress) # encode # byte -> string
except KeyboardInterrupt:
    print("Press Ctrl-C to terminate while statement")
    pass
