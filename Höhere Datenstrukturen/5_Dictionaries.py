roosbr = dict() #macht es zu einem Dictionary (leer, wird unten mit Keys befüllt)

roosbr["Gehalt"] = 3065.94
roosbr["Vorname"] = "Bruno"
roosbr["Nachname"] = "Roos"
roosbr["Aufgaben"] = ["Telefonserivce", "Kundenberatung"]

print(roosbr["Aufgaben"])
print(roosbr.get("Jahresgehalt", "Keine Info"))
# Notiz: get() gibt den zweiten Wert ("Keine Info") zurück, WENN der Key nicht existiert,
# statt wie roosbr["Jahresgehalt"] einen KeyError zu werfen -> dadurch sicherer/robuster.


# --- Zusammenfassung: Dictionaries ---

# Eigenschaften:
# - Speichern Key-Value-Paare (Schlüssel -> Wert), kein Index wie bei Listen.
# - Keys müssen einzigartig sein (wird ein Key doppelt vergeben, überschreibt der neue Wert den alten)
#   und müssen hashable sein (z.B. String, Zahl, Tupel - keine Liste als Key).
# - Values dürfen beliebig sein, auch Listen (siehe "Aufgaben" oben) oder sogar andere Dictionaries.
# - Seit Python 3.7 behalten Dictionaries die Einfügereihenfolge bei (vorher galt das nicht garantiert).
# - Mutable: Werte können nachträglich geändert, hinzugefügt oder entfernt werden.

# Weitere wichtige Funktionen (Ergänzung zu dict(), [], .get()):
print(roosbr.keys())     # alle Keys als Liste-ähnliches Objekt
print(roosbr.values())   # alle Values
print(roosbr.items())    # alle (Key, Value) Paare als Tupel

print("Vorname" in roosbr)   # Mitgliedschaftstest prüft bei Dictionaries den KEY, nicht den Value

roosbr["Gehalt"] = 3200.00   # bestehenden Key überschreiben (Update)
roosbr.pop("Nachname")       # entfernt Key "Nachname" (inkl. Value) und gibt den Wert zurück
del roosbr["Vorname"]        # entfernt Key "Vorname", gibt aber nichts zurück

print(roosbr)

# Effizienz-Tipp:
# Wie bei Sets basieren Dictionaries intern auf Hashing -> Zugriff über einen Key ist im
# Schnitt O(1) (sehr schnell), unabhängig davon wie viele Einträge das Dictionary hat.

# Einsatzzweck:
# Dictionaries eignen sich, wenn Daten über einen aussagekräftigen Namen statt über eine
# Position abgerufen werden sollen (z.B. roosbr["Gehalt"] statt sich zu merken "Gehalt steht
# an Index 3"). Ideal für strukturierte Datensätze wie hier ein Mitarbeiter-Profil.