#pares clave, valor

x = {}

print(type(x))

file_counts ={"jpg":10, "txt":14, "csv":2, "py":23}
print(file_counts)

print(file_counts["txt"])

print("jpg" in file_counts)

file_counts["cfg"] = 8

print(file_counts)

file_counts["cfg"] = 18

print(file_counts)

del file_counts["cfg"]

print(file_counts)