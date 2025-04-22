# Funktion zur Verarbeitung des Buchinhalts
def get_book_text(dateipfad):
    with open(dateipfad, encoding="utf-8") as datei:
        inhalt = datei.read()
        return inhalt
    
# Funktion zur Zählung der Worte
def count_words(dateipfad):
        counted = len(get_book_text(dateipfad).split())
        return counted 