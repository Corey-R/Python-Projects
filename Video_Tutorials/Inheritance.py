

# Defining a parent class
class Organism:
    # creating attributes
    name = "Unknown"
    species = "Unknown"
    legs = None # None gives legs a value of "nothing" 
    arms = None # None is not a sting or integer but has a data type of "None"
    dna = "Sequence A"
    origin = "Unknown"
    carbon_based = True

    # creating a method unique to this class
    def information(self): # self is a keyword that allows access to the attributes of the class
        msg = "\nName: {}\nSpecies: {}\nLegs: {}\nArms: {}\nDNA: {}\nOrigin: {}\nCarbon Based: {}".format(self.name,self.species,self.legs,self.arms,self.dna,self.origin,self.carbon_based)
        return msg # returns the value of the variable msg


# child class instance
class Human(Organism):
    # attributes for child class
    name = "MacGayver"# overrides the name attribute from the parent class
    species = "Homosapian"
    legs = 2
    arms = 2
    origin = 'Earth'

    # creating a method unique to this child class
    def ingenuity(self):
        msg = "\nCreates a deadly weapon using only a paper clip, chewing gum, and a roll of duck tape!"
        return msg

# creating another child class instance
class Dog(Organism):
    name = 'Spot'
    species = 'Canine'
    legs = 4
    arms = 0
    dna = 'Sequence B'
    origin = 'Earth'

    # creating a method unique to this child class using (self)
    def bite(self):
        msg = "\nEmits a loud, menacing growl and bites down ferociously on its target!"
        return msg

# creating another child class instance
class Bacterium(Organism):
    name = 'X'
    species = 'Bacteria'
    legs = 0
    arms = 0
    dna = 'Sequence C'
    origin = 'Mars'

    # unique method for child class
    def replication(self):
        msg = "\nThe cells begin to divide and multiply into two separate organisms!"
        return msg



if __name__ == "__main__":
    # instantiate ech of the classes
    human = Human()
    print(human.information())
    print(human.ingenuity())

    dog = Dog()
    print(dog.information())
    print(dog.bite())

    bacteria = Bacterium()
    print(bacteria.information())
    print(bacteria.replication())
