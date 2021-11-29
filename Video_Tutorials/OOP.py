


class Game: # Defined a class 'Game'
    # Attributes and values of the class
    variable1 = 'Hello'
    variable2 = 'World!'






















if __name__ == "__main__":
    # Instantiates the class creating a class object
    # NOTE: you can have multiple instances of a class
    x = Game() # Builds a class object with a name of 'x'
    # We can now call the class object by it's new name "x"
    print(x.variable1) # prints the value stored in variable1 of Game() class object named 'x'
    # 'Hello' is printed
    print(x.variable2)
    """
        It prints Hello
                  World!
        which isn't very clean.
        So, to fix this we can use wildcards and
        the '.format' method.
    """
    print("{} {}".format(x.variable1,x.variable2))
    # This statement prints "Hello World!" on the same line...
    
