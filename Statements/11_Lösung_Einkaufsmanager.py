einkaufsliste = []

while True:
    aktion = input("Moechtest du einen Artikel (h)inzufügen, (a)nzeigen, (e)ntfernen oder Das Programm (b)eenden ? ").lower()
    if aktion == "h":
        artikel = input("Welchen Artikel möchtest du hinzufügen? ")
        einkaufsliste.append(artikel)
        print(artikel, "wurde Erfolgreich zu Liste hinzugefügt")
    elif aktion == "a":
        print(einkaufsliste)
    elif aktion == "e":
        artikel = input("Welchen Artikel möchtest du entfernen?")
        if artikel.lower in einkaufsliste:
            einkaufsliste.remove(artikel)
        else: print("Artikel nicht enhalten")
    elif aktion == "b":
        print("Programm beeendet")
        break 
    else:
        print("Ungültige eingabe bitte wähle `a`; `h` ; `e` oder `b` ")