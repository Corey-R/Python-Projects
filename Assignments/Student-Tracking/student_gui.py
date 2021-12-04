

# importing tkinter module with all widgets
import tkinter as tk
from tkinter import *
from tkinter import messagebox

# importing corresponding modules
import student_main
import student_func

# creating the labels, textboxes, and buttons
# keep naming conventions in mind because it must match

def load_gui(self):

        # tk.Label() creates the label
        self.lab_fname = tk.Label(self.master, text="First Name: ")
        self.lab_fname.grid(row=0, column=0, padx=(30,0), pady=(20,0), sticky=N+W)
        self.lab_lname = tk.Label(self.master, text="Last Name: ")
        self.lab_lname.grid(row=0, column=3, padx=(30,0), pady=(20,0), sticky=N+W)
        self.lab_phone = tk.Label(self.master, text="Phone Number: ")
        self.lab_phone.grid(row=1, column=0, padx=(30,0), pady=(20,0), sticky=N+W)
        self.lab_email = tk.Label(self.master, text="Email Address: ")
        self.lab_email.grid(row=1, column=3, padx=(30,0), pady=(20,0), sticky=N+W)
        self.lab_course = tk.Label(self.master, text="Course Name: ")
        self.lab_course.grid(row=2, column=1, padx=(30,0), pady=(20,0), sticky=N+W)
        self.lab_student = tk.Label(self.master, text="Current Students: ")
        self.lab_student.grid(row=5, column=0, padx=(30,0), pady=(10,0), sticky=N+W)

        # tk.Entry() creates the textbox
        self.tex_fname = tk.Entry(self.master, text='')
        self.tex_fname.grid(row=0, column=1, columnspan=2, padx=(12,0), pady=(20,0), sticky=N+W)
        self.tex_lname = tk.Entry(self.master, text='')
        self.tex_lname.grid(row=0, column=4, columnspan=2, padx=(12,0), pady=(20,0), sticky=N+W)
        self.tex_phone = tk.Entry(self.master, text='')
        self.tex_phone.grid(row=1, column=1, columnspan=2, padx=(12,0), pady=(20,0), sticky=N+W)
        self.tex_email = tk.Entry(self.master, text='')
        self.tex_email.grid(row=1, column=4, columnspan=2, padx=(12,0), pady=(20,0), sticky=N+W)
        self.tex_course = tk.Entry(self.master, text='')
        self.tex_course.grid(row=2, column=3, columnspan=2, padx=(12,0), pady=(20,0), sticky=N+W)

        # creating listbox and scrollbar
        self.scrollbar = Scrollbar(self.master, orient=VERTICAL)
        self.listbox = Listbox(self.master, exportselection=0, yscrollcommand=self.scrollbar.set)
        self.listbox.bind('<<ListboxSelect>>',lambda event: student_func.onSelect(self,event))
        self.scrollbar.config(command=self.listbox.yview)
        self.scrollbar.grid(row=6, column=6, rowspan=7, padx=(0,0), pady=(10,0), sticky=N+S+W)
        self.listbox.grid(row=6, column=0, rowspan=7, columnspan=6, padx=(30,0), pady=(10,0), sticky=N+E+W+S)

        # creating the buttons
        self.btn_submit = tk.Button(self.master,width=16,height=1,text="Submit", bg="green", fg="white", command=lambda: student_func.submit(self))
        self.btn_submit.grid(row=3, column=7, padx=(30,0), pady=(30,0), sticky=E+S)
        self.btn_delete = tk.Button(self.master,width=16,height=1,text="Delete", bg="darkred", fg="white", command=lambda: student_func.delete(self))
        self.btn_delete.grid(row=6, column=7, padx=(30,0), pady=(30,0), sticky=E+S)

        student_func.create_db(self)
        student_func.onRefresh(self)


if __name__ == "__main__":
    pass

                              
    
