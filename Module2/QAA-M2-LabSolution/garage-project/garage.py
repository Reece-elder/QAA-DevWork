from hashlib import new
from operator import index
from child_vehicle import *


class Garage():

    garage_list = []

    def addToGarage(self,vehicle):
        self.garage_list.append(vehicle)

    def quoteVehicle(self, index):
        return f"Fix quote cost: {self.runFixVehicle(index)}"

    def fixVehicle(self, index):
        cost = self.runFixVehicle(index)
        self.removeVehicle(index)
        return f"Vehicle fixed, cost: {cost}"

    def printAllVehicles(self):
        for vehicle in self.garage_list:
            print(str(vehicle))

    def removeVehicle(self, index):
        del self.garage_list[index]
        return True

    def updateVehicle(self, index, vehicle):
        self.garage_list[index] = vehicle
        return f"Updated Garage List {index} with {vehicle.age}"

    def fixAllVehicles(self):
        index_count = 0
        total = 0
        for vehicle in self.garage_list:
            cost = self.runFixVehicle(index_count)
            total = total + cost
            print(f"Vehicle at index {index_count} cost: {cost}")
            index_count += 1

        return f"Total cost: {total}"

    def runFixVehicle(self, index):
        cost = self.garage_list[index].fixVehicle()
        return cost


newportGarage = Garage()
car1 = Car("B", 21, 5, True, False)
car2 = Car("A", 15, 3, False, False)
car3 = Car("C", 7, 2, True, True)

newportGarage.addToGarage(car1)
print(newportGarage.quoteVehicle(0))
print(newportGarage.fixVehicle(0))
newportGarage.addToGarage(car1)
newportGarage.addToGarage(car2)
newportGarage.addToGarage(car3)
print(newportGarage.quoteVehicle(1))
newportGarage.printAllVehicles()
print(newportGarage.fixAllVehicles())
