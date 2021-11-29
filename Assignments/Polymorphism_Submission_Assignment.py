
"""
    POLYMORPHISM SUBMISSION ASSIGNMENT 
"""

# creating the parent class
class Gym:
    # NOTE: To allow authentication, values are stored in this class
    # as a pseudo-database.
    fname = "Courage"
    lname = "Dog"
    DOB = "October 18, 1996"
    username = "Cowardly"
    email = "cdog@outlook.com"
    password = "Murial"
    Active = True

    # method of the parent class
    def memberLogin(self): # <-- Grants access to the above class
        # creating a while loop to allow multiple attempts
        # NOTE: Ideally, you would want to restrict the number of attempts to prevent cyber attacks
        go = True
        while go:
            entry_username = input("Enter Username or Email: ")
            entry_password = input("Enter Password: ")
            # make an if statement to verify member information
            if entry_username == self.username or self.email and entry_password == self.password:
                msg = "\nWelcome Back {}! \nLet's break a sweat!".format(self.username)
                return msg
                go = False # this stops the Loop if successful
            # make an else statement if values did not match
            else:
                print("\nInvalid Username or Password! Try again...\n\n")

# creating a child class
class Trainer(Gym):
    # override values from parent class
    fname = "Trevor"
    lname = "Merks"
    DOB = "February 12, 2002"
    # Unique attribute 
    TrainerID = "000321"
    # Overridden attribute
    email = "trevmerk@outlook.com"
    # Unique attribute
    PIN = 5990 
    # Unique attribute
    Active_License = True

    # Using the same naming convention for this method
    # with different values for this child class
    def memberLogin(self):
        go = True
        while go:
            entry_ID = input("Enter TrainerID: ")
            entry_PIN = input("Enter PIN: ")
            # make an if statement to verify member information
            if entry_ID == self.TrainerID and entry_PIN == self.PIN:
                msg = "\nWelcome {}! \nLet's guide and sculp the world!".format(self.fname)
                return msg
                go = False # this stops the Loop if successful
            # make an else statement if values did not match
            else:
                print("\nInvalid ID or PIN! Please try again...\n\n")

# creating another child class with unique attributes
class Manager(Gym):
    fname = "Todd"
    lname = "Mathews"
    DOB = "June 10, 1980"
    # Unique attribute
    mng_id = 503125
    # Unique attribute
    mng_pin = 2032
    # Overridden attribute
    email = "toddDodge@gmail.com"
    # Unique attribute
    Branch_Location = "Grenada"

    # creating a method for this child class
    # same naming convention, different values
    def memberLogin(self):
        go = True
        while go:
            entry_MngID = input("Enter ManagerID: ")
            entry_MngPIN = input("Enter PIN: ")
            # make an if statement to verify member information
            """
                NOTE: For the if statement to work successfully,
                you must match the data types of raw data 'entry_MngID'
                with the stored value 'self.mng_id' by converting the
                raw data into an integer 'int(entry_MngId) == self.mng_id
            """
            if int(entry_MngID) == self.mng_id and int(entry_MngPIN) == self.mng_pin:
                msg = "\nGreetings {}! Here are your daily reports!".format(self.fname)
                return msg
                go = False # this stops the Loop if successful
            # make an else statement if values did not match
            else:
                print("\nInvalid ID or PIN! Please try again...\nif problem persists, consult with the tech specialist \nor reset ID/PIN.\n\n")
        
    

        
        

        


if __name__ == "__main__":
    # storing classes in variables
    welcome = Gym()
    greetings = Trainer()
    salutation = Manager()
    # using memberLogin() to call the method for each class
    print(salutation.memberLogin())
    

    
        
