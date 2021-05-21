from tkinter import *
from tkinter.ttk import *

class Fibonaci(Frame):
    def __init__(self, master):
        self.master = master

        self.Fibonaccisekvens = Toplevel(self.master.root)

        self.Fibonaccisekvens.title("Fibonaci")

        self.Fibonaccisekvens.geometry("800x200")

        self.Fibonaccisek()


    def Fibonaccisek(self):
        n = Entry(self.Fibonaccisekvens)
        n.pack(padx=20,pady=0,side=LEFT)

        Knap = Button(self.Fibonaccisekvens,text="Brug Fibonaci metoden",command=self.Fibonacimetode)
        Knap.pack(padx=20,pady=0,side=RIGHT)

        return n

    def Fibonacimetode(self,n):
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
            yy = Label(self.Fibonaccisekvens,text=y)
            yy.pack(padx=30,pady=0,side=BOTTOM)
        else:
            xx = Label(self.Fibonaccisekvens,text=x)
            xx.pack(padx=30,pady=0,side=BOTTOM)
