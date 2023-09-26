# class Apple: #iniciamos una clase y le ponemos el nombre con la primera en mayus
#     pass #indentamos a la derecha y le ponemos pass para que no haga nada

class Apple:
    color = ""
    flavour = "" 


jonagold = Apple() # creamos una nueva instancia de la clase apple

#le pasamos los valores a los atributos

jonagold.color = "red"
jonagold.flavour= "sweet"

print(jonagold.color.capitalize() , jonagold.flavour)

golden = Apple()

golden.color = "yellow"
golden.flavour = "soft"