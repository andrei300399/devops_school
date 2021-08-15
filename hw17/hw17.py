# Написать скрипт, который будет вытаскивать gps данные
# из фотографии (jpg файл) и передавать их на вход программе
# из hw16.txt
from GPSPhoto import gpsphoto
import os

data = gpsphoto.getGPSData('image2.jpg')
print(f"Coordinates: {data['Latitude']}, {data['Longitude']}")


path_to_file = os.path.join("../hw16", "hw16.py")
os.system(f"python {path_to_file} {data['Latitude']},{data['Longitude']}")



