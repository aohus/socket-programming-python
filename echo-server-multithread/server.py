import socket
from threading import Thread

HOST = "127.0.0.1"
PORT = 25000


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"서버가 {HOST}:{PORT}에서 시작되었습니다.")


def connect(conn: socket, addr: str):
    with conn:
        print(f"{addr}에서 연결됨.")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
            print(data.decode())
    print(f"{addr}와의 연결이 끊어졌습니다.")


# client 몇 개까지 받을 수 있을까?
# 1) 프로세스가 스레드를 개까지 열 수 있을까?
# 2) 프로세스사 몇 개의 소켓을 열 수 있을까?
# 3) 몇개의 소켓까지 성능에 이상없이 처리가능할까?
while True:
    conn, addr = server_socket.accept()
    # client 연결 끊을 때, 간헐적으로 `ConnectionResetError: [Errno 54] Connection reset by peer` 발생함
    Thread(target=connect, args=(conn, addr)).start()
