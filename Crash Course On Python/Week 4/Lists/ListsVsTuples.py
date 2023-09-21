#una tupla es una lista de elementos inmutable

fullname = ("Isaac", "T", "Loureiro")

print(fullname)
#las usaremos para situaciones en las que queremos que los elementos no se modifiquen y ocupen siempre su posición

# se usan normalmente para contener los valores que devuelve una función

def convert_seconds(Seconds):
    Hours = Seconds // 3600
    Minutes = (Seconds - Hours * 3600) // 60
    Remaining_seconds = Seconds - Hours * 3600 - Minutes * 60
    return Hours, Minutes, Remaining_seconds

result= convert_seconds(5000)
print(type(result))