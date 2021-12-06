

import sqlite3

# get personal info from user
firstName = input("Enter your First Name: ")
lastName = input("Enter your Last Name: ")
age = int(input("Enter your age: "))
personData = (firstName, lastName, age) # creates a tuple containing the values from user's input

# execute insert statement for supplied person data
# remember to use the file path where the database was created
# otherwise, it will create a new database
with sqlite3.connect('C:/Users/Corey Reid/Desktop/test_database.db') as connection:
    c = connection.cursor()
    c.execute("INSERT INTO People VALUES (?, ?, ?)", personData)
connection.close()

with sqlite3.connect('C:/Users/Corey Reid/Desktop/test_database.db') as connection:
    c = connection.cursor()
    c.execute("UPDATE People SET Age=? WHERE FirstName=? AND LastName=?",
              (45, 'Luigi', 'Vercotti'))
