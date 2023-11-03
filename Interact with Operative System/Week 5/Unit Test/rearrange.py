# used to verify that small,  isolated parts of a program are correct

import re 

def rearrange_name(name):
    result = re.search(r"^([\w .]*), ([\w .]*)$", name)
    
    #al haber comprobado que la cadena vacía producía un error pasamos a depurar el código para incluir ese edge case
    if result is None:
        return  name
    

    return "{} {}".format(result[2], result[1])
