from os.path import dirname, join
import os

current_dir = dirname(__file__)
fileToDelete = join(current_dir, "./a_borrar.txt")

#os.remove(fileToDelete) # así borramos un archivo

fileToRename = join(current_dir, "./nuevoNombre.txt")

# os.rename(fileToRename,join(current_dir,"nuevoNombre2.txt")) # así renombramos

print(os.path.exists(join(current_dir,"nuevoNombre2.txt"))) # comprobamos si existe


print(os.path.getsize(join(current_dir,"nuevoNombre2.txt"))) #devuelve el tamaño en bytes

print(os.path.getmtime(join(current_dir,"nuevoNombre2.txt")))

import datetime

timestamp = os.path.getmtime(join(current_dir,"nuevoNombre2.txt"))
print(datetime.datetime.fromtimestamp(timestamp)) # lo pasamos a datetime para que sea legible


print(os.path.abspath(join(current_dir,"nuevoNombre2.txt"))) #devuelve la ruta completa