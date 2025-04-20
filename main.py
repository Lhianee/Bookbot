def get_book_text(dateipfad):
    with open(dateipfad, encoding="utf-8") as datei:
        inhalt = datei.read()
        return inhalt
def main():
    import os
    dateipfad = r"E:\Onedrive\02 Python\Github\Repositories\Bookbot\books\frankenstein.txt"    
    if os.path.exists(dateipfad):
        buch_inhalt = get_book_text(dateipfad)
        print(buch_inhalt)
    else:
        print("Datei wurde nicht gefunden!")
main ()