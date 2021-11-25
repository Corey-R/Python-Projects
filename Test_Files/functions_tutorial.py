


mySentence = 'loves the color'

color_list = ['red', 'blue', 'green', 'yellow', 'pink', 'purple']

# syntax to create a function starts with 'def'

def color_function(name):
    lst = []
    for i in color_list:
        msg = '{0} {1} {2}'.format(name,mySentence, i)
        lst.append(msg)
    return lst

def get_name():
    go = True
    while go:
        name = input('What is your name')
        if name == '':
            print('You need to provide your name.')
        elif name == 'Sally':
            print('Sally huh!?, sorry Sally access denied!')
        else:
            go = False
    lst = color_function(name)
    for i in lst:
        print(i)



get_name()




