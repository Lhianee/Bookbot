import os  # Operatind System
from stats import get_book_text, count_words, count_characters, sorted_characters

# Dynamischer Dateipfad je nach Umgebung
if os.name == "nt":  # Windows
    dateipfad = r"E:\Onedrive\02Python\Github\Repositories\Bookbot\books\frankenstein.txt"
else:  # Linux (WSL)
    dateipfad = "/mnt/e/Onedrive/02Python/Github/Repositories/Bookbot/books/frankenstein.txt"
        
# Hauptfunktion: Text holen und ausgeben
def main():
    import sys
    print(sys.argv)
    


# Skript starten
main()

