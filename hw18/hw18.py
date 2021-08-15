# Написать скрипт, который будет создавать миниатюры фотографий.
# Объем полученого файла должен передаваться как параметр.

from PIL import Image
import sys
"""
get 1 argument as parameter - % from original size
"""
percentage = int(sys.argv[1])
img = Image.open('image2.jpg')
width, height = img.size
img = img.resize((int(width * percentage/100), int(height * percentage/100)), Image.ANTIALIAS)
img.save('output.jpg')
