#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM) # create server socket
#Prepare a server socket
## start
serverPort = 80 # server is listening port:1234
serverSocket.bind(('127.0.0.1', serverPort)) # listening only port number 1234
serverSocket.listen(1) # listen # 한번에 하나의 소켓 연결
print('listening...')
## finsish
while True:
    #Establish the connection
    print('Ready to serve...')
    ## start 
    connectionSocket, addr = serverSocket.accept()  
    ## finish
    # serverSocket : client 연결 요청 수신
    # connectionSocket : client socket과 실질적으로 연결돼서 데이터 송수신하는 소켓, accept() API를 통해 만들어짐
    try:
        ## start
        message = connectionSocket.recv(1500) # recv() # input에 버퍼사이즈 2048 할당
        ## finish        
        filename = message.split()[1] # path is second part of http header
        f = open(filename[1:]) #추출한 path에는 '\' 로 시작하기에 두번째 문자부터 읽어줘야한다
        ## start 
        outputdata = f.read() # 파일을 읽고 전체 내용을 filedata에 저장한다
        ## finish
        f.close()
        #Send one HTTP header line into socket
        ## start
        header = '\nHTTP/1.1 200 OK\n\n'
        connectionSocket.send(header.encode())
        ## finish
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode()) # connection socket에 요청 파일 내용 보냄
        connectionSocket.close()
        print("OK!")
    except IOError:
        #Send response message for file not found
        ## start
        print("error\n")
        errorMessage = '\nHTTP/1.1 404 Not Found\r\n\r\n'
        connectionSocket.send(errorMessage.encode())
        print("error\n")
        #errorMessage = '<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n'
        #connectionSocket.send(errorMessage.encode())
        #connectionSocket.send(b'\r\n\r\n')
        ## finish
        #Close client socket
        ## start
        connectionSocket.close()  
        ## finish
serverSocket.close()
