import socket

HOST = "127.0.0.1"
PORT = 25000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
print("Connected")


while True:
    send_data = input("입력: ")
    client_socket.send(send_data.encode("utf-8"))
    data = client_socket.recv(1024)
    print("received", repr(data))
