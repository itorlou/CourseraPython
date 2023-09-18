x = 0  # inicializamos

while x < 5:  # condición para que siga ejecutándose
    print("No there yet, x =", x)
    x += 1

print("x = ", x)  # salimos del while

################################


def attempts(n):
    X = 1
    while X < n:
        print("Attemp ", X)
        X += 1
    print("Done")


attempts(5)
