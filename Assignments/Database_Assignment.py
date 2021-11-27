
# importing the sqlite3 database so we can leverage SQL query
import sqlite3

# we must establish a connection with the database which will be stored in a variable
conn = sqlite3.connect('files.db')

# Now, using the with keyword, we will create a table with 2 columns
with conn:
    # setting cur variable to establish our cursor() method
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileName \
        )") # the '\' is an escape character that allows multiline statements
    conn.commit() # commits changes to the database
conn.close() # closes the connection and prevents memory leaks

"""
    At this point, you want to check to ensure your table has been created by
    locating and opening the database in your DB Browser for SQLite.
    If the database did not exist already, it will be created in the same file path
    as your script. 
"""

# copying the fileList for the assignment

fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

# we must now establish another connection with our database to perform our next action
# NOTE: Ideally, you would want to create a function for this code for easier code reusability.

conn = sqlite3.connect('files.db') # remember to specify the database argument in '' to prevent an error

# we will now create a for loop to iterate through the above tuple
for items in fileList:
    if items.endswith('.txt'): # create an if statement to target specified files
        with conn:
            cur = conn.cursor()
            # We want to insert the file name of ONLY tuples that have the file extension '.txt'
            # The '?' is a wildcard denoting one column (don't forget the trailing comma denoting a tuple)
            cur.execute("INSERT INTO tbl_files(col_fileName) VALUES (?)", (items,))
        print(items) # will display all matching files into the shell
conn.close()
        
