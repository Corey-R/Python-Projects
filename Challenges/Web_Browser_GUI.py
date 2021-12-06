
# import sebbrowser and supporting modules
import webbrowser

import tkinter as tk
from tkinter import *

import Web_Browser_Func


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(200, 100)
        self.master.maxsize(500, 250)
        self.master.title('Create Webpage')

        # create a label for the corresponding textbox
        self.lbl_body = Label(self.master, text="Enter web content...")
        self.lbl_body.grid(row=0, column=0, padx=(30,0), pady=(20,0), sticky=W)

        # creating the corresponding textbox
        self.txt_body = Entry(self.master, text='', width=40)
        self.txt_body.grid(row=1, column=0, columnspan=2, padx=(30,30), pady=(10,0), sticky=W)

        # creating a button to create webpage and display in default browser
        self.btn_create = Button(self.master, text='Create Page', width=12, height=1, command=lambda: Web_Browser_Func.Create_HTML(self))
        self.btn_create.grid(row=2, column=1, padx=(0,30), pady=(20,20),sticky=E+S)

        
                           

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
