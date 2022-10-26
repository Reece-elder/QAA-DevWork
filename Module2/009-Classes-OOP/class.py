class Cake:
    colour = "Brown"
    tiers = 3
    decorated = True
    def bake(self):
        print("In the oven now!")

caterpillar_cake = Cake()
print(caterpillar_cake)
print(caterpillar_cake.colour)
caterpillar_cake.bake()

class CakeConstructor:
    def __init__(self, colour, tiers, decorated):
        self.colour = colour
        self.tiers = tiers
        self.decorated = decorated
        
    def bake(self):
        print("In the oven now!")

blackForest = CakeConstructor("Black", 3, True)
print(blackForest.colour)

# Get Attribute used to retrieve the attribute value
print(getattr(blackForest, 'tiers'))

# Has Attribute checks if this object has that attribute
print(hasattr(blackForest, 'calories'))

setattr(blackForest, 'calories', 12000)
print(hasattr(blackForest, 'calories'))

delattr(blackForest, 'calories')

# Exercise 
# Create a constructor of a type of animal of your choice, the constructor must include 3 unique variables and 1 function
# Create 2x objects of this constructors and make commands for the getattr, hasattr, setattr, delattr

