# Funktion zur Verarbeitung des Buchinhalts
def get_book_text(dateipfad):
    with open(dateipfad, encoding="utf-8") as datei:
        inhalt = datei.read()
        return inhalt 
# Funktion zur Zählung der Worte
def count_words(dateipfad):
    counted = len(get_book_text(dateipfad).split())
    return counted 
# Funktion zur Zählung der Buchstaben und Zeichen
def count_characters(text):
    text = text.lower()
    letter_count = {}
    for letter in text:
        letter_count[letter] = letter_count.get(letter, 0) + 1
    return letter_count
# Funktion zur Sortierung der gezählten Buchstaben
def sorted_characters(char_count):
    sorted_list = []
    for letter, count in char_count.items():
        char_dict = {"char": letter, "count": count}
        sorted_list.append(char_dict)
    # Hilfsfunktion 
    def sort_on(dict):
        return dict["count"]
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list