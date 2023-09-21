file_counts ={"jpg":10, "txt":14, "csv":2, "py":23}
print(file_counts)

for extension in file_counts:
    print(extension)

for ext, amount in file_counts.items():
    print ("there are {} files withh the .{} extension".format(amount, ext))

print(file_counts.keys())

print(file_counts.values())

for value in file_counts.values():
    print(value)


def count_letters(text):
    result = {}
    # Go through each letter in the text
    for letter in text:
      # Check if the letter needs to be counted or not
        if letter not in result:
            result[letter.lower()] = 1
        # Add or increment the value in the dictionary
        else:
            result[letter.lower()] += 1
    return result

print(count_letters("A long text"))