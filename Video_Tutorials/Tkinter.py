
# import the tkinter module to gain access to its syntax
import tkinter
from tkinter import * # imports all widgets from tkinter module 

# Blupring for creating a tkinter window
class ParentWindow(Frame): # (Frame) is the parent class within the tkinter module
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        # this allows the window to be resized if True
        # if False, the ability to resize the window will not work
        self.master.resizable(width=True, height=True) 
        self.master.geometry('{}x{}'.format(700, 400)) # specifies window size in pixels
        self.master.title('Learning Tkinter!')
        # this allows you to alter the background
        self.master.config(bg='lightgray')

        # How to create variables in tkinter and use them
        self.varFName = StringVar()
        self.varLName = StringVar()
        # Assign a value to the variables
        # set() means to assign it a value


        # create labels for the text boxes
        # this instantiates a class object
        self.lblFName = Label(self.master,text='First Name: ',font = ("Helvetica", 16),fg='black',bg='lightgray')

        # this paints the class object to the tkinter window
        self.lblFName.grid(row=0, column=0,padx=(30,0), pady=(30,0)) # padx=(left,right), pady=(top, bottom)

        self.lblLName = Label(self.master,text='Last Name: ',font = ("Helvetica", 16),fg='black',bg='lightgray')        
        self.lblLName.grid(row=1, column=0,padx=(30,0), pady=(30,0))

        self.lblDisplay = Label(self.master,text='',font = ("Helvetica", 16),fg='black',bg='lightgray')
        self.lblDisplay.grid(row=3, column=1,padx=(30,0), pady=(30,0))

        # this paints our text box
        # this instantiates from tkinter one of the widgets we've already imported
        self.txtFName = Entry(self.master, text = self.varFName, font = ("Helvetica", 16), fg='black', bg='lightblue')
        # 'Entry' creates a signle line text box for input

        # references self.txtFName so we can actually use it's values
        # add a geometry manager to the reference variable so it can paint the values
        # .pack() is a geometry manager that places the contents in the window with no specification
        # .grid() places the contents in a specified position of the tkinter window
        self.txtFName.grid(row=0, column=1,padx=(30,0), pady=(30,0))

        # the grid( geometry manager requires parameters to specify where to place the content
        self.txtLName = Entry(self.master, text = self.varLName, font = ("Helvetica", 16), fg='black', bg='lightblue')
        self.txtLName.grid(row=1, column=1,padx=(30,0), pady=(30,0))

        # this creates buttons for the form
        self.btnSubmit = Button(self.master, text="Submit", width=10, height=2, command=self.submit)
        self.btnSubmit.grid(row=2, column=1, padx=(0,0), pady=(30,0), sticky=NE) #NE for North East

        self.btnCancel = Button(self.master, text="Cancel", width=10, height=2, command=self.cancel)
        self.btnCancel.grid(row=2, column=1, padx=(0,90), pady=(30,), sticky=NE)

    def submit(self):
        fn = self.varFName.get()
        ln = self.varLName.get()
        self.lblDisplay.config(text='Hello {} {}!'.format(fn,ln))

    def cancel(self):
        self.master.destroy() # closes the window
        
# Controls the flow of operations
if __name__ == "__main__":
    # passing the class object into a variable which we can use
    root = Tk() # calls the tkinter class from the tkinter module
    App = ParentWindow(root)
    # this keeps the window open
    root.mainloop
    
