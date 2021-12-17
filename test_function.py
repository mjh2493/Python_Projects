
mySentence= 'loves the color'

color_list= ['red', 'blue', 'green', 'pink', 'teal', 'black']

def color_function(name):
    for i in color_list:
        print("{0} {1} {2}".format(name, mySentence, i))


color_function('Mallory')
