frutas = ["Plátano","Melón","Sandía","Piña"]

frutas.append("Manzana") # siempre lo añade al final

print(frutas)

frutas.insert(0,"Naranja") # si queremos ponerlo en una posición en concreto tendremos que usar insert, podemos usar un número más grande que el tamaño de la lista y lo añadirá al final

print(frutas)

frutas.remove("Melón") #elimina el que indiquemos, si le mandamos uno que no está dará error

print(frutas)

frutas.pop(3) #elimina esa posición de la lista

print(frutas)

frutas[2]="Melocotón" #modificamos el valor de un elemento de la lista

print(frutas)