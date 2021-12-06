
import sqlite3

def New_db():
    conn = sqlite3.connect(":memory:")
    with conn:
        c = conn.cursor()        
        c.execute("CREATE TABLE IF NOT EXISTS Roster( \
                        Name TEXT, \
                        Species TEXT, \
                        IQ TEXT \
                        );")

        # populate the table with data
        specValues = (("Jean-Baptiste Zorg", "Human", "122",), ("Korben Dallas", "Meat Popsicle", "100"), ("Ak'not", "Mangalore", "-5"))
        c.executemany("INSERT INTO Roster VALUES (?, ?, ?)",
                           specValues)

        # this displays all names and IQs whose species is Human
        c.execute("SELECT Name, IQ FROM Roster WHERE Species = 'Human'")
        for entry in c.fetchall():
            print(entry, "\n")

            
        # this updates Korben Dallas species to Human
        c.execute("UPDATE Roster SET Species=? WHERE Name=? AND IQ=?",
                  ('Human', 'Korben Dallas', '100'))

        # this displays all names and IQs whose species is Human
        c.execute("SELECT Name, IQ FROM Roster WHERE Species = 'Human'")
        print("UPDATED TABLE: All that are Human \n")
        for entry in c.fetchall():
            print(entry)
        
        conn.commit()
        
    conn.close()





if __name__ == "__main__":
    New_db()
    
   
    
        
                  
            
        
                                                                                                           
