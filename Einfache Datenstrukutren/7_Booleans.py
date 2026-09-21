# Booleans sind ein Datentyp mit nur zwei möglichen Werten: True oder False.

ist_wach = True
ist_muede = False

print(ist_wach)
print(ist_muede)

# Vergleiche (==, >, <, !=) geben automatisch einen Boolean zurück.
zahl = 5
print(zahl > 3)   # True
print(zahl == 10) # False

# Booleans kann man auch wie Zahlen behandeln: True zählt als 1, False als 0.
print(True + True)   # 2
print(True + False)  # 1

# Mit isinstance() prüfst du, von welchem Datentyp eine Variable ist.
print(isinstance(ist_wach, bool))  # True, weil ist_wach ein Boolean ist
print(isinstance(zahl, bool))      # False, weil zahl eine Zahl (int) ist
