print(len(["Hallo", "Autobahn", "Essen"]))

wochentage = ["montag", "dienstag", "mittwoch"]
wochentage.append("Donnerstag")
wochentage.insert(4,"Haselnuss")

wochenende = ["Samstag", "Sonntag"]
wochentage.extend(wochenende)

print(f"Eine woche hat {len(wochentage)} Wochentage naemlich\n {wochentage}" )

zahlen = [7,1,2,3,4,1,5]
zahlen.remove(1)

print(zahlen)

obstsorten = ["Apfel", "bananen", "pfirsich"]
print(obstsorten.pop(0))
print(obstsorten)

# --- weitere Listenfunktionen, die klassisch dazugehören ---

# remove() - entfernt ein bestimmtes Element
wochentage.remove("mittwoch")
print(wochentage)

# insert() - fügt an einer bestimmten Position ein (Index, Wert)
wochentage.insert(0, "sonntag")
print(wochentage)

# pop() - entfernt das letzte Element und gibt es zurück
letzter_tag = wochentage.pop()
print(letzter_tag)
print(wochentage)

# index() - findet die Position eines Elements
print(wochentage.index("montag"))

# count() - zählt, wie oft ein Element vorkommt
print(wochentage.count("montag"))

# sort() - sortiert die Liste alphabetisch
wochentage.sort()
print(wochentage)
