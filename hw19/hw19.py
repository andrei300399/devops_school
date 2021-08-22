# Написать dns сервер.
# Сервер должен принимать соединения по протоколу udp.
# Если приходит запрос "domain.name" должен отправлять в ответ ip адрес.
# * Доп задание: иметь возможность переопределять записи клиентами:
# * ADD my.google.com:228.228.228.228
# С Доп.Заданием
# отчет о работе на скнине result.png
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 9999))
users_defined = {}
while True:
    data, sender = server_socket.recvfrom(512)
    data_list = data.decode().split()
    # если команда переопределить
    if len(data_list) > 1 and data_list[0] == "ADD":
        users_defined[data_list[1].split(":")[0]] = data_list[1].split(":")[1]
        server_socket.sendto(b"Data updated", sender)
    # если есть в определенном пользователе словаре
    elif data_list[0] in users_defined:
        server_socket.sendto(users_defined[data_list[0]].encode(), sender)
    # утилита gethostbyname переведет, если домена нет в предопределенном словаре
    else:
        try:
            server_socket.sendto(socket.gethostbyname(data_list[0]).encode(), sender)
        except:
            server_socket.sendto(b"No such domain", sender)
