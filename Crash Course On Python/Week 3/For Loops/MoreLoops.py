def to_celsius(X):
    return (X-32)*5/9

for x in range(0,101,10): # de 0 a 101 en pasos de 10
    print(x, round(to_celsius(x)))