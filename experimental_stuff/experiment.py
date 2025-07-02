from PIL import Image, ImageTk
import time
import csv  # Oder openpyxl, siehe unten
import os
script_dir = os.path.dirname(__file__)
# Konfiguration
anzahl_panels = 6
bilder_ordner = os.path.join(script_dir, "BILDER_EXPERIMENT")
standard_reihenfolge = [f"Bild_{i}_neu.png" for i in range(1, anzahl_panels + 1)]
umgekehrte_reihenfolge = list(reversed(standard_reihenfolge))
nutzer_eingaben = []  # Liste zur Speicherung der Texte

# Widgets, die wir später brauchen
info_links = Label(fenster, text="Panels werden nur 10 Sekunden angezeigt.")
info_rechts = Label(fenster, text="Du hast danach 30 Sekunden Zeit zum Beschreiben.")
bild_label = Label(fenster)
textfeld = Text(fenster, width=50, height=10)


def starte_durchlauf(index, bilderliste):
    if index >= len(bilderliste):
        speichern()
        return

    # Setze aktuelle Bilddatei
    bildpfad = os.path.join(bilder_ordner, bilderliste[index])
    bild = Image.open(bildpfad)
    bild = bild.resize((400, 400))  # falls nötig
    bild_tk = ImageTk.PhotoImage(bild)
    bild_label.config(image=bild_tk)
    bild_label.image = bild_tk

    # Anzeigen
    info_links.grid(row=0, column=0, pady=10)
    info_rechts.grid(row=0, column=2, pady=10)
    bild_label.grid(row=1, column=0, padx=20, pady=10)
    textfeld.delete("1.0", END)
    textfeld.grid(row=1, column=2, padx=20, pady=10)

    # Nach 10 Sek: Bild ausblenden
    fenster.after(10000, lambda: bild_label.grid_forget())

    # Nach 40 Sek: Texteingabe ausblenden, Text speichern, nächster Schritt
    def naechster_schritt():
        eingabe = textfeld.get("1.0", END).strip()
        nutzer_eingaben.append((bilderliste[index], eingabe))
        textfeld.grid_forget()
        starte_durchlauf(index + 1, bilderliste)

    fenster.after(40000, naechster_schritt)


def experiment():
    # Vorherige Widgets verstecken
    for widget in fenster.winfo_children():
        widget.grid_forget()

    # Welche Reihenfolge?
    gruppe = user_info["Gruppe"]
    if gruppe == 1:
        bildfolge = standard_reihenfolge
    else:
        bildfolge = umgekehrte_reihenfolge

    # Starte mit erstem Bild
    starte_durchlauf(0, bildfolge)
