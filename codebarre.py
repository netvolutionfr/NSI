from pyzbar.pyzbar import *
from PIL import Image

print(decode(Image.open('IMG_4380.JPG'))[0].data.decode('UTF-8'))
