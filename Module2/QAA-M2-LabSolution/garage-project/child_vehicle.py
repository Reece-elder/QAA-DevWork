from Vehicle import * 

class Car(Vehicle):
    def __init__(self, condition, age, doors, convertible, electric):
        super().__init__(condition, age)
        self.doors = doors
        self.convertible = convertible
        self.electric = electric

    def fixVehicle(self):
        cost = 100
        if self.condition == "A":
            cost = 100
        elif self.condition == "B":
            cost = 200
        elif self.condition == "C":
            cost = 400
        
        cost = cost + (self.age * 2)

        cost = cost + (self.doors * 10)

        if self.convertible:
            cost = cost * 1.8

        if self.electric:
            cost = cost * 1.2

        return cost
