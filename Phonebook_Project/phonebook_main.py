# Phonebook demo

from tkinter import *
from tkinter import messagebox
import tkinter as tk

#import other modules
import phonebook_gui
import phonebook_func

#Frame is the tkinter frame class that our own class will inherit
class ParentWindow(Frame):
    def __init__ (self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #define our master frame config
        self.master=master
        self.master.minsize(500,300)
        self.master.maxsize(500,300)
        #this centers app on user screen
        phonebook_func.center_window(self,500,300)
        self.master.title("The Tkinter Phonebook Demo")
        self.master.configure(bg="#f0f0f0")
        #this catches if the user clicks the x in the upper window
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg= self.master

        #load in the GUI widgets from separate module, keeping code clean
        phonebook_gui.load_gui(self)


if __name__=="__main__":
    root= tk.Tk()
    App=ParentWindow(root)
    root.mainloop()
