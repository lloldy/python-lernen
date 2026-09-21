# == gleich
# != ungleich

print(1 == 1)
print(2 == 1)
print(2 == True + True)
print(0 == False)

zutat = "Mehl"
Zutaten_liste = ["Mehl", "Zucker", "Hefe"]

print(zutat == Zutaten_liste[0])

einkaufs_liste = ["Hefe", "Zucker", "Mehl"]

Zutaten_liste.sort()
einkaufs_liste.sort()
print(Zutaten_liste == einkaufs_liste)

# --- weitere Vergleichsoperatoren, die klassisch dazugehören ---

# < und > - kleiner als / größer als
alter = 20
print(alter < 18)   # False
print(alter > 18)   # True

# <= und >= - kleiner-gleich / größer-gleich
print(alter >= 20)  # True
print(alter <= 18)  # False

# is - prüft, ob zwei Variablen auf dasselbe Objekt zeigen (nicht nur denselben Wert)
liste_a = [1, 2, 3]
liste_b = [1, 2, 3]
liste_c = liste_a

print(liste_a == liste_b)  # True, gleicher Inhalt
print(liste_a is liste_b)  # False, zwei unterschiedliche Objekte im Speicher
print(liste_a is liste_c)  # True, liste_c zeigt auf dasselbe Objekt wie liste_a
