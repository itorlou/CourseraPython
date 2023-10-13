log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"

log2 = "July 31 07:51:48 mycomputer bad_process[1232312345]: ERROR Performing package upgrade"
index = log.index("[")

print(log[index+1:index+6])

#podríamos tener un problema si este número se modifica si se reinician los servidores o si  añadimos otro corchete después del primero

 # para solucionar esto importaremos se para utilizar su función search para buscar expresiones regulares dentro de las strings

import re 

regex = r"\[(\d+)\]"

result = re.search(regex, log2)
print(result[1])
