
import shutil

import os

import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd

import datetime
from datetime import *

import File_Transfer

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(400, 200)
        self.master.maxsize(600, 250)
        self.master.title('File Transfer')

        # labels for buttons and textboxes
        self.lbl_from = Label(self.master, text='Check from')
        self.lbl_from.grid(row=0, column=0, padx=(27,0), pady=(30,0), sticky=W)
        self.lbl_to = Label(self.master, text='Transfer to')
        self.lbl_to.grid(row=2, column=0, padx=(27,0), pady=(30,0), sticky=W)

        # Browse and Transfer Buttons
        self.btn_from = Button(self.master, text='Browse...', width=12, height=1, command=lambda: File_Transfer.dir1(self))
        self.btn_from.grid(row=1, column=0, padx=(27,0), pady=(10,0), sticky=W)
        self.btn_to = Button(self.master, text='Browse...', width=12, height=1, command=lambda: File_Transfer.dir2(self))
        self.btn_to.grid(row=3, column=0, padx=(27,0), pady=(10,0), sticky=W)
        self.btn_transfer = Button(self.master, text='Transfer', width=15, height=2, command=lambda: File_Transfer.transfer(self))
        self.btn_transfer.grid(row=4, column=2, padx=(0,0), pady=(20,20), sticky=E+S)

        # Text fileds for corresponding browse buttons
        self.txt_from = Entry(self.master, text='', width=35)
        self.txt_from.grid(row=1, column=1, columnspan=2, padx=(27,0), pady=(10,0), sticky=W)
        self.txt_to = Entry(self.master, text='', width=35)
        self.txt_to.grid(row=3, column=1, columnspan=2, padx=(27,0), pady=(10,0), sticky=W)
        
        
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
