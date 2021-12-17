# Nice or Mean game as part of my python course in my software developer bootcamp

def start(nice=0, mean=0, name=""):
    #get user's name
    name= describe_game(name)
    nice,mean,name= nice_mean(nice,mean,name)

def describe_game(name):
    """
    check if this is a new game or not and if it is a new user or not.
    """
    if name != "":
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop= True
        while stop:
            if name == "":
                name= input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted \nby several different people. \nYou can chose to be nice or mean,")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop= False
    return name

def nice_mean(nice,mean,name):
    stop=True
    while stop:
        show_score(nice,mean,name)
        pick= input("\nA stranger approaches you for a \nconveration. Will you be nice \nor mean? (N/M) \n>>>: ")
        if pick =="N":
            print("\nthe stranger walks away smiling...\nThank you for being kind!")
            nice=(nice +1)
            stop= False
        if pick== "M":
            print("\nthe stranger glares at you \nmenacingly and storms off...\nMaybe rethink your actions..")
            mean= (mean+1)
            stop=  False
    score(nice,mean,name) #pass the 3 variables to the score()


def show_score(nice,mean,name):
    print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name, nice, mean))

def score(nice,mean,name):
    if nice >2:
        win(nice,mean,name)
    if mean >2:
        lose(nice, mean,name)
    else:
        nice_mean(nice,mean,name)

def win(nice,mean,name):
    print("\nNice job {}, you win! \nEveryone loves you! \nKindness goes a LONG way :)".format(name))
    again(nice,mean,name)

def lose(nice,mean,name):
    print("\nAhhhh too bad, game over! \n{}, you were not nice enough! \nConsider being kinder next time".format(name))
    again(nice,mean,name)

def again(nice,mean,name):
    stop= True
    while stop:
        choice=input("\nDo you want to play again? (y/n): \n>>> ")
        if choice == "y":
            stop=False
            reset(nice,mean,name)
        if choice =="n":
            print("\nOh, so sad, sorry to see you go!")
            stop=False
            quit()
        else:
            print("Enter (Y) for 'YES', (N) for 'NO': \n>>> ")


def reset(nice,mean,name):
    nice=0
    mean=0
    start(nice,mean,name)



if __name__== "__main__":
    start()
