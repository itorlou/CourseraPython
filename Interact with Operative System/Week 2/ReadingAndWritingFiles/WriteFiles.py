from os.path import dirname, join

current_dir = dirname(__file__)
file_path = join(current_dir, "./novel.txt")

with open(file_path, "w") as file: # los archivos se pueden abrir en varios modos, R (default) solo para leer, W para escribir
    file.write("Era una noche oscura y tormentosa")