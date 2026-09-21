# Tuples ()Klammern, Listen [] Klammern
# Tuples sind unveränderbar

einkauf = ("Apfel", "Mehl", "Zucker")
essen = ("Apfel",) # komma wichtig bei nur einem Inhalt

repetive_number = (1,)*7  #klappt auch bei Listen
print(repetive_number)


a,b,c = (1,2,3)
 
print(a) 

d = 1
e = 2

e,d = d,e

print(d)


# --- Zusammenfassung Tuples ---

# Unveränderbarkeit (immutable):
# Ein Tuple kann nach dem Erstellen NICHT mehr geändert werden.
# Kein Hinzufügen, kein Entfernen, kein Überschreiben einzelner Werte.
# einkauf[0] = "Birne"  # -> TypeError: 'tuple' object does not support item assignment (deshalb auskommentiert)
# Man kann nur ein KOMPLETT NEUES Tuple erzeugen, z.B. durch Zusammenfügen:
einkauf2 = einkauf + ("Milch",)
print(einkauf2)

# Effizienz:
# Weil Tuples unveränderbar sind, kann Python sie schlanker im Speicher ablegen
# und schneller lesen als Listen. Für Daten, die sich nicht ändern sollen,
# sind Tuples deshalb die bessere (schnellere, sparsamere) Wahl als Listen.

# Länge und Methoden:
# Tuples haben nur ZWEI eingebaute Methoden (im Gegensatz zu vielen bei Listen),
# eben weil man sie nicht verändern kann.
print(len(einkauf))          # Anzahl Elemente
print(einkauf.count("Apfel")) # wie oft kommt "Apfel" vor
print(einkauf.index("Mehl"))  # an welcher Position steht "Mehl"

# Umwandeln zwischen Tuple und Liste:
einkauf_liste = list(einkauf)   # Tuple -> Liste (jetzt veränderbar)
einkauf_liste.append("Butter")
einkauf_zurueck = tuple(einkauf_liste)  # Liste -> Tuple (wieder fixiert)
print(einkauf_zurueck)

# Verschachtelte Tuples (Tuple in Tuple):
koordinate = (3, 7)
punkte = (koordinate, (0, 0), (5, 5))
print(punkte[0])

# Erweitertes Unpacking mit *:
erster, *rest = einkauf
print(erster)
print(rest)

# Typische Use Cases:
# - feste Datensätze, die sich logisch nie ändern (z.B. Koordinaten, RGB-Farbwerte)
# - Rückgabe mehrerer Werte aus einer Funktion
# - Tauschen von Variablen (siehe e,d = d,e oben)
# - als Dictionary-Key, weil Tuples "hashable" sind - Listen dürfen NICHT als Key
#   verwendet werden, Tuples schon:
orte = {(48, 11): "München", (52, 13): "Berlin"}
print(orte[(48, 11)])

# Tipp: Wenn du dir nicht sicher bist, ob du Liste oder Tuple brauchst -
# frag dich "Soll sich das jemals ändern?". Nein -> Tuple, Ja -> Liste.