import tkinter
from tkinter import *


class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master=master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Learning Tkinter!')
        self.master.config(bg='pink')

        self.varFName= StringVar()
        self.varLName= StringVar()

        self.lblFName=Label(self.master, text='First Name: ', font=("Arial", 16), fg='black', bg='pink')
        self.lblFName.grid(row=0, column=0, padx=(10, 0), pady=(10,10))

        self.lblLName=Label(self.master, text='Last Name: ', font=("Arial", 16), fg='black', bg='pink')
        self.lblLName.grid(row=1, column=0, padx=(10, 0), pady=(10,10))

        self.lblDisplay= Label(self.master, text='', font=("Arial", 16), fg='black', bg='pink')
        self.lblDisplay.grid(row=3, column=1, padx=(10, 0), pady=(10,10))

        self.txtFName= Entry(self.master, text=self.varFName, font=("Arial", 16), fg='black', bg='light blue')
        self.txtFName.grid(row=0, column=1, padx=(10, 0), pady=(10,10))

        self.txtLName= Entry(self.master, text=self.varLName, font=("Arial", 16), fg='black', bg='light blue')
        self.txtLName.grid(row=1, column=1, padx=(10, 0), pady=(10,10))

        self.btnSubmit= Button(self.master, text="SUBMIT", width=10, height=2, fg='white', bg='purple', command=self.submit)
        self.btnSubmit.grid(row=2, column=1, padx=(0, 0), pady=(30,0), sticky=NE)

        self.btnCancel= Button(self.master, text="CANCEL", width=10, height=2, fg='white', bg='purple', command=self.cancel)
        self.btnCancel.grid(row=2, column=1, padx=(0,90), pady=(30,0), sticky=NE)

    def submit(self):
        fn= self.varFName.get()
        ln= self.varLName.get()
        self.lblDisplay.config(text='Hello, {} {}!'.format(fn, ln))

    def cancel(self):
        self.master.destroy()



if __name__=="__main__":
    root= Tk()
    App= ParentWindow(root)
    root.mainloop()
