einkauf = ["Mehl", "Zucker", "Hefe", "Zucker"]

print(einkauf)
print(einkauf[3][:4])

# --- Notizen zu den Zeilen oben ---
# Notiz: eine Liste steht in eckigen Klammern [], Elemente durch Komma getrennt
# Notiz: print(einkauf) gibt die ganze Liste aus
# Notiz: einkauf[3] holt das Element an Index 3 (also "Zucker", Zählung startet bei 0)
# Notiz: [:4] ist dann ein normales String-Slicing auf diesem Wort -> "Zuck"

# --- Weitere einfache Beispiele ---

# Länge der Liste (Anzahl Elemente)
print(len(einkauf))

# einzelnes Element per Index ansprechen
print(einkauf[0])

# letztes Element mit negativem Index
print(einkauf[-1])

# Element hinzufügen
einkauf.append("Salz")
print(einkauf)

# Element entfernen
einkauf.remove("Hefe")
print(einkauf)

# Slicing der ganzen Liste (erste 2 Elemente)
print(einkauf[:2])