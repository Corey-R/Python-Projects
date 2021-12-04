
# import tkinter and all associated widgets
import tkinter as tk
from tkinter import *
from tkinter import messagebox

# import any other modules necessary
import student_func
import student_gui

# define the ParentWindow(Frame) class which contains the tkinter
# master class for creating the window.

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # configure master window
        self.master = master
        self.master.minsize(700,400) # (height, width) in pixels
        self.master.maxsize(700,400) # limiting the size of the window
        student_func.center_window(self, 700, 400) # centers app on user's screen
        self.master.title("Student Tracker")
        self.master.configure(bg="lightgray")
        # tkinter method that catches if user clicks the "X" button in upper right corner
        self.master.protocol("WM_DELETE_WINDOW", lambda: student_func.ask_quit(self))

        student_gui.load_gui(self)


if __name__ == "__main__":
    # syntax needed to create the window
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop() # <-- used to keep the window open

    
