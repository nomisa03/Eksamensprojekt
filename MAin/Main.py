from tkinter import *
from tkinter.ttk import *

#Importer de andre windows
from Primtal import primtalmenu
from Fibonaccisekvens import Fibonaci

class Mainwindow:
    def __init__(self):
        self.root = Tk()
        
        self.root.geometry("400x150")

        hej = Label(self.root, text="Hej")
        hej.pack(padx = 20, pady = 0, side=TOP)
        
        Prime = Button(self.root, text="primtals menu", command = lambda:primtalmenu(self))
        Prime.pack(padx = 20, pady = 0, side=LEFT)




        mainloop()

if __name__ =='__main__':
    main = Mainwindow()