import requests as req
from pyzbar.pyzbar import *
from PIL import Image


code = decode(Image.open('IMG_4380.JPG'))[0].data.decode('UTF-8')

resp = req.get("https://www.googleapis.com/books/v1/volumes?q=isbn:"+code)

livre = resp.json()

print(livre["items"][0]["volumeInfo"]["title"])


