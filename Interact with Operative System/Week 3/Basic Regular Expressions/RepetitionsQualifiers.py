import re

print(re.search(r"Py.*n","Pygmalion")) #. cualquiera * varios caracteres

print(re.search(r"Py.*n","Python Programming")) #. pilla el maximo de caracteres que puede
# si no queremos que sea tan greedy tenemos que usar character classes
print(re.search(r"Py[a-z]*n","Python Programming")) #. 


print(re.search(r"Py[a-z]*n","Pyn")) #. puede ser que el patrón no exista

# introducimos el uso de + para letras que se puedan repetir

print(re.search(r"o+l+","gold"))

print(re.search(r"o+l+","woolly"))

print(re.search(r"o+l+","boil")) # hay un caracter en el medio, entonces no lo pilla

# introducimos el uso de ? para una o cero ocurrencias

print(re.search(r"p?each","each"))

print(re.search(r"p?each","peach"))