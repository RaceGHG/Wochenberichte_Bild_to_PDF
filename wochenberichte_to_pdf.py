import os
from PIL import Image
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

def bild_in_pdf_konvertieren(bild_datei, pdf_datei):
    try:
        bild = Image.open(bild_datei)
        bild.save(pdf_datei, "PDF", resolution=100.0)
        return True
    except Exception as e:
        print(f"Fehler beim Konvertieren von {bild_datei} zu PDF: {str(e)}")
        return False

def auswahl_bild_verzeichnis():
    global bild_verzeichnis
    bild_verzeichnis = filedialog.askdirectory(title="Wähle das Verzeichnis mit den Wochenberichten")
    if bild_verzeichnis:
        bild_verzeichnis_label.config(text=bild_verzeichnis)

def auswahl_pdf_verzeichnis():
    global pdf_verzeichnis
    pdf_verzeichnis = filedialog.askdirectory(title="Wähle das Zielverzeichnis für die PDFs")
    if pdf_verzeichnis:
        pdf_verzeichnis_label.config(text=pdf_verzeichnis)

def umwandeln_button():
    if not bild_verzeichnis or not pdf_verzeichnis:
        ausgabe_label.config(text="Bitte Verzeichnisse auswählen.")
        return

    bilder = [datei for datei in os.listdir(bild_verzeichnis) if datei.lower().endswith(tuple(unterstuetzte_formate))]

    if not bilder:
        ausgabe_label.config(text="Keine unterstützten Bilddateien gefunden.")
    else:
        os.makedirs(pdf_verzeichnis, exist_ok=True)
        erfolgreich_umgewandelt = 0

        for bild in bilder:
            bild_nummer = bild.split("_")[1].split(".")[0]
            pdf_datei = os.path.join(pdf_verzeichnis, f"Wochenbericht_{bild_nummer}.pdf")
            bild_datei = os.path.join(bild_verzeichnis, bild)
            if bild_in_pdf_konvertieren(bild_datei, pdf_datei):
                erfolgreich_umgewandelt += 1

        if erfolgreich_umgewandelt == len(bilder):
            ausgabe_label.config(text="Alle Wochenberichte erfolgreich in PDF umgewandelt.")
        else:
            ausgabe_label.config(text=f"{erfolgreich_umgewandelt} von {len(bilder)} Wochenberichten erfolgreich umgewandelt. Einige Konvertierungsfehler traten auf.")

root = tk.Tk()
root.title("Wochenberichte in PDF umwandeln")
root.geometry("800x400")

# Hintergrundfarbe auf dunkles Grau setzen
root.configure(bg="#565656")

# Unterstützte Bildformate
unterstuetzte_formate = (".jpeg", ".jpg", ".png", ".gif")

ausgabe_label = tk.Label(root, text="")
ausgabe_label.pack()
# Hintergrundfarbe der Labels auf dunkles Grau setzen
ausgabe_label.configure(bg="#565656")

bild_verzeichnis_label = tk.Label(root, text="")
bild_verzeichnis_label.pack()
# Hintergrundfarbe der Labels auf dunkles Grau setzen
bild_verzeichnis_label.configure(bg="#565656")

pdf_verzeichnis_label = tk.Label(root, text="")
pdf_verzeichnis_label.pack()
# Hintergrundfarbe der Labels auf dunkles Grau setzen
pdf_verzeichnis_label.configure(bg="#565656")

style = ttk.Style()
style.map("C.TButton",
          foreground=[("active", "blue"), ("!active", "black")],
          background=[("active", "lightgray"), ("!active", "gray")]
          )

auswahl_bild_button = ttk.Button(root, text="Wochenberichte Verzeichnis auswählen", style="C.TButton", command=auswahl_bild_verzeichnis)
auswahl_bild_button.pack(padx=20, pady=10)

auswahl_pdf_button = ttk.Button(root, text="Zielverzeichnis auswählen", style="C.TButton", command=auswahl_pdf_verzeichnis)
auswahl_pdf_button.pack(padx=20, pady=10)

umwandeln_button = ttk.Button(root, text="Umwandeln", style="C.TButton", command=umwandeln_button)
umwandeln_button.pack(padx=20, pady=10)

# Copyright-Symbol und Text hinzufügen
copyright_label = tk.Label(root, text="\u00A9 Fabian Hellmann")
copyright_label.pack()
# Hintergrundfarbe und Schriftfarbe des Copyright-Labels anpassen
copyright_label.configure(bg="#565656", foreground="white")

root.mainloop()
