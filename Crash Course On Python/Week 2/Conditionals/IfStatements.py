# construiremos una función que diga si el nombre del usuario es válido
# la condición es que tenga 3 caracteres o más

def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    elif len(username) > 15:
        print("Invalid username. Must be at most 15 characters long")
    else:
        print("Valid username")

hint_username("as")

hint_username("IsaacTorradoLoureiro")

hint_username("asp")

#sin usar el else pero tenemos que usar return para que se termine el if 

def is_even(number):
    if number % 2==0:
        return True
    return False

print(str(is_even(5)))

print(str(is_even(8)))