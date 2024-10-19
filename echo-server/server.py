import socket

HOST = "127.0.0.1"
PORT = 25000


# SO_REUSEADDR 옵션: process A가 포트 25000번을 timewait 상태로 점유하고 있을 때, process B도 25000번 포트로 연결 가능하게 함.
# 서버는 안정성이 제일 중요함. (성능은 2번째) 그래서 재시작하는 경우를 생각해야한다.
# 소켓을 닫는 역할은 무조건 클라이언트에서 해야하는데, 서버가 먼저 소켓을 닫게되는 과정에서 timewait이 발생하는데, timewait은 수초에서 수분까지 걸린다.
# 이 때, 서버가 죽어서 다시 실행하면 timewait이 걸려있는 것 때문에 새로운 소켓을 생성할 수 없다. 이때, REUSE 옵션이 유용하다. timewait 상태의 소켓에만 적용된다고 나오네??

# SO_REUSEPORT 옵션: process A, B가 한 포트에서 실행가능. 하지만, recv()로 먼저 읽은 프로세스만 동작함.
# 처음 recv() 받은 서버로 지속적으로 메시지 전달되는가??
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
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
            # 수신한 데이터를 클라이언트에게 다시 전송
            conn.sendall(data)
            print(data.decode())
