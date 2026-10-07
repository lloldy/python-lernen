antwort = ""
kontakte = {}   # Name -> Nummer
Nummer_bereich = (3, 15)



while True:
    aktion = input("(h)inzufuegen, (a)nzeigen, (s)uchen, (e)ntfernen, (b)eenden? ").lower()
    if aktion == "h":
        kontakt = input("Geben sie die Nummer des gewünschten Kontaktes ein ")
        # prüft: min (3) <= Länge UND Länge <= max (15), also ob Nummer zwischen 3 und 15 Ziffern hat
        if kontakt.isdigit() and Nummer_bereich[0] <= len(kontakt) <= Nummer_bereich[1]:
            kontakt_name = input("wie moechten sie ihren Kontakt benenen ?")
            kontakte[kontakt_name] = kontakt 
        else:
            print("Nummer ungültig versuchen sie es nochmal ")
    elif aktion == "a":
        print (kontakte)
    elif aktion == "s":
        kontakt_name = input("Geben sie den Namen ihres gewünschten Kontaktes ein ")
        if kontakt_name in kontakte:
            print (f"{kontakte[kontakt_name]} vorhanden")
        else:
            print("Kontakt nicht vorhanden")
    elif aktion == "e":
        kontakt_name = input("Geben sie den gewünschten Namen des Kontaktes ein der entfernt werden soll ")
        if kontakt_name in kontakte:
            del kontakte[kontakt_name]
            print("Kontakt wurde erfolgreich entfernt")
        else:
            print("Kontakt nicht vorhanden")
    elif aktion == "b":
        print("Programm wird beendet")
        break
    else:
        print ("Aktion nicht vorhanden bitte tippen sie \n (h) ; (a) ; (s) ; (e) ein für eine gültige Aktion")