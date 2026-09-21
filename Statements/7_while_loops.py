zahl = 0

while zahl <= 10: 
    print(zahl)
    zahl += 1


antwort = ""

while antwort.lower() != "ja":                                  # lower macht das wenn die antwort kleingeschrieben ja wäre es passt also das "JA" oder "jA/Ja" auch geht. Das selbe geht auch mit upper
    antwort = input("Möchtest du Fortfahren? (ja/nein) ")     #Zeile endet erst wenn antwort ja ist weil Schleife aktiv ist solange != "ja" (nicht "ja")

print("Programm beendet")


# Beispiel mit break: Schleife sofort verlassen, egal was Bedingung sagt
zahl = 0

while True:
    print(zahl)
    if zahl == 5:
        break
    zahl += 1


# Beispiel mit continue: aktuellen Durchlauf überspringen, Schleife läuft weiter
zahl = 0

while zahl < 10:
    zahl += 1
    if zahl % 2 == 0:
        continue        # gerade Zahlen überspringen
    print(zahl)