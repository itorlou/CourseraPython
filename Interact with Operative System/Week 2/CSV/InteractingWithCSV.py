from os.path import dirname, join
import csv

current_dir = dirname(__file__)
file_path = join(current_dir, "./employees.csv")

file = open(file_path) # abrimos archivo


csv_f = csv.reader(file) #indexamos el csv

for row in csv_f: #entramos al csv con el index 
    name,phone,role = row # parseamos la línea
    print("Name: {} , Phone: {}, Role {}".format(name, phone, role))

file.close()