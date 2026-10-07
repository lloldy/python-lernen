# Übungsaufgabe: Notenverwaltung
#
# Baue ein Programm, das Schulnoten für Schüler verwaltet.
# Speichere die Daten in einem Dictionary: Name -> Liste von Noten (int).
#
# Das Programm soll in einer Schleife laufen und den Nutzer fragen, welche
# Aktion er ausführen möchte:
#   (h) Note hinzufügen
#   (a) alle Schüler mit ihren Noten anzeigen
#   (d) Durchschnittsnote eines Schülers berechnen und anzeigen
#   (e) einen Schüler komplett entfernen
#   (b) Programm beenden
#
# Bedingungen:
# 1. Beim Hinzufügen (h):
#    - Nutzer gibt zuerst den Namen des Schülers ein.
#    - Danach gibt der Nutzer eine Note ein.
#    - Die Note muss eine ganze Zahl zwischen 1 und 6 sein (Noten_bereich = (1, 6)).
#      Ist die Eingabe keine Zahl oder außerhalb des Bereichs, soll eine
#      Fehlermeldung ausgegeben werden und die Note NICHT gespeichert werden.
#    - Existiert der Schüler noch nicht im Dictionary, lege eine neue leere
#      Liste für ihn an, bevor du die Note hinzufügst.
#
# 2. Beim Anzeigen (a):
#    - Gib jeden Schüler mit seiner Notenliste aus.
#    - Falls noch keine Schüler vorhanden sind, gib eine passende Meldung aus.
#
# 3. Beim Durchschnitt berechnen (d):
#    - Nutzer gibt den Namen eines Schülers ein.
#    - Existiert der Schüler, berechne und zeige den Durchschnitt seiner Noten
#      (gerundet auf 2 Nachkommastellen).
#    - Existiert der Schüler nicht, gib eine Fehlermeldung aus.
#
# 4. Beim Entfernen (e):
#    - Nutzer gibt den Namen eines Schülers ein.
#    - Existiert der Schüler, entferne ihn komplett aus dem Dictionary.
#    - Existiert der Schüler nicht, gib eine Fehlermeldung aus.
#
# 5. Bei ungültiger Aktion (weder h, a, d, e noch b):
#    - Gib eine Meldung aus, die alle gültigen Aktionen nochmal auflistet.
#
# 6. Bei (b) soll das Programm mit einer Abschiedsmeldung beendet werden.
#
# Tipp: Achte auf denselben Aufbau wie in 12_Eigene_Test_Aufgabe:
#       while True: -> input() für Aktion -> if/elif-Kette -> break bei "b"

Notendatenbank = {}
notenbereich = (1, 6)

while True:
    print("Willkommen zum Notenmanager")
    aktion = input("(h) Note hinzufügen\n(a) alle Schüler mit ihren Noten anzeigen\n(d) Durchschnittsnote eines Schülers berechnen und anzeigen\n(e) einen Schüler komplett entfernen\n(b) Programm beenden").lower()

    if aktion == "h":
        Name = input("geben sie den Namen des Schülers ein")
        Note = input("Geben sie die Note des Schülers ein")
        if Note.isdigit() and notenbereich[0] <= int(Note) <= notenbereich[1]:
         # KORREKTUR: Schüler existiert noch nicht -> leere Liste anlegen
            if Name not in Notendatenbank:
                Notendatenbank[Name] = []
            # KORREKTUR: Note als int (nicht als String) in die Liste anhängen
            Notendatenbank[Name].append(int(Note))
        else:
            # KORREKTUR: passendere Fehlermeldung, da nicht die Aktion sondern die Note ungültig ist
            print("Ungültige Note")

    elif aktion == "a":
        # KORREKTUR: Meldung falls Dictionary leer ist (siehe Aufgabe Punkt 2)
        if not Notendatenbank:
            print("Es sind noch keine Schüler vorhanden")
        else:
            print(Notendatenbank)

    elif aktion == "d":
        Name = input("geben sie den Namen des Schülers ein")
        if Name in Notendatenbank:
            noten = Notendatenbank[Name]
            durchschnitt = sum(noten) / len(noten)
            print(f"Durchschnitt von {Name}: {round(durchschnitt, 2)}")
        else:
            print("Schüler nicht vorhanden")

    elif aktion == "e":
        Name = input("geben sie den Namen des Schülers ein")
        if Name in Notendatenbank:
            del Notendatenbank[Name]
        else:
            print("Schüler nicht vorhanden")

    elif aktion == "b":
        print("Auf Wiedersehen!")
        break
    else:
        print("Ungültige Aktion. Gültige Aktionen: h, a, d, e, b")
