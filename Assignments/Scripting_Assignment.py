

"""
    Scripting assignment.
    For this assignment, you will need to write a script that will check a specific
    folder on the hard drive, verify whether those files end with a “.txt” file
    extension and, if they do, print those qualifying file names and their corresponding
    modified time-stamps to the console.
"""

# First, import os (if haven't already)
import os

# add 'import time' to be able to convert modified time to local time
import time


#I'm setting a variable that has the file path to the directory I want to iterate

Directory = 'C:\\A\\' # Keep in mind the escape characters

# Store in a variable a tuple containing the file extensions you want your program
# to print(); for the assignment, we want to print the '.txt' files

Ext = ('.txt',) # don't forget the comma even for single items or it won't be recognized as a tuple

# Now, we must create a for loop so the program can iterate through the enitre directory.
# We will use an if/else statement to print any files that match the '.txt' file extension.


for files in os.listdir(Directory): # os.listdir() is a method used to list all files within the targeted directory
    if files.endswith(Ext):
        # using path.join() method so the absolute path of the file can be displayed        
        match = os.path.join(Directory, files)
        stamp = os.path.getmtime(match)
        local = time.ctime(stamp)
        print(match + ' ' + str(local))                 
    else:
        continue

"""
     NOTE: We do not have to instruct the method to stop at any one point because we want it to
     iterate through the entire directory so it can print any files that match the file extension
     The above code would have fulfilled all requirements of the current assignment had we stopped
     at print(match + str(stamp)) but the time would have been in seconds since epoch. To improve
     user experience, we converted the modified time into the file's local time which can be easily
     read and understood.
"""

"""
    Also, in order to combine the above print statement, notice the str() method being used.
    This allows a data type, in this case (float), to be converted into a string.
    When using Python, you cannot add different data types together:
    print(match [string] + stamp [float]) so to prevent an error, we must convert:
    print(match [string] + str(stamp) [now a string])
"""
