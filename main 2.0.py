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
    print(sys.path)
    if os.path.exists(dateipfad):
        buch_inhalt = get_book_text(dateipfad)
        num_words = count_words(dateipfad)
        #print(f"{num_words} words found in the document.")
        #num_characters = count_characters(buch_inhalt) 
        #print(num_characters)
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")

        print("--------- Character Count -------")
        char_count = count_characters(buch_inhalt)
        sorted_chars = sorted_characters(char_count)

        for char_dict in sorted_chars:
            if char_dict["char"].isalpha():
                print(f"{char_dict['char']}: {char_dict['count']}")
        print("============= END ===============")

    else:
        print("Datei wurde nicht gefunden!")

# Skript starten
main()

