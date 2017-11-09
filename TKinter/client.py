import tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Alarmsysteem: Client")
root.wm_resizable(width=False, height=False)
root.geometry("400x400")

frame = Frame(root)
#tekst opgeslagen als variabelen om code sneller te kunnen bewerken en overzichtelijk te houden.
v1 = 'Turn alarm on.'
v2 = 'Turn alarm off.'

#functie checkt de text van de knop, en veranderd de text als op de knop gedrukt wordt
#in de praktijk zou er een 30 seconde timer moeten komen voordat het alarm afgaat
def alarmFunctie():
    textcheck = button.cget('text')
    if textcheck == v1:
        button.config(text = v2 , bg = 'Green')
    if textcheck == v2:
        button.config(text = v1 , bg = 'Red')


labelText = StringVar()
label = Label(frame, textvariable=labelText)
button = Button(frame,text = v1, bg = 'Red', command= alarmFunctie)


labelText.set("Welkom in het hoofdmenu, gebruiker.")

label.pack()
button.pack()
button.config(height = 100, width = 100)
frame.pack()



root.mainloop()