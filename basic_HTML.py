import webbrowser
from tkinter import *
from tkinter import messagebox
import tkinter as tk

class ParentWindow(Frame):
    def __init__ (self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #define our master frame config
        self.master=master
        self.master.minsize(500,300)
        self.master.maxsize(500,300)
        self.master.title("Add Your Text to our Website")
        self.master.configure(bg="pink")
        #this catches if the user clicks the x in the upper window
        self.master.protocol("WM_DELETE_WINDOW", lambda: ask_quit(self))
        arg= self.master

        load_gui(self)

#created website
def create():
    f=open("basic_website.html", "x")
    f.close()

#reads website
def read():
    f=open("basic_website.html", "r")
    print(f.read())

#opens website when view website button is clicked
def open_website():
    webbrowser.open_new_tab("basic_website.html")

#quits box if x is pressed
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        self.master.destroy()

#adds body text inputted by user
def add(self):
    f=open("basic_website.html", "a")
    source=self.text_entry.get()
    message=("<p>{}</p>".format(source))
    f.write(message)
    f.close()

#builds out the GUI
def load_gui(self):
    self.lbl_text=tk.Label(self.master, text='Insert your custom text here: ')
    self.lbl_text.grid(row=0, column=0, padx=(27,0), pady=(10,0), sticky=N+W)

    self.text_entry=tk.Entry(self.master, text='')
    self.text_entry.grid(row=0, column=1, rowspan=3, columnspan=5, padx=(30,40), pady=(0,0), sticky=N+E+W)

    self.btn_add= tk.Button(self.master, width=12, height=2, text='Add', command= lambda: add(self))
    self.btn_add.grid(row=4, column=0, padx=(25,0), pady=(45,10), sticky=W)

    self.btn_view= tk.Button(self.master, width=20, height=2, text='View Website', command=open_website)
    self.btn_view.grid(row=4, column=1, padx=(25,0), pady=(45,10), sticky=W)


if __name__=="__main__":
    root=tk.Tk()
    App=ParentWindow(root)
    root.mainloop()
