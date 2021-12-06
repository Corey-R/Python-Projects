

import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd

import GUI_Challenge

def open(self):
    var_Browse1 = self.txt_Browse1
    path = fd.askdirectory()
    print(path)
    var_Browse1.delete(0, END)
    var_Browse1.insert(0, path)
    
    
        
    


if __name__ == "__main__":
    pass
