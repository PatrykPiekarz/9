#konwertuje z jednego systemu liczbowego na drugi (dwojkowy,osemkowy,dziesietny)

'''

from Tkinter import *
root=Tk()
root.title(u"Wykszta\u0142cenie")

var=IntVar()

for text, value in [('dziesietyn na dwojkowy',1),('dziesietny na osemkowy',2)]:
    Radiobutton(root,text=text,value=value,variable=var).pack(anchor=W)


var.set(3)
root.geometry("250x150")
root.mainloop()
print var.get()

'''

from Tkinter import *
from tkMessageBox import *

class EntryDemo (Frame):


    def __init__(self):
        Frame.__init__(self)
        self.pack(expand=YES,fill=BOTH)
        self.master.title("Testowanie pol tekstowych")
        self.master.geometry("325x100")

        self.frame1=Frame(self)
        self.frame1.pack(pady=5)

        self.text1=Entry(self.frame1,name="tekst 1")
        self.text1.bind("<Return>",self.showContents)
        self.text1.pack(side=LEFT,padx=5)
        self.var=IntVar()
        for text, value in [('dziesietyn na dwojkowy',1),('dziesietny na osemkowy',2)]:
            Radiobutton(self,text=text,value=value,variable=self.var).pack(anchor=W)
        self.var.set(1)
    def showContents(self,event):
        """Wyswietl zawartosc pola"""
        #wyswietl nazwe pola tekstowego generujacego zdarzenie
        theName=event.widget.winfo_name()
        #podstaw zawartosc tego pola do zmiennej theContents
        theContents=event.widget.get()
        #Po wypelnieniu pola tekstowego i wcisniecia Enter
        #Zawartosc tego pola znajduje sie w theContents
        #a tu dla celow szkoleniowych drukujemy je w osobnym
        #oknie modulu messagebox
        if self.var.get()==1:
            conv=int(theContents)
            conv=self.dbin(conv)
            showinfo("dziesietny na dwojkowy",conv)
        else:
            conv=int(theContents)
            conv=self.doct(conv)
            showinfo("dziesietyn na osemkowy",conv)
    def dbin(self,x):
        return int(bin(x)[2:])
    def doct(self,x):
        return int(oct(x)[1:])
def main():
    EntryDemo().mainloop()
if __name__=="__main__":
    main()
