

# import tkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox

# import associated modules
import student_gui
import student_main

# import os and sqlite3
import os # allows use of os module (os._exit() for example)
import sqlite3 # allows functionality of SQL

# This method centers the window of the user's screen
def center_window(self, w, h): # accesses the ParentWindow class, width, and height (400,700)
    screen_width = self.master.winfo_screenwidth() # <-- syntax used to get user's screen width
    screen_height = self.master.winfo_screenheight() # <-- syntax used to get user's screen height
    x = int((screen_width/2) - (w/2)) # half the user's width subtracted by half our created width
    y = int((screen_height/2) - (h/2)) # (user's width/2) - (700/2)
    centerWin = self.master.geometry('{}x{}+{}+{}'.format(w,h,x,y)) # <-- formula used to center the window
    return centerWin # returns the value (centered position) to the program that called this method

# defining the method to create our database
def create_db(self):
    conn = sqlite3.connect('student.db') # <-- connects (or creates if new) to the specified database
    with conn: # <-- "if connection successful, perform the following:"
        cur = conn.cursor() # storing cursor() method in variable for later use
        cur.execute("CREATE TABLE if not exists tbl_students( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_fullname TEXT, \
            col_phone TEXT, \
            col_email TEXT, \
            col_course TEXT \
            );")
        conn.commit() # <-- saves changes in database
    # NOTE: the indentation is important
    conn.close() # <-- closes the connection to the database
    first_run(self) # calls the specified method

# This method checks to ensure at least one record is in the database
# if there isn't, it will create a 'dummy' record to prevent errors
def first_run(self):
    conn = sqlite3.connect('student.db')
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur) #<-- calls the 'cont_records' method passing in (cur) to allow db acces
        # if no records were found in the db, add a dummy record
        if count < 1: # the value of count comes from the 'count_records' method
            cur.execute("""INSERT INTO tbl_students (col_fname,col_lname,col_fullname,col_phone,col_email,col_course) VALUES (?,?,?,?,?,?)""", ('Oscar', 'Wilde', 'Oscar Wilde', '312-231-1323', 'owilde@gmail.com', 'Psychology'))
            conn.commit()
    conn.close # remember to align the conn.close to the 'with' keyword

# checks if the database is empty and returns the results
def count_records(cur):
    count = "" #<-- default value of count
    cur.execute("""SELECT COUNT(*) FROM tbl_students""") # sql statement that counts the # of records in student table
    count = cur.fetchone() [0] # storing the # of records found in a variable named 'count'
    return cur,count # returns that number (along with sql functions) back to whatever calls this method

