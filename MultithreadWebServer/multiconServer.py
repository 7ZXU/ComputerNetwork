import socket 
from _thread import *
# 쓰레드에서 실행되는 코드 

# 접속한 클라이언트마다 새로운 쓰레드가 생성되어 통신함 
def threaded(client_socket, addr): 

    print('Connected by :', addr[0], ':', addr[1]) 

    # 클라이언트가 접속을 끊을 때 까지 반복
    while True: 

        try:

            # 데이터가 수신되면 클라이언트에 다시 전송
            data = client_socket.recv(1024)

            if not data: 
                print('Disconnected by ' + addr[0],':',addr[1])
                break

            print('Received from ' + addr[0],':',addr[1])

            filename = data.split()[1]
            f = open(filename[1:])
            outputdata = f.read()
            f.close()
            header = '\nHTTP/1.1 200 OK\n\n'
            client_socket.send(header.encode())
            for i in range(0, len(outputdata)):
                client_socket.send(outputdata[i].encode())

        except ConnectionResetError as e:

            print('Disconnected by ' + addr[0],':',addr[1])
            break
             
    client_socket.close() 


HOST = '127.0.0.1'
PORT = 80

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT)) 
server_socket.listen() 

print('server start')


# 클라이언트가 접속하면 accept 함수에서 새로운 소켓을 리턴
# 새로운 쓰레드에서 해당 소켓을 사용하여 통신
while True: 
    client_socket, addr = server_socket.accept() 
    start_new_thread(threaded, (client_socket, addr)) 

server_socket.close() 