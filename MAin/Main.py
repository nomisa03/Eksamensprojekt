from tkinter import *
from tkinter.ttk import *
from Astar import Spot

class Mainwindow:
    def __init__(self):
        self.root = Tk()

        hej = Label(self.root, text="Hej")
        hej.pack

        astar = Button(self.root, Text="Astar", command = lambda: Spot(self))
        astar.pack


        mainloop()

if __name__ =='__main__':
    main = Mainwindow()