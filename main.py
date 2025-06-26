from tkinter import *


# Die folgende Funktion soll ausgeführt werden, wenn

# der Benutzer den Button anklickt

def button_action():

    anweisungs_label.config(text="Ich wurde geändert!")



# Ein Fenster erstellen

fenster = Tk()

fenster.title("Experiment TEXT UND KOHAERENZ") # Titel des Fensters
fenster.geometry('1000x750') # Wie groß das Fenster ist

# Label und Buttons erstellen.

change_button = Button(fenster, text="Ändern", command=button_action)
exit_button = Button(fenster, text="Beenden", command=fenster.quit)
# button widget with red color text inside


anweisungs_label = Label(fenster, text="Ich bin eine Anweisung:\nklicke auf 'Ändern'.")
info_label = Label(fenster, text="Ich bin eine Info:\n Der Beenden Button schliesst das Programm.")
ergebnis_label = Label(fenster, text="Du hast noch nichts geschrieben! Schreibe doch etwas")

txt = Entry(fenster, width=10)
# function to display user text when
# button is clicked
def clicked():
    res = "You wrote " + txt.get()
    ergebnis_label.configure(text = res)

btn = Button(fenster, text = "RESULT" ,fg = "red", command=clicked)
# Nun fügen wir die Komponenten unserem Fenster in der gewünschten Reihenfolge hinzu.
# Note: there are different geometry management tools: pack(), grid(), place(); grid could help keep them in plae

anweisungs_label.pack() # 1. Label anzeigen mit Text
change_button.pack() # 2. Button darunter hinzufügen. Er benutzt die Funktion: "Button Action"
info_label.pack() # 3. Label (wie in 1)
ergebnis_label.pack()
txt.pack()
btn.pack()
exit_button.pack() # 4. Button wieder hinzufügen. Er benutz die Funktion "Quit" --> Schließt das Fenster





# In der Ereignisschleife auf Eingabe des Benutzers warten.

fenster.mainloop()