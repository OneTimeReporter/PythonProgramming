import tkinter
from tkinter import *
from tkinter import ttk
import time

root = Tk()
root.title("Alarmsysteem: Server")
root.wm_resizable(width=False, height=False) #zorgt ervoor dat de schermdimensies niet veranderbaar zijn
root.geometry("400x400") #schermdimensies

frame = Frame(root)


alarmstatus = False    #deze variable zou moeten veranderen naar True als het alarm afgaat bij de client

#Deze functie zorgt voor het knipperlicht, als variable alarmstatus True is
def alarmFunctie():
    if alarmstatus == True:
        current_color = alarm.cget("background")
        next_color = "green" if current_color == "red" else "red"
        alarm.config(background=next_color, text= 'ALARM ALARM, ALARM')
        root.after(100, alarmFunctie)




labelText = StringVar()

label = Label(frame, textvariable=labelText)
alarm = Label(frame,text = 'Geen alarm gaat af op het moment') #default scherm as het alarm niet af gaat, zet alarmstatus = False om te testen
simulatieButton = Button(frame, text ='Simulatie', command = alarmFunctie())


labelText.set("Welkom in het hoofdmenu, admin.")
label.pack()
alarm.pack()
alarm.config(height = 100, width = 100)
frame.pack()


root.mainloop()