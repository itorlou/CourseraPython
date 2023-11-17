#!/usr/bin/env python3
import os
import requests

# declaramos variable con el contenido de los archivos de reviews
src_dir = "/data/feedback/"

# hacemos una lista de archivos
files = os.listdir(src_dir)

# funcion para pasar las líneas a una lista
def readlines(file):
    with open(src_dir + file) as f:
        lines = f.read().splitlines()
    return lines


# load feedback entries into dictionary:
feedback = []
keys = ["title", "name", "date", "feedback"]
for file in files:
    lines = readlines(file)
    feedback.append(dict(zip(keys, lines)))

# seteamnos la url
url = "http://localhost/feedback/"

# mandamos las entradas
for entry in feedback:
    response = requests.post(url, data=entry)
    if response.ok:
        print("loaded entry")
    else:
        print(f"load entry error: {response.status_code}")