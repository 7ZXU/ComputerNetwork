# Import socket module
import socket
import sys

# local host IP '127.0.0.1'


# Define the port on which you want to connect
# port = 12345

# while True:
host = '127.0.0.1'
port = 80
file_name = sys.argv[1]

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# connect to server on local computer
s.connect((host,port))

# message you send to server
message = 'GET /' + file_name

while True:  
    # message = 'GET/' + file_name
    # message sent to server
    s.send(message.encode())
    header = s.recv(1024).decode()
    messageRecv = s.recv(1024).decode()
    finalMessage = ''
    while messageRecv:
            finalMessage += messageRecv
            messageRecv = s.recv(1024).decode()        
    
    print(header+finalMessage)
    # ask the client whether he wants to continue
# close the connection
s.close()
  