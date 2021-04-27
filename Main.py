from tkinter import *
from tkinter.ttk import *

class Mainwindow:
    def __init__(self):
        self.root = Tk()

        hej = Label(self.root, text="Hej")
        hej.pack



        mainloop()

if __name__ =='__main__':
    main = Mainwindow()