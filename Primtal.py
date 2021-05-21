from tkinter import *
from tkinter.ttk import *

#Primtal: er et tal, der kun kan deles med sig selv og med 1 - altså 1 og tallet selv er divisorer, så der ikke er nogen rest

class primtalmenu(Frame):
    def __init__(self, master,):
        self.master = master

        self.Tal = Toplevel(self.master.root)

        self.Tal.title("List Window")

        self.Tal.geometry("300x150")

        self.Create_gadets()

    def Create_gadets(self):

        Inputlabel = Label(self.Tal, text="Skriv et tal der er større end 1")
        Inputlabel.pack(padx = 20, pady = 0, side=TOP)

        Inputfelt = Entry(self.Tal)
        Inputfelt.pack(padx = 20, pady = 0, side=LEFT)

        Regn = Button(self.Tal, text="Test det", command=self.Regner)
        Regn.pack(padx=40,pady=40,side=BOTTOM)

        global n

        n = int(Inputfelt.get())

    def Regner(self, n):
        if n > 1:
            for i in range(2, n):                   #for loopet kører alle tallene fra 2 til det valgte tal igennem, for at tjekke om det kan divideres med andet end 1 og selve tallet uden rester
                if (n % i) == 0:                    #her tjekkes om der er rest på de forskellige tal
                    print(str(n) + " er ikke et primtal, da det kan divideres med " + str(i) + " og ikke have en rest.")    #her bliver printet, hvis det ikke er et primtal, hvor der så bliver forklaret hvorfor
                    Ikke = Label(self.Tal, text=str(n) + " er ikke et primtal, da det kan divideres med " + str(i) + " og ikke have en rest.")
                    Ikke.pack(padx=20,pady=0,side=RIGHT)
                    return False
            else:
                print(str(n) + " er et primtal.")
                er = Label(self.Tal,text=str(n) + " er et primtal.")
                er.pack(padx=20,pady=0,side=RIGHT)     #her bliver printet, hvis det er et primtal
                return True
        else:
            Dinklunk=Label(self.Tal, text="jeg skrev over 1 din klunk. Kan du ikke tælle, eller kan du ikke læse?")    #dette bliver printet, hvis inputet ikke er et positivt heltal
            Dinklunk.pack(padx=20,pady=0,side=RIGHT)