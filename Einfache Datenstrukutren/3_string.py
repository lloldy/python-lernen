zahl = 12
satz = str ("Hello, World!")

# Notiz: Jetzt ohne verschachteltes print() - gibt einfach beide Klassen aus.
print(type(satz),(type(zahl)))

# Notiz: \n in einem String erzeugt einen Zeilenumbruch beim Ausgeben.
text = "Das ist ein Beispiel satz und ich hab keine Ahnung nicht warum er nicht kürzer ist ! \n Guck mal ein Zeilenumbruch ich bin eine Zeile niedriger"

# Notiz: """...""" erlaubt einen String ueber mehrere Zeilen, ohne \n zu brauchen.
text2 = """Dies ist ein Beispiel satz und ich hab keine Ahnung nicht warum er nicht kürzer ist !
 Guck mal ein Zeilenumbruch ich bin eine Zeile niedriger"""

print(text + "\n" + text2)

# Notiz: \t erzeugt einen Tabstopp (Einrueckung) beim Ausgeben.
text3 = "Hier kommt ein \t TAB"

print(text3)

# --- ein paar weitere kurze Beispiele ---

# Notiz: + haengt Strings aneinander (verketten).
print("Hallo" + " " + "Welt")

# Notiz: len() gibt die Anzahl Zeichen zurueck.
print(len(satz))

# Notiz: [] liest ein Zeichen an einer Position aus (0 = erstes Zeichen).
print(satz[0])

# Notiz: .upper() / .lower() aendern Gross-/Kleinschreibung.
print(satz.upper())
print(satz.lower())