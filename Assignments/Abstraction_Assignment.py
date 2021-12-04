
# Import a Python built-in class ABC (abstract base class)
from abc import ABC, abstractmethod

# defining a child class inheriting the ABC class
class Sale(ABC):
    # defining a method that will print in the console
    def Total(self, amount):
        print('Your total: ', amount)
    # this abstract method passes the parameter (amount)
    def payment(self, amount):
        pass #<-- will pass the argument to the program that calls it

# This next class will inherit the attributes from Sale AND ABC
class Debit(Sale):
    # Creating a polymorphism method
    # This will implement the payment method from the parent class
    # and change it's attributes for this child class
    def payment(self, amount):
        print("Transaction Complete! \n{} has been processed on your card!".format(amount))

# Controlling flow of operations
if __name__ == "__main__":
    obj = Debit() #<-- contains all classes inherited
    obj.Total('$200') #<-- passes argument of '$200' in 'amount'
    obj.payment('$200') #<-- ^^^^
    
    
