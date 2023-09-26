class Apple:
    def __init__(self, color, flavor): # este método lo usaremos como constructor
        self.color = color
        self.flavor = flavor
    def __str__(self): # este método lo usaremos para dar una descripción de la instancia de la clase
        return "This apple is {} and its flavor is {}.".format(self.color, self.flavor)


golden = Apple("yellow","soft")

print(golden.flavor)

print(golden)