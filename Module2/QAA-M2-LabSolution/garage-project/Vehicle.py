from abc import abstractmethod

class Vehicle:
    def __init__(self, condition, age):
        self.condition = condition
        self.age = age

    @abstractmethod
    def fixVehicle(self):
        pass