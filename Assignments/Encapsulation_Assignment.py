

# defining a class
class Protect:
    # defining __init__(self) method
    def __init__(self):
        self._protectedVar = "Hello" # setting protected variable a string value
        self.__privateVar = 'World!' # storing private variable a string value

    def Print(self): # defining method print()
        # by placing str() around each variable,
        # we are matching their data types to string
        # preventing any potential errors when combining 
        print(str(self._protectedVar) + ', ' + str(self.__privateVar))
        

    # defines a set() method
    # passing a private parameter

"""
    This allows the varaible 'self.__privateVar' to be 
    set by the user without altering any of the source code
    created. (Encapsulates)
"""
    def Set(self, private):
        # This sets the the variable to a new value
        # The value of (private) must be given as an argument when calling
        # this method
        self.__privateVar = private


# controls the flow (or order) of operations
if __name__ == "__main__":
    obj = Protect() # gives variable 'obj' access to the Protect() class
    obj.Print() # performs actions in this method
    obj.Set('Everyone!') # calls method with argument value ('Everyone!')
    obj.Print() # recalls method with new value
        
