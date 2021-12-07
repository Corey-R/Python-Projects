

import shutil
import os
import datetime
from datetime import *
from tkinter import filedialog as fd
from tkinter import messagebox


import File_Transfer_GUI

def dir1(self):
    from_path = fd.askdirectory()

    self.txt_from.delete(0)
    self.txt_from.insert(0, from_path)    
    

def dir2(self):
    to_path = fd.askdirectory()

    self.txt_to.delete(0)
    self.txt_to.insert(0, to_path)
    

def transfer(self):
    source = self.txt_from.get()
    destination = self.txt_to.get()
    if (len(source) < 1) and (len(destination) < 1):
        messagebox.showerror("Missing Directory", "At least one of the directories are missing. \nPlease provide a directory for both fields.")
    else:    
        files = os.listdir(source)

        last_24 = datetime.now() - timedelta(hours=24)


        for i in files:
            filePath = os.path.join(source + '/' + i) # combines file to directory
            st = os.stat(filePath) # gets status of file
            mtime = datetime.fromtimestamp(st.st_mtime) # gets last modified or created time of file            
            if mtime > last_24: # if timestamp of file was within last 24 hours
                # we are saying move the files represented by 'i' to their new destination 
                shutil.move(filePath, destination)
                messagebox.showinfo("Transfer Complete", "You have successfully transferred files from the last 24 hours!")

        


if __name__ == "__main__":
    pass
