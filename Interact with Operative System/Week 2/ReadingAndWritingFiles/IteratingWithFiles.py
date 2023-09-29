with open("spider.txt") as file:
    for line in file: #recorremos el archivo línea por línea
            print(line.strip().upper()) 
            #para quitar las líneas vacias podemos usar strip



file = open("spider.txt")
lines= file.readlines()
file.close()

lines.sort()
print(lines)