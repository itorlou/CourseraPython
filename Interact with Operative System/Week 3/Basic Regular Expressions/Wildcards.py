import re 

print(re.search(r"[Pp]ython","Python")) # [las opciones que puede encontrar]


print(re.search(r"[a-z]way","The end of the highway")) # [las opciones que puede encontrar]

#podemos combinarlos

print(re.search(r"cloud[a-zA-Z0-9]","cloudy")) # 
print(re.search(r"cloud[a-zA-Z0-9]","cloud9")) # 


#para cualquier caracter usaremos [^]

print(re.search(r"[^a-zA-Z]","This is a sentence with spaces."))

print(re.search(r"[^a-zA-Z ]","This is a sentence with spaces.")) # si le pasamos un espacio al final negamos

print(re.search(r"cat|dog","I like cats.")) #con la pipe podemos pasarle varios
print(re.search(r"cat|dog","I like dogs."))
print(re.search(r"cat|dog","I like both dogs and cats."))

# para que encuentre todos los que coinciden usaremos findall

print(re.findall(r"cat|dog","I like both dogs and cats."))

