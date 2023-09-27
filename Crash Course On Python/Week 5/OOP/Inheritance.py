class Fruit:
    def __init__ (self, color, flavor):
        self.color= color
        self.flavor= flavor

class Apple(Fruit): # heredan de la clase madre
    pass

class Grape(Fruit):
    pass

granny_smith = Apple("green","tart")
carnelian = Grape("purple","sweet")

print(granny_smith.flavor)

print(carnelian.color)