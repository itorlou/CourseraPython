#create lists in a shorter way

multiples = []
for x in range(1,11):
    multiples.append(x*7)

print(multiples)

multiples2 = [x*7 for x in range(1,11)]

print(multiples2)

languages= ["Python", "Perl" ,"Ruby" ,"Go"," Java" , "C"]
lengths = [len(language) for language in languages]

print(lengths)

z = [x for x in range(0,101) if x % 3 == 0]
print(z)