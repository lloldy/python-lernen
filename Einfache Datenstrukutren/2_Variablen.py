# Notiz: Eine Variable speichert einen Wert unter einem Namen ab.
buch_seiten = 67
buch_teile = 5

# Notiz: Man kann mit Variablen genauso rechnen wie mit Zahlen direkt.
print(buch_seiten * buch_teile)

# Notiz: GROSSBUCHSTABEN sind nur eine Konvention fuer Werte, die sich
# nicht mehr aendern sollen (Konstanten). Python verhindert das aendern
# technisch aber nicht - es ist reine Absprache unter Programmierern.
USER_AGE = 25
user_age = 23

# Notiz: type() zeigt, welchen Datentyp die Variable gerade enthaelt.
print(type(USER_AGE))

average_age = 22

# Notiz: += ist die Kurzform fuer "average_age = average_age + 1"
average_age += 1

print(average_age)

# Notiz: Genauso gibt es -=, *= und /= als Kurzformen.
punkte = 10
punkte -= 3
print(punkte)

punkte *= 2
print(punkte)

punkte /= 4
print(punkte)

# Notiz: Variablen koennen auch Text (String) speichern, nicht nur Zahlen.
name = "Filip"
print(name)

# Notiz: Eine Variable kann jederzeit ueberschrieben werden -
# auch mit einem anderen Datentyp.
name = 5
print(type(name))
