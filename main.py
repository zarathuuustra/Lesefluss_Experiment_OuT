from tkinter import *
import os
from PIL import Image

# Bilderpfade
script_dir = os.path.dirname(__file__)
pic1_dir = os.path.join(script_dir, "BILDER_EXPERIMENT", "Bild_1.png")
pic2_dir = os.path.join(script_dir, "BILDER_EXPERIMENT", "Bild_2.png")
pic3_dir = os.path.join(script_dir, "BILDER_EXPERIMENT", "Bild_3.png")
pic4_dir = os.path.join(script_dir, "BILDER_EXPERIMENT", "Bild_4.png")
pic5_dir = os.path.join(script_dir, "BILDER_EXPERIMENT", "Bild_5.png")
pic6_dir = os.path.join(script_dir, "BILDER_EXPERIMENT", "Bild_6.png")

fenster = Tk()
fenster.title("Experiment TEXT UND KOHAERENZ")
fenster.geometry('1000x750')
user_info = {"Name": "", "Gruppe":0}
bilder_cache = {}
collected_data = {
    "Bild1": "",
    "Bild2": "",
    "Bild3": "",
    "Bild4": "",
    "Bild5": "",
    "Bild6": "",
}

# Spalten gleichmäßig verteilen (von 0 bis 5 z. B.)
for i in range(6):
    fenster.grid_columnconfigure(i, weight=1)

def clicked():
    res = i_txt.get()
    user_info["Name"] = res
    i_name_label.configure(text=f"Vielen Dank fürs Mitmachen {res}!")
    print(user_info)

def clicked_1():
    text_1 = "Okay, du bist Gruppe 1!"
    i_button_1.configure(text=text_1)
    user_info["Gruppe"] = 1
    i_button_2.grid_forget()
    print(user_info)

def clicked_2():
    text_2 = "Okay, du bist Gruppe 2!"
    i_button_2.configure(text=text_2)
    user_info["Gruppe"] = 2
    i_button_1.grid_forget()
    print(user_info)

def clicked_bereit():
    if user_info["Gruppe"] == 0:
        i_status_label.configure(text="Bitte trage deine Gruppe ein!")
    elif user_info["Name"] == "":
        i_status_label.configure(text="Bitte trage deinen Namen noch ein!")
    else:
        i_status_label.configure(text="Super, dann geht es jetzt los!")
        experiment()

# Informationen_ANFANG_SALVE
i_hallo_label = Label(fenster, text="Hallo! Willkommen zum Experiment! \n"
                                 "Hier wirst du Comic-Bilder in einer bestimmten Reihenfolge sehen und interpretieren.")
i_hallo_label.grid(column=1, row=0, pady=10)

# Informationen_ANFANG_NAME
i_name_label = Label(fenster, text="Bitte trage deine Namen ein.")
i_name_label.grid(column=1, row=1)
i_txt = Entry(fenster, width=20)
i_txt.grid(column=1, row=2)
i_btn = Button(fenster, text="Bestätigen!", fg="red", command=clicked)
i_btn.grid(column=1, row=3, pady=5)

# Informationen_ANFANG_GRUPPE
intro_gruppen_label = Label(fenster, text="Und sag uns bitte in welcher Gruppe du bist.")
intro_gruppen_label.grid(column=2, row=0)
i_button_1 = Button(fenster, text="Gruppe 1", command=clicked_1)
i_button_1.grid(column=2, row=1, pady=5)
i_button_2 = Button(fenster, text="Gruppe 2", command=clicked_2)
i_button_2.grid(column=2, row=2, pady=5)

# Informationen_ANFANG_START
i_status_label = Label(fenster, text="Wenn du Name und Gruppe eingegeben hast,\ndann drücke auf den Button 'BEREIT'.")
i_status_label.grid(column=2, row=4)
i_button_bereit = Button(fenster, text="BEREIT", command=clicked_bereit)
i_button_bereit.grid(column=2, row=5, pady=5)

# Die Option das Spiel zu beenden (wird immer angezeigt)
exit_label = Label(fenster, text="Wenn du das Experiment beenden möchtest,\ndann drücke auf den Knopf 'Beenden'.")
exit_label.grid(column=3, row=0)
exit_button = Button(fenster, text="Beenden", command=fenster.quit)
exit_button.grid(column=3, row=1, pady=10)

# Reihenfolge Standard: 1-6; Reihenfolge anders: 6-1

def experiment():
    """
    Wenn das Experiment startet, mache folgendes:
    1. Vergesse die vorherigen Buttons und Labels
    2. Zeige die neuen Buttons und Labels passend zur Gruppe an.
    :return:
    """
    i_hallo_label.grid_forget()
    i_name_label.grid_forget()
    i_txt.grid_forget()
    i_btn.grid_forget()
    intro_gruppen_label.grid_forget()
    i_button_1.grid_forget()
    i_button_2.grid_forget()
    i_status_label.grid_forget()
    i_button_bereit.grid_forget()
    if user_info["Gruppe"] == 1:
        gruppe1()
    else:
        pass

def gruppe1():
    print("Gruppe_1_Test")
    bilder_cache["bild1"] = PhotoImage(file=pic1_dir)
    bild_label = Label(fenster, image=bilder_cache["bild1"])
    bild_label.grid(column=2, row=1)

fenster.mainloop()