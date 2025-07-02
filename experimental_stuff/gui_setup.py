from tkinter import Label, Button, Entry

def setup_gui(fenster, user_info, experiment_callback, nutzer_eingaben):
    def clicked():
        user_info["Name"] = entry.get()
        name_label.config(text=f"Willkommen, {user_info['Name']}!")

    def clicked_1():
        user_info["Gruppe"] = 1
        gruppe_label.config(text="Gruppe 1 gewählt")
        button_2.grid_forget()

    def clicked_2():
        user_info["Gruppe"] = 2
        gruppe_label.config(text="Gruppe 2 gewählt")
        button_1.grid_forget()

    def clicked_bereit():
        if not user_info["Name"] or user_info["Gruppe"] == 0:
            status_label.config(text="Bitte Name und Gruppe eingeben.")
        else:
            status_label.config(text="Starte Experiment...")
            experiment_callback(fenster, user_info, nutzer_eingaben)

    # GUI-Elemente
    name_label = Label(fenster, text="Bitte gib deinen Namen ein:")
    name_label.grid(row=0, column=1)
    entry = Entry(fenster)
    entry.grid(row=1, column=1)

    button_bestätigen = Button(fenster, text="Bestätigen", command=clicked)
    button_bestätigen.grid(row=2, column=1)

    gruppe_label = Label(fenster, text="Wähle deine Gruppe:")
    gruppe_label.grid(row=0, column=2)
    button_1 = Button(fenster, text="Gruppe 1", command=clicked_1)
    button_1.grid(row=1, column=2)
    button_2 = Button(fenster, text="Gruppe 2", command=clicked_2)
    button_2.grid(row=2, column=2)

    status_label = Label(fenster, text="Drücke 'BEREIT', wenn du bereit bist.")
    status_label.grid(row=3, column=1, columnspan=2)
    button_bereit = Button(fenster, text="BEREIT", command=clicked_bereit)
    button_bereit.grid(row=4, column=1, columnspan=2)
