import os  # Operatind System

# Dynamischer Dateipfad je nach Umgebung
if os.name == "nt":  # Windows
    dateipfad = r"E:\Onedrive\02Python\Github\Repositories\Bookbot\books\frankenstein.txt"
else:  # Linux (WSL)
    dateipfad = "/mnt/e/Onedrive/02Python/Github/Repositories/Bookbot/books/frankenstein.txt"

# Funktion zur Verarbeitung des Buchinhalts
def get_book_text(dateipfad):
    with open(dateipfad, encoding="utf-8") as datei:
        inhalt = datei.read()
        return inhalt

# Hauptfunktion: Text holen und ausgeben
def main():
    if os.path.exists(dateipfad):
        buch_inhalt = get_book_text(dateipfad)
        print(buch_inhalt)
    else:
        print("Datei wurde nicht gefunden!")

# Skript starten
main()