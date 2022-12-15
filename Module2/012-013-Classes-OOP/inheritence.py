from cProfile import run

class Bird:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
    
    def makeNoise(self):
        return "Caw Caw!"

class Penguin(Bird):
    def __init__(self, name, colour, swimSpeed):
        super().__init__(name, colour)
        self.swimSpeed = swimSpeed

    def makeNoise(self):
        # I googled this and this is what reddit told me penguin sounds as text are..
        return "Gak Gak Gak"

class Ostrich(Bird):
    def __init__(self, name, colour, runSpeed):
        super().__init__(name, colour)
        self.runSpeed = runSpeed

    def makeNoise(self):
        return "Chirp Chirp Hisssss"

pingu = Penguin("Pingu", "Black and White", 20)
olly = Ostrich("Olly", "Beige", 30)
print(pingu.makeNoise())

