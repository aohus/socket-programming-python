import socket

HOST = "127.0.0.1"
PORT = 25000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# TCP_NODELAY 옵션: 네이글 알고리즘 끄는 옵션. send data가 들어오면 바로바로 송신함.
client_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
client_socket.connect((HOST, PORT))
client_socket.setblocking(False)
print("Connected")

while True:
    send_data = input("입력: ")
    for data in send_data:
        client_socket.send(data.encode("utf-8"))
    # while True:
    # 시스템 호출이 인터럽트 되고 시그널 처리기가 예외를 발생시키지 않으면,
    # 메서드는 이제 InterruptedError 예외를 발생시키는 대신 시스템 호출을 재시도합니다.
    for _ in range(3):
        try:
            data = client_socket.recv(1024)
            print("received", repr(data))
        # .setblocking(False)로 설정하면 소켓에 들어온 데이터 없을 때 BlockingIOError 발생함
        # 서버에서 데이터 보내는 시간이 길어서 echo data가 다 오기전에 BlockingIOError 일어날 수 있음.
        except BlockingIOError:
            print(1)
            continue
