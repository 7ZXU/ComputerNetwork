
import socket  

port = 80                      
s = socket.socket()           
s.bind(('127.0.0.1', port))
print("Bind success")
s.listen(5)           
print ('Waiting for connection...')


while True:
    c, addr = s.accept()     

    filename='sent_data.txt' # 보내는 파일 이름 지정
    f = open(filename,'rb')
    content = f.read(1024) # 파일 읽기
    while (content):
       c.send(content)
       print('Sent ',repr(content))
       content = f.read(1024)
    f.close()

    print('Done sending')
    # c.send('Thank you for connecting')
    c.close()