




# creating a class
class Snacks:
    # using the __init__ dunder
    def __init__(self, brand, amount, size, price, flavor, store):
        # setting the above class attribute equal to
        # the class object's values
        self.brand = brand
        self.amount = amount
        self.size = size
        self.price = price
        self.flavor = flavor
        self.store = store

    # creating a method for 'snacks' class that will returna message
    def inventory(self): # self argument gives access to the 'Snacks' class
        msg = "INVENTORY \nProduct: {} {} \nAmount: {} \nSize: {} \nPrice: {} \nStore: {}".format(self.flavor,self.brand,self.amount,self.size,self.price,self.store)
        return msg
    
    


# creating a child class to the now parent class 'Snacks'
class Drinks(Snacks):
    """
        NOTE: This class will inherit all of the above properties
        However, I could give this class unique attributes if chosen.
    """
    # creating a method for this child class that returns a message
    def storage(self):
        msg = "\n\nProduct: {} {} \nQuantity: {} \nSize: {} \nStore {} \nPrice: {}".format(self.flavor,self.brand,self.amount,self.size,self.store,self.price)
        return msg







if __name__ == "__main__":
    # creating the class object
    # storing an object with arguments into a variable 'Chips'
    chips = Snacks("Ruffles", "348 Boxes", "Family Size", "$3.95", "Queso-Cheddar", "Walmart")
    # this calls the method inventory()
    # the 'chips.' tells the program to use the following
    # variable containing overridden data
    print(chips.inventory())

    # creating a child class object
    drinks = Drinks("Coke", "32 Crates", "2-Liter", "$2.78", "Cherry", "Walmart")

    # calling the child class's 'storage()' method
    print(drinks.storage())
