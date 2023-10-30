import subprocess
subprocess.run(["date"]) # ejecución de hilos, hasta que no acabe el hilo no terinará el script padre

subprocess.run(["sleep", "2"])

result = subprocess.run(["ls", "this_file_does_not_exists"])
# aquí capturamos el resultado dentro de la variable result, devolverá un 2 puesto que tiene un error

print(result.returncode)