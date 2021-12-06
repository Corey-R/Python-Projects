

import sqlite3

peopleValues = (('Ron', 'Obvious', 42), ('Luigi', 'Vercotti', 43), ('Arthur', 'Belling', 28))

with sqlite3.connect('C:/Users/Corey Reid/Desktop/test_database.db') as connection:
    c = connection.cursor()
    c.execute("DROP TABLE IF EXISTS People")
    c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")
    c.executemany("INSERT INTO People VALUES (?, ?, ?)",
                  peopleValues)

    # select all first and last names over age 30
    c.execute("SELECT FirstName,Lastname FROM People WHERE Age > 30")
    while True:
        row = c.fetchone()
        if row is None:
            break
        print(row)
              
