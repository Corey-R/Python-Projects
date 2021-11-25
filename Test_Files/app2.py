
"""
    NOTE: In order to import a module into your current file, you must ensure that
    both files are stored, or saved, in the same directory in memory.
"""
import app # Imports, or transfers, all of the content from app.py into this file


# Creating, or defining, another function

def print_app2():
    name = (__name__)
    return name


if __name__ == "__main__":  # __main__ is the script being ran using the run command
    # The following is calling code from within this script.
    print("I am running code from {}".format(print_app2()))

    # The following is calling code from the imported app.py.
    print("I am running code from {}".format(app.print_app()))

