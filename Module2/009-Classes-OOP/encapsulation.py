# Encapsulation
class BankAccount:
    # _leading underscore suggests the variable SHOULD be private.. 
    # but Python doesnt do anything to support this. Purely a conventional thing
    _pin = "1234"
    _money = 100

    def deposit(self, money, pin):
        if(pin == self._pin):
            self._money += money
            return True

    def withdraw(self, money, pin):
        if(pin == self._pin):
            self._money -= money
            return True

    def displayMoney(self, pin):
        if(pin == self._pin):
            return self._money

    def setFeathers(self, feathers):
        if type(feathers) is str:
            print("Yep, this works")
        else:
            print("Not a string :( ")
    
myBank = BankAccount()
print(myBank.deposit(500, "1234"))
print(myBank.displayMoney("1234"))