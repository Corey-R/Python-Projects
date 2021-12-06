

import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd

import Fun_Challenge


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(300, 150)
        self.master.maxsize(600, 150)
        self.master.title('Check files')

        # creating the Buttons and positioning them
        self.btn_Browse1 = Button(self.master, text='Browse...', width=12, command=lambda: Fun_Challenge.open(self))
        self.btn_Browse1.grid(row=0, column=0, padx=(27, 0), pady=(10,0), sticky=W)
        self.btn_Browse2 = Button(self.master, text='Browse...', width=12)
        self.btn_Browse2.grid(row=1, column=0, padx=(27, 0), pady=(10,0), sticky=W)
        self.btn_Check = Button(self.master, text='Check for files...', height=2)
        self.btn_Check.grid(row=2, column=0, padx=(27, 0), pady=(10,0), sticky=W+S)
        self.btn_Close = Button(self.master, text='Close Program...', height=2)
        self.btn_Close.grid(row=2, column=2, padx=(27, 27), pady=(10,0), sticky=E+S)

        # creating the textboxes
        self.txt_Browse1 = Entry(self.master, text='', width=40)
        self.txt_Browse1.grid(row=0, column=1, columnspan=2, padx=(27,27), pady=(10,0), sticky=W)
        self.txt_Browse2 = Entry(self.master, text='', width=40)
        self.txt_Browse2.grid(row=1, column=1, columnspan=2, padx=(27,27), pady=(10,0), sticky=W)
        
        
        
        
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
