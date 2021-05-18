from tkinter import *
from tkinter.ttk import *

#Primtal: er et tal, der kun kan deles med sig selv og med 1 - altså 1 og tallet selv er divisorer, så der ikke er nogen rest

class primtalmenu(Frame):
    def __init__(self, master):
        self.master = master
        
        self.Primtal = Toplevel(self.master.root)
        
        self.Primtal.title("List Window")
        
        self.Primtal.geometry("800x200")
        
        Inputfelt = Entry(self.Primtal)
        Inputfelt.insert(text="skriv et positivt heltal, der er større end 1")
        Inputfelt.Primtal.pack(padx = 20, pady = 0, side=LEFT)
        
        n = Inputfelt.get()
        
        if n > 1:
            for i in range(2, n):                   #for loopet kører alle tallene fra 2 til det valgte tal igennem, for at tjekke om det kan divideres med andet end 1 og selve tallet uden rester
                if (n % i) == 0:                    #her tjekkes om der er rest på de forskellige tal
                    print(str(n) + " er ikke et primtal, da det kan divideres med " + str(i) + " og ikke have en rest.")    #her bliver printet, hvis det ikke er et primtal, hvor der så bliver forklaret hvorfor
                    Inputfelt.delete("1.0, END")
                    Inputfelt.insert(text=str(n) + " er ikke et primtal, da det kan divideres med " + str(i) + " og ikke have en rest.")
                    return False
            else:
                print(str(n) + " er et primtal.")
                Inputfelt.delete("1.0, END")
                Inputfelt.insert(text=str(n) + " er et primtal.")           #her bliver printet, hvis det er et primtal
                return True
        else:
            Inputfelt.delete("1.0, END")
            Inputfelt.insert(text="jeg skrev over 1 din klunk. Kan du ikke tælle, eller kan du ikke læse?")    #dette bliver printet, hvis inputet ikke er et positivt heltal
    
        
        
