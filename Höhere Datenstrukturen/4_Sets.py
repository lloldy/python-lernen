einkauf = {"Mehl", "zucker", "Hefe"}
einkauf.add("Nutella")

print(type(einkauf))
print(einkauf)


liste = list (set(["Milch", "Schrauben", "Milch", "Nuttela"]))  #gut um duplikate zu entfernen da sets keine erlauben. # Um es dann wieder zu liste zu machen einfach "list" vor "set"
print(liste)


# --- Zusammenfassung: Sets ---

# Eigenschaften:
# - Ungeordnet: Sets haben keine feste Reihenfolge, deshalb kein Zugriff per Index (kein einkauf[0]).
# - Einzigartig: Jedes Element kommt nur einmal vor, Duplikate werden automatisch entfernt.
# - Veränderbar (mutable): Elemente können hinzugefügt/entfernt werden, ABER die Elemente selbst
#   müssen "hashable" sein -> z.B. keine Listen als Set-Element möglich (nur Zahlen, Strings, Tupel, ...).

# Elemente entfernen:
einkauf.remove("Hefe")     # entfernt "Hefe", wirft KeyError falls Element nicht existiert
einkauf.discard("Salz")    # entfernt "Salz" falls vorhanden, KEIN Fehler falls nicht vorhanden
print(einkauf)

# Mengenoperationen (typischer Einsatzzweck von Sets):
a = {"Mehl", "Zucker", "Hefe"}
b = {"Hefe", "Nutella"}

print(a | b)   # Vereinigung (union): alle Elemente aus a und b
print(a & b)   # Schnittmenge (intersection): nur Elemente, die in beiden vorkommen
print(a - b)   # Differenz (difference): Elemente, die nur in a sind
print(a ^ b)   # Symmetrische Differenz: Elemente, die nur in einem der beiden sind

# Mitgliedschaftstest:
print("Mehl" in a)   # True/False - sehr schnell, da Sets intern mit Hashing arbeiten

# Effizienz-Tipp:
# "in"-Abfragen sind bei Sets im Schnitt O(1) (sehr schnell), bei Listen dagegen O(n)
# (Python muss die Liste im schlimmsten Fall komplett durchsuchen).
# Deshalb sind Sets ideal, wenn man oft prüfen will, ob ein Element enthalten ist,
# oder wenn man Duplikate aus großen Datenmengen entfernen möchte.