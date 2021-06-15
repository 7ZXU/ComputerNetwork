import socket                   

s = socket.socket() # 소켓 생성
host = '127.0.0.1'              
port = 80                       

s.connect((host, port)) 

with open('Received_data.txt', 'wb') as f:  # write 파일 생성 
    while True:
        print('receiving data...')
        messageRecv = s.recv(1024)
        if not messageRecv:
            break
        
        while messageRecv:
            f.write(messageRecv)    # request 데이터 파일에 기록
            messageRecv = s.recv(1024)
        
        print("Writing success!")
f.close()
s.close()
print('connection closed')