import asyncio
import socket

HOST = "127.0.0.1"
PORT = 25000


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"서버가 {HOST}:{PORT}에서 시작되었습니다.")


async def connect(conn: socket, addr: str):
    with conn:
        # 클라이언트로부터 데이터 수신
        # conn.recv(bufsize) -> byte 객체라 .decode()로 디코딩해줌.
        print(f"{addr}에서 연결됨.")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            await conn.sendall(data)
            print(data.decode())
    print(f"{addr}와의 연결이 끊어졌습니다.")


# client 몇 개까지 받을 수 있을까?
# 1) 프로세스가 소켓을 몇개까지 열 수 있을까? 최대로 설정하면?
# 2) 몇개의 소켓까지 성능에 이상없이 처리가능할까?
async def main():
    while True:
        conn, addr = server_socket.accept()
        asyncio.create_task(connect(conn, addr))


if __name__ == "__main__":
    asyncio.run(main())
