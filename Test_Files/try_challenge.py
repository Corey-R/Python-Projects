

def getRaw():
    num1 = input("\nPlease enter a number: ")
    num2 = input("\nPlease enter another number: ")
    return num1,num2

def multiply():
    go = True
    while go:
        num1,num2 = getRaw()
        try:
            num3 = int(num1) * int(num2)
            go = False
        except ValueError as e:
            print("{}: \n\nYou entered info that was not a number!".format(e))
        finally:
            print("\n\nThe program has finished...")
    print("\nHere's what we calculated: \n{} x {} = {}".format(num1,num2,num3))

if __name__ == "__main__":
    multiply()
