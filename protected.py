#defining the Protected class
class Protected:
    def __init__(self):
        self._protectedVar=0

#calling the class and printing a protected string
test= Protected()
test._protectedVar= 'This is protected'
print(test._protectedVar)

#defining the private class
class Private_test():
    def __init__(self):
        self.__privateVar='This is private.'

    def getPrivate(self):
        print(self.__privateVar)

    #this allows for someone to change the private var
    def setPrivate(self, private):
        self.__privateVar=private

#calling the first and changed private strings
test2= Private_test()
test2.getPrivate()
test2.setPrivate('This changes the string.')
test2.getPrivate()

