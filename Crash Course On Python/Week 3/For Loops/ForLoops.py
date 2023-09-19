for x in range(5):
    print(x)

values = [ 23, 52, 59, 37, 48 ]
sum = 0
length =0
for value in values:
    sum += value
    length += 1

print("Total sum: ",sum, "Average:",sum/length)