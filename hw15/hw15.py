# Написать класс router.
# Должен иметь методы добавить/удалить/вывести список ip address.
# Должен иметь методы добавить/удалить/вывести список ip routes.
#
# Есть маршруты к непосредственно-подключенным сетям:
# если у устройства есть ip-address 192.168.5.14/24 на интерфейсе eth1,
# значит у него должен быть маршрут:
# к сети 192.168.5.0/24 через eth1 или через 192.168.5.14.
#
# Если мы хотим добавить маршрут к какой-нибудь удаленной сети,
# то надо проверять доступен ли gateway.
#
# Например мы можем добавить маршрут к 172.16.0.0/16 через gateway
# 192.168.5.132, только если у нас уже есть маршрут до 192.168.5.132.
#
# Если же мы попытаемся добавить маршрут до какой-либо сети через gateway,
# до которого у нас пока еще нет маршрута, то должен вылетать exception.
#
# Например:
# Добавляем ip-address 192.168.5.14/24 eth1.
# Добавляем маршрут до 172.16.0.0/16 через 192.168.5.1 - ok.
# Добавляем маршрут до 172.24.0.0/16 через 192.168.8.1 - exception.
# Добавляем маршрут до 172.24.0.0/16 через 172.16.8.1 - ok.
#
# Итого - 1 интерфейс и 3 маршрута в таблице.

import ipaddress


class Router:
    def __init__(self):
        self.ip_address = {}
        self.ip_routes = {}

    def add_address(self, address, interface):
        """
        добавляет адрес на интерфес
        address и interface - тип string
        """
        if not (address in self.ip_address.values() or interface in self.ip_address):
            self.ip_address[interface] = ipaddress.ip_interface(address)
            # добаляет маршрут к сети через новый адрес при добавлении адреса
            self.ip_routes[self.ip_address[interface].network] = self.ip_address[interface].ip

    def delete_address(self, interface):
        """
        удаляет адрес на интерфесе
        interface - тип string
        """
        if interface in self.ip_address:
            del self.ip_routes[self.ip_address[interface].network]
            del self.ip_address[interface]

    def get_addresses(self):
        for interface, address in self.ip_address.items():
            print(f"Interface {interface} - ip address {address}")

    def add_route(self, route):
        """
        добаяляет маршрут к сети через gateway
        route - кортеж, 1 аргумент сеть, к которой добавляем маршрут, 2 - gateway (ip-адресс)
        """
        new_network = ipaddress.ip_network(route[0])
        new_ip = ipaddress.ip_address(route[1])
        for network in self.ip_routes:
            # проверка что ip есть в сетях, к которым уже построен маршрут (что к ip есть маршрут)
            if new_ip in network:
                self.ip_routes[new_network] = new_ip
                return
        raise Exception(f"Not route to {new_ip}")

    def delete_route(self, network):
        """
        удаляет маршрут у сети
        network - тип string
        """
        deleted_network = ipaddress.ip_network(network)
        if deleted_network in self.ip_routes:
            del self.ip_routes[deleted_network]

    def get_routes(self):
        for network, ip in self.ip_routes.items():
            print(f"Route to {network} over {ip}")


route1 = Router()

route1.add_address("192.168.5.14/24", "eth1")
route1.add_route(("172.16.0.0/16", "192.168.5.1"))
route1.add_route(("172.24.0.0/16", "172.16.8.1"))
route1.get_addresses()
route1.get_routes()
route1.delete_route("172.24.0.0/16")
print("table after delete 172.24.0.0/16")
route1.get_routes()
route1.add_route(("172.24.0.0/16", "192.168.8.1"))
