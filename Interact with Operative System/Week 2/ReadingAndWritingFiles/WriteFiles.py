from os.path import dirname, join

current_dir = dirname(__file__)
file_path = join(current_dir, "./novel.txt")

with open(file_path, "w") as file: # los archivos se pueden abrir en varios modos, R (default) solo para leer, W para escribir, A para añadir
    file.write("Era una noche oscura y tormentosa")

with open(file_path, "r") as file: # los archivos se pueden abrir en varios modos, R (default) solo para leer, W para escribir, A para añadir
    print(file.read())

with open(file_path, "a") as file: # los archivos se pueden abrir en varios modos, R (default) solo para leer, W para escribir, A para añadir
    file.write("\nY sigue la peli....")

with open(file_path, "r") as file: # los archivos se pueden abrir en varios modos, R (default) solo para leer, W para escribir, A para añadir
    print(file.read())

with open(file_path, "w") as file: # los archivos se pueden abrir en varios modos, R (default) solo para leer, W para escribir, A para añadir
    file.write("borramos y ponemos de 0")

with open(file_path, "r") as file: # los archivos se pueden abrir en varios modos, R (default) solo para leer, W para escribir, A para añadir
    print(file.read())