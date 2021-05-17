from tkinter import *
from tkinter.ttk import *

class Fibonaci:
    def __init__(self, master):
        self.master = master
        
        self.Primtal = Toplevel(self.master.root)
        
        self.Primtal.title("List Window")
        
        self.Primtal.geometry("800x200")

    n = int(input("Skriv antal sekvenser: "))
    x=0
    y=1
    i=2
    while i < n:
        if (i % 2) == 0:
            x=x+y
            i=i+1
        else:
            y=x+y
            i=i+1
    if (i % 2) == 0:
        print(y)
    else:
        print(x)
