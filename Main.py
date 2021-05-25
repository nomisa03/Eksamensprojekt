#Imortere vores Tkinter som er den pakke vi bruger
from tkinter import *
from tkinter.ttk import *

#Importer de andre windows
from Primtal import primtalmenu
from Fibonaccisekvens import Fibonaci

#Laver vores klasse hvor der kommer en funktion ind i.
#Den funktion starter så vores canvas op med argumentet self
class Mainwindow:
    def __init__(self):
        #Laver såden at når vi skriver "self.root" så ved den det er tkinter den skal have fat i.
        self.root = Tk()
        #sætter vores vindue størresel til 260x150
        self.root.geometry("260x150")
        #Laver et label som er en tekstbox vi kan skrive i
        hej = Label(self.root, text="Velkommen til vores algoritme GUI \nHer kan du vælge imellem de to algoritmer: \ngod fornøjelse:)")
        #Så "packer" vi den så vi placere den her i toppen af canvas
        hej.pack(padx = 20, pady = 0, side=TOP)
        #her bliver der lavet en knap. Også når man trykker på den så åber den det næste vindue
        #Med til det nye vindue kommer self med for at sige du har styring nu.
        Prime = Button(self.root, text="Primtal", command = lambda:primtalmenu(self))
        Prime.pack(padx = 20, pady = 0, side=LEFT)

        fibonaci = Button(self.root, text="Fibonacci", command = lambda:Fibonaci(self))
        fibonaci.pack(padx = 20, pady = 0, side=LEFT)



        #venter på input fra bruger
        mainloop()
#tjekker at den for fat på Tkinter og ikke en anden udvidesel
if __name__ =='__main__':
    main = Mainwindow()
