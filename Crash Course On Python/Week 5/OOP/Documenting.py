class Apple:
    def __init__(self, color, flavor): # este método lo usaremos como constructor
        self.color = color
        self.flavor = flavor
    def __str__(self): # este método lo usaremos para dar una descripción de la instancia de la clase
        return "This apple is {} and its flavor is {}.".format(self.color, self.flavor)


help(Apple)

def to_seconds(hours, minutes, seconds):
    """Returns the amnount of seconds in the given hours, minutes and seconds."""
    return hours*3600+minutes*60+seconds

help(to_seconds)