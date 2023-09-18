# while x % 2 == 0: si metemos el valor x =0 entonces entraríamos en un bucle infinito
#     x = x / 2

# para evitar eso podemos concatenar una comprobación con un operador lógico

x = 64

while x!=0 and x % 2 == 0:
    x = x/2
    print(x)