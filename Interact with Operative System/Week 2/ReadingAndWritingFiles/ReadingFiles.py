file = open("spider.txt") # abrimos archivo
  
print(file.readline()) # leemos una línea y avanzamos el puntero

print(file.readline())

print(file.read()) # empieza a leer desde donde estemos hasta el final

file.close() # cerramos el archivo

# usando el with 

with open("spider.txt") as file:
    print(file.readline())
    # así python cierra automáticamente el archivo 