# This method allows ... on Select
def onSelect(self,event):
    varList = event.widget #<-- passing built-in event method to a variable
    select = varList.curselection()[0] #<-- grabs the index of the selected widget
    value = varList.get(select) #<-- gets the text value stored in selected index
    conn = sqlite3.connect('student.db') #<-- establishes a connection with the database
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT col_fname,col_lname,col_phone,col_email,col_course FROM tbl_students WHERE col_fullname = (?)""", [value])
        varBody = cursor.fetchall() #<-- retrieves all data associated with the selected value
        # This creates a tuple containing 5 parts
        # Creating a for loop to delete and insert the associated info into their respected textboxes in the window
        for data in varBody:
            self.tex_fname.delete(0, END) #<-- deletes content in the First Name textbox
            self.tex_fname.insert(0, data[0]) #<-- inserts the value in index 0 of the varBody tuple into the First Name textbox
            self.tex_lname.delete(0, END)
            self.tex_lname.insert(0, data[1])
            self.tex_phone.delete(0, END)
            self.tex_phone.insert(0, data[2])
            self.tex_email.delete(0, END)
            self.tex_email.insert(0, data[3])
            self.tex_course.delete(0, END)
            self.tex_course.insert(0, data[4])
    # NOTE: the connection doesn't close to ensure the selected data remains shown in the window's textboxes

# creating the submit method giving functionality to the submit button
# called by self.btn_submit in 'student_gui' module
def submit(self):
    var_fname = self.tex_fname.get() #<-- storing the value the user inputs in the First Name textbox into this variable
    var_lname = self.tex_lname.get() #<-- ^^^^^^^ lname ^^^^^^
    # normalize the data for database consistency
    var_fname = var_fname.strip() #<-- removes any extra white spaces before and after the value
    var_lname = var_lname.strip() #<-- ^^^^
    var_fname = var_fname.title() #<-- capitalizes the first letter
    var_lname = var_lname.title() #<-- ^^^^
    var_fullname = "{} {}".format(var_fname,var_lname) # combines First & Last Name into Fullname variable
    print("var_fullname: {}".format(var_fullname)) # shows the 'developer' a display of the full name (not the user)
    # get vales and strip white spacing for remaining values
    var_phone = self.tex_phone.get().strip()
    var_email = self.tex_email.get().strip()
    var_course = self.tex_course.get().strip().title()
    if not "@" or not "." in var_email:
        print("Invalid email format!!!")
    # if there is data in the following variables, perform the following:
    if (len(var_fname) > 0) and (len(var_lname) > 0) and (len(var_phone) > 0) and (len(var_email) > 0) and (len(var_course) > 0):
        conn = sqlite3.connect('student.db')
        with conn:
            cursor = conn.cursor()
            # check the db to see if the created fullname exists, if so, alert the user and cancel request to add new data
            cursor.execute("""SELECT COUNT (col_fullname) FROM tbl_students WHERE col_fullname = '{}'""".format(var_fullname))
            count = cursor.fetchone() [0] #<-- if a record is found with the value created in 'var_fullname' store it here
            chkName = count #<-- solely for naming convention purposes, this step isn't required you could just used count
            # if there's no full name in the db that matches the value of 'var_fullname', create a new record
            if chkName == 0:
                print("chkName: {}".format(chkName)) #<-- match verification for the developer only...
                cursor.execute("""INSERT INTO tbl_students (col_fname,col_lname,col_fullname,col_phone,col_email,col_course) VALUES (?,?,?,?,?,?)""", (var_fname,var_lname,var_fullname,var_phone,var_email,var_course))
                # update the listbox with changes
                self.listbox.insert(END, var_fullname)
                onClear(self) # clears all textboxes
            else:
                messagebox.showerror("Name Error", "'{}' already exists! \nPlease choose a different name.".format(var_fullname))
                onClear(self) 
        conn.commit() #<-- saves all changes since connection was established (note the indent)
        conn.commit() #<-- closes the established connection
    else:
        messagebox.showerror("Missing Text Error","Please ensure that there is data in all fields.")
                                                                                                            
# Creating the delete method giving functionality to the delete button
# called by the self.btn_delete in the 'student_gui' module
def delete(self):
    var_select = self.listbox.get(self.listbox.curselection()) # store listbox's selected value into the variable
    conn = sqlite3.connect('student.db')
    with conn:
        cur = conn.cursor()
        # checking to ensure the record requesting for deletion
        # is not the last record in the database
        cur.execute("""SELECT COUNT(*) FROM tbl_students""") #<-- counts all records in the db
        count = cur.fetchone() [0] #<-- stores the number of records here
        # if there's more than one record in the db, proceed to deletion promp
        # else, send messagebox alerting the user and cancel request
        if count > 1:
            confirm = messagebox.askokcancel("Are you sure?", "This will permanently remove all fields associated with {}, \n\nDo you wish to continue?".format(var_select))
            if confirm: # this occurs if the user clicks 'ok'
                # establish a connection to remove the requested record from the database
                conn = sqlite3.connect('student.db')
                with conn:
                    cursor = conn.cursor()
                    cursor.execute("""DELETE FROM tbl_students WHERE col_fullname = '{}'""".format(var_select))
                onDeleted(self) # calls this method after a record has been deleted
                conn.commit() # saves changes once instruction from 'with' are completed
        else:
            messagebox.showerror("Last Record", "({}) is the last record in our database and cannot be deleted currently. \n\nYou must add another record first before you can delete ({}).".format(var_select,var_select))
    conn.close()


def onDeleted(self):
    # clear the text in these textboxes
    self.tex_fname.delete(0,END)
    self.tex_lname.delete(0,END)
    self.tex_phone.delete(0,END)
    self.tex_email.delete(0,END)
    self.tex_course.delete(0,END)
    # onRefresh(self) # update the listbox of the changes
    try:
        index = self.listbox.curselection()[0]
        self.listbox.delete(index)
    except IndexError:
        pass

def onClear(self):
    # clear the text in these textboxes
    self.tex_fname.delete(0,END)
    self.tex_lname.delete(0,END)
    self.tex_phone.delete(0,END)
    self.tex_email.delete(0,END)
    self.tex_course.delete(0,END)
    

def onRefresh(self):
    # Populate the listbox, coinciding with the database
    self.listbox.delete(0,END)
    conn = sqlite3.connect('student.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT COUNT(*) FROM tbl_students""") #<-- sql statement that selects all records from students table
        count = cursor.fetchone()[0] #<-- store the total number of records here
        i = 0 # establishing a default integer value for i
        while i < count: # while loop iterates through all records found in the table
                cursor.execute("""SELECT col_fullname FROM tbl_students""") # grabs this column for each record
                varList = cursor.fetchall()[i] #<-- stores 'all' of each record's contents here
                for item in varList: #<-- for loop to iterate through each record to:\/ ('\/' = down arrow)
                    self.listbox.insert(0,str(item)) # insert all records found into the listbox as a string
                    i = i + 1 # <-- increments the i value (this allows i to eventually become greater than the total number of records counted)
    conn.close() # closes your connection with the database

# creating the ask_quit(self) method to display a messagebox to confirm the user's actions
def ask_quit(self):
    # if a messagebox appears after the user has clicked exit (or alt+F4)
    # and the user clicks 'ok' to close window:
    if messagebox.askokcancel("Close Window", "Are you sure you want to close this program? \n\nAny entries not submitted will not be saved. \nEnsure you've completed all tasks before clicking 'OK'."):
        self.master.destroy() # <-- build-in tkinter method that closes the app
        os._exit(0) #<-- built-in os method that closes ALL widgets and returns the user's memory back to prevent memory leaks
                    
    



# this controls the flow (or order) of operations performed in this module
if __name__ == "__main__":
    # pass tells the program once it's finished with this module to pass (or skip) on any specific methods
    # so it will parse from top to bottom
    pass














































































    

            
        

    
