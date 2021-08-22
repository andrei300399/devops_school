import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    data = input("Input domain:")
    client_socket.sendto(data.encode(), ('localhost', 9999))
    server_data, sender = client_socket.recvfrom(512)
    print(server_data.decode())
