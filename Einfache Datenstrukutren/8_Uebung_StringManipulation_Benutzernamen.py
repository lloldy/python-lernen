# Übung: String-Manipulation - Benutzernamen erstellen
# Schreibe ein Programm, das einen Benutzernamen aus dem Vor- und Nachnamen
# bsp lösung

vorname = "Noah"
nachname = "Filipovic"

USERNAME = vorname[:2].lower() + nachname[:3].lower()

print(f"Dein Username lautet: {USERNAME}")  # Ausgabe: noafi