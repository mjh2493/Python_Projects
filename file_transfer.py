import shutil
import os
import datetime
import timedelta
import time
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
import tkinter as tk

class ParentWindow(Frame):
    def __init__ (self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #define our master frame config
        self.master=master
        self.master.minsize(500,300)
        self.master.maxsize(500,300)
        self.master.title("Select your Folders")
        self.master.configure(bg="light grey")
        #this catches if the user clicks the x in the upper window
        self.master.protocol("WM_DELETE_WINDOW", lambda: ask_quit(self))
        arg= self.master

        load_gui(self)

#quits box if x is pressed
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        self.master.destroy()

        

def button_source(self):
    global source_folder
    source_folder=filedialog.askdirectory()+"/"
    print(source_folder)
##    filename= filedialog.askdirectory()
##    source_folder.set(filename)
##    print(filename)

def button_dest(self):
    global dest_folder
    dest_folder=filedialog.askdirectory()+"/"
    print(dest_folder)
##    filename= filedialog.askdirectory()
##    dest_folder.set(filename)
##    print(filename)


def find_files_time():
    modTime= datetime.datetime.now() - datetime.timedelta(hours=24)
    files=os.listdir(source_folder)
    for i in files:
        fullpath= source_folder+i
        mtime= os.path.getmtime(fullpath)
        date_time=datetime.datetime.fromtimestamp(mtime)
        print(date_time)
        if date_time > modTime:
            shutil.move(source_folder+i, dest_folder)

#builds out the GUI
def load_gui(self):
    dest_folder= StringVar()
    source_folder= StringVar()
    self.lbl_sourcefolder=tk.Label(self.master, text='Click the button below to \nselect the folder you want to \nplace and modify your files in.')
    self.lbl_sourcefolder.grid(row=0, column=0, padx=(27,0), pady=(10,0))
    self.lbl_destfolder=tk.Label(self.master, text='Click the button below to \nselect the folder you want to \nplace to modified folders in to \ntransfer to the home base computer.')
    self.lbl_destfolder.grid(row=0, column=1, padx=(27,0), pady=(10,0))

    self.btn_source= tk.Button(self.master, width=20, height=2, text='Add Source Folder', command= lambda: button_source(self))
    self.btn_source.grid(row=2, column=0, padx=(25,0), pady=(45,10))
    self.btn_dest= tk.Button(self.master, width=20, height=2, text='Add Destination Folder', command=lambda: button_dest(self))
    self.btn_dest.grid(row=2, column=1, padx=(25,0), pady=(45,10))

    self.btn_start= tk.Button(self.master, width=20, height=2, text='Start the Process!', command=find_files_time)
    self.btn_start.grid(row=4, column=1, padx=(25,0), pady=(45,10))


if __name__=="__main__":
    root=tk.Tk()
    App=ParentWindow(root)
    root.mainloop()
