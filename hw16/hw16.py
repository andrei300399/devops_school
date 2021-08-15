# Написать программу, которая будет считывать из файла gps координаты,
# и формировать текстовое описание объекта и ссылку на google maps.
# Пример:
#
# Input data: 60,01';30,19'
# Output data:
# Location: Теремок, Енотаевская улица, Удельная, округ Светлановское, Выборгский район, Санкт-Петербург, Северо-Западный федеральный округ, 194017, РФ
# Goggle Maps URL: https://www.google.com/maps/search/?api=1&query=60.016666666666666,30.322
from geopy.geocoders import Nominatim
import sys


def get_object_by_coordinates(coordinates):
    print(f"Input data: {coordinates}", end="")
    geolocator = Nominatim(user_agent="app")
    location = geolocator.reverse(coordinates)
    print("Output data:")
    print(location.address)
    print(f"https://www.google.com/maps/search/?api=1&query={coordinates}")


if len(sys.argv) == 1:
    with open('./input.txt', 'r', encoding='utf-8') as file:
        for line in file.readlines():
            get_object_by_coordinates(line)
else:
    for i in range(1, len(sys.argv)):
        get_object_by_coordinates(sys.argv[i])
