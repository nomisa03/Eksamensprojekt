from tkinter import *
from tkinter.ttk import *

class Fibonaci(Frame):
    def __init__(self, master):
        self.master = master
        
        self.Fibonaccisekvens = Toplevel(self.master.root)
        
        self.Fibonaccisekvens.title("List Window")
        
        self.Fibonaccisekvens.geometry("800x200")
        
        Inputfelt = Entry(self.Fibonaccisekvens)
        Inputfelt.insert(text="skriv et positivt heltal, der er større end 1")
        Inputfelt.Fibonaccisekvens.pack(padx = 20, pady = 0, side=LEFT)
     

    def Fibonaccisek(n):
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
