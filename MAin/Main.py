from tkinter import *
from tkinter.ttk import *
from Astar import main

class Mainwindow:
    def __init__(self):
        self.root = Tk()

        hej = Label(self.root, text="Hej")
        hej.pack

        Astar = Button(self.root, Text="Astar", COMMAND=lambda: main(self))
        Astar.pack


        mainloop()

if __name__ =='__main__':
    main = Mainwindow()