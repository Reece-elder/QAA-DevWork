from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

class Penguin(Animal):
    def __init__(self, feathers, name):
        self.feathers = feathers
        self.name = name

    def eat(self):
        return "*Fish eating Noises*"


    