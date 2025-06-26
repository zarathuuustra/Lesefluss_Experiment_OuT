from tkinter import *

fenster = Tk()
fenster.title("Experiment TEXT UND KOHAERENZ")
fenster.geometry('1000x750')
INFO_LIST = []

# Spalten gleichmäßig verteilen (von 0 bis 5 z. B.)
for i in range(6):
    fenster.grid_columnconfigure(i, weight=1)

def clicked():
    res = f"Vielen Dank {txt.get()}!"
    ergebnis_label.configure(text=res)

def clicked_1():
    text_1 = "Okay, du bist Gruppe 1!"
    button_1.configure(text=text_1)
    INFO_LIST.append("GRUPPE1")
    # print(interessante_liste)
    button_2.grid_forget()

def clicked_2():
    text_2 = "Okay, du bist Gruppe 2!"
    button_2.configure(text=text_2)

# Hinweis: Alle zentral in Spalte 2 oder 3 setzen
info_label = Label(fenster, text="Hallo! Willkommen zum Experiment! \n"
                                 "Hier wirst du Comic-Bilder in einer bestimmten Reihenfolge sehen und interpretieren.")
info_label.grid(column=2, row=0, pady=10)

# Informationsgruppe 1
info_label_2 = Label(fenster, text="Bitte trage deine Namen ein.")
info_label_2.grid(column=1, row=1)
txt = Entry(fenster, width=20)
txt.grid(column=1, row=2)
btn = Button(fenster, text="Bestätigen!", fg="red", command=clicked)
btn.grid(column=1, row=3, pady=5)
ergebnis_label = Label(fenster, text="Hier steht später dein Name...")
ergebnis_label.grid(column=1, row=4, pady=10)

#Infoabfrage
info_label_abfrage = Label(fenster, text="Wenn du Name und Gruppe eingetragen hast kann das Experiment beginnen.\n"
                                   "Bist du bereit?")
info_label_abfrage.grid(column=2, row=1)

# Informationsgruppe 2
info_label_2 = Label(fenster, text="Und sag uns bitte in welcher Gruppe du bist.")
info_label_2.grid(column=3, row=1)
button_1 = Button(fenster, text="Gruppe 1", command=clicked_1)
button_1.grid(column=3, row=2, pady=5)
button_2 = Button(fenster, text="Gruppe 2", command=clicked_2)
button_2.grid(column=3, row=3, pady=5)

exit_button = Button(fenster, text="Beenden", command=fenster.quit)
exit_button.grid(column=2, row=7, pady=10)

fenster.mainloop()