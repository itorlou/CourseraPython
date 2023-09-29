from os.path import dirname, join

current_dir = dirname(__file__)
file_path = join(current_dir, "./spider.txt")

file = open(file_path) # abrimos archivo
  
print(file.readline()) # leemos una línea y avanzamos el puntero

print(file.readline())

print(file.read()) # empieza a leer desde donde estemos hasta el final

file.close() # cerramos el archivo

# usando el with 

with open(file_path) as file:
    print(file.readline())
    # así python cierra automáticamente el archivo