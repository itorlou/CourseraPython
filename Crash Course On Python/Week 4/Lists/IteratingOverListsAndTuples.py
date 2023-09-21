animals = ["Lion","Zebra","Dolphin","Monkey"]

chars = 0

for animal in animals:
    chars += len(animal)


print("Total characters: {}, Average lenght: {}".format(chars, chars/len(animals)))


winners = ["Pepe","Luis","Ana"]

for index, person in enumerate(winners): #usando la función enumerate
    print("{} - {}".format(index +1, person))



def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result

print(full_emails([("alex@example.com", "Alex Diego"),("shay@example.com", "Shay Brandt")]))