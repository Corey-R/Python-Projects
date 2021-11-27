

"""
    CREATING TWO CHILD CLASSES
    For each child class, inherit all attributes from their parent
    class and ensure each child class has their own two unique attributes...
"""

# Defining the parent class
# NOTE: These are only default values
class Pets:
    Species = " "
    Color = " "
    Legs = 0

# Defining the child class 'Dogs'
class Dogs(Pets): # (Pets) allows this class to inherit from the parent class
    Age_Months = 0 # Attribute unique to this class
    Breed = "Dog Breed" # ^^^^

# Defining the child class "Birds" inheriting (Pets) class
class Birds(Pets):
    Feed = "Bird seed" # Attribute unique to 'Birds' class
    Cage_Size_Inches = 0.00 # ^^^^
    
