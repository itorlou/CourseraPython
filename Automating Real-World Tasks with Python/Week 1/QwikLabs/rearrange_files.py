#!/usr/bin/env python3
from os import listdir
from PIL import Image

#declaramos variables de pathing
src_dir = "images/"
new_dir = "/opt/icons/"

#seteamos valores finales
rx_90dg = -90
rx_size = (128, 128)

rx_frmt = "JPEG"

#hacemos una lista con las imagenes
img_files = [f for f in listdir(src_dir) if f.startswith("ic_")]

#recorremos las imagenes
for file in img_files:
    src_img = Image.open(src_dir + file) #modificamos variable a imagen_n

    new_img = src_img.rotate(rx_90dg).resize(rx_size) #rotamos y modificamos tamaño

    new_img = new_img.convert("RGB") #modificamos formato

    new_img.save(new_dir + file, rx_frmt) #guardamos