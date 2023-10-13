import re

result = re.search(r"aza","plaza") # r = rawstring, tal como está 

print(result) # es un match object

result = re.search(r"aza","bazaar")
print(result) # es un match object

result = re.search(r"aza","maze")
print(result) # si no está devuelve un none

result = re.search(r"^x","xenon") # ^al principio
print(result) # 



result = re.search(r"p.ng","penguin") # . reemplaza cualquier caracter
print(result) 

result = re.search(r"p.ng","sponge") # . reemplaza cualquier caracter
print(result) 


result = re.search(r"p.ng","Pangea", re.IGNORECASE) # re.IGNORECASE para que no tenga en cuenta las mayus
print(result) 