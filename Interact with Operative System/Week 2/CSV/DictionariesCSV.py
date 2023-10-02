from os.path import dirname, join
import csv

current_dir = dirname(__file__)
file_path = join(current_dir, "./software.csv")
# leer como diccionario, con claves
with open(file_path) as software:
    reader = csv.DictReader(software)
    for row in reader:
         print("{} has {} users".format(row["name"], row["users"]))


# Escribir en un csv con diccionarios
users =[{"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"},{"name": "Lio Nelson", "username":"lion","department": "User Experience Research"},{"name": "Charlie Grey", "username": "greyc" ,"department": "Development"}]

keys =["name", "username", "department"]

file_path2 = join(current_dir, "./by_department.csv")

with open(file_path2, 'w') as by_department:
     writer = csv.DictWriter(by_department, fieldnames=keys)
     writer.writeheader()
     writer.writerows(users)