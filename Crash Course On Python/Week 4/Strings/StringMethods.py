pets = "Cats & Dogs"

print(pets.index("&"))

print(pets.index("Dog"))

print(pets.index("s")) # si hay más de una iguales solo nos enseña la primera

print("x" in pets)

print("Cat" in pets)


print( "Mountains".upper()) #pasa a mayus
print( "Mountains".lower()) #pasa a minus

print( "  yes  ".strip()) # quita los espacios en blanco
print( "  yes  ".lstrip()) # quita los espacios en blanco de la izq
print( "  yes  ".rstrip()) # quita los espacios en blanco de la dcha

print( "El perro de san roque no tiene rabo".count("e")) # dice el número de veces que aparece esa string

print("forest".endswith("est")) #devuelve true o false si la cadena termina en lo que va entre paréntesis

print("forest".isnumeric())

print("12345".isnumeric()) #devuelve true si es un numero

print(" ".join(["This","is","a","phrase"])) #recibe una lista de strings y las une con el caracter que pongamos

print("This is another example".split()) #separa todas las palabras y las pasa a un array