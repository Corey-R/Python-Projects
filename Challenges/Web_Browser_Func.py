
# Import the webbrowser module 
import webbrowser

# import any supporting modules
import tkinter as tk
from tkinter import *

import Web_Browser_GUI


# defining a method that creates the HTML file
def Create_HTML(self):
    var_body = self.txt_body.get()
    # 'x' creates new file and sends error if exists
    # 'a' would have continued appending the f.write statement
    # 'w' would have overridden any changes made
    f = open("Basic_File.html", "w")
    # this adds the html content to the file
    f.write('<!DOCTYPE html> \n<html lang="en"> \n\t<body> \n\t\t<h1> \n\t\t\t{} \n\t\t</h1> \n\t</body> \n</html>'.format(var_body))
    f.close()
    

    # Once the file is made, use webbrowser module to open
    # file in a new tab of the user's default browser
    # Since the file was created, it's automatically stored in the CWD
    url = "Basic_File.html"
    webbrowser.open(url, new=2) #<-- new=2 opens in new tab if possible
    


if __name__ == "__main__":
    pass
