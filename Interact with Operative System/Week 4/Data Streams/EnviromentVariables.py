import os 

#con el get conseguimos que si la variable no está presente devuelva una cadena alternativa
print ("HOME "+ os.environ.get("HOME", ""))
print ("SHELL "+ os.environ.get("SHELL", ""))
print ("FRUIT "+ os.environ.get("FRUIT", ""))

# la añadimos con export FRUIT=Pineapple desde el shell