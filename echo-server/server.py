import socket

HOST = "127.0.0.1"
PORT = 25000


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"서버가 {HOST}:{PORT}에서 시작되었습니다.")

while True:
    conn, addr = server_socket.accept()
    # conn: client와 연결된 socket
    # addr: (client ip, client port)

    with conn:
        # 클라이언트로부터 데이터 수신
        # conn.recv(bufsize) -> byte 객체라 .decode()로 디코딩해줌.
        print(f"{addr}에서 연결됨.")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            # 수신한 데이터를 클라이언트에게 다시 전송
            conn.sendall(data)
            print(data.decode())
