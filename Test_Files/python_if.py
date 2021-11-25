


num1 = 12
key = False

# NOTE: Using one equal sign stores value into a variable
# So, when making a compairson, use two equal signs "==" instead.

if num1 == 12:
    if key:
        print("Num1 is equal to Twelve and they have the key!")
    else:
         print("Num1 is equal to Twelve and they DO NOT have the key!")
elif num1 < 12:
     print("Num1 is less than Twelve!")
else:
    print("Num1 is NOT equal to Twelve!") 

# My Own Conditional Statement

monja = 'Name'
x = 6

if monja == 'Goku':
    print("Goku's the name!")
elif monja == 'Name':
    if x > 10:
        print('Hi! My name\'s Corey and it\'s a pleasure to meet ya!')
    else:
        print('Goku here, thought I\'d stop by to say hello!')
else:
    print('Sorry, I can\'t remember my name...')
          
# Boolean Challenge

x = 19

if x < 20:
    print('X didn\'t make the cut')
else:
    print('X made the cut')

print(bool('Monja'))
print(bool(33))
print(isinstance(x, bool))
