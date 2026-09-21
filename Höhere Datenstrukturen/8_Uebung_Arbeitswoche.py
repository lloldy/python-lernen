
Wochentage = ("Montag","Dienstag","Mittwoch","Donnerstag","Freitag","Samstag","Sonntag")
Arbeitstage = ["Montag","Dienstag","Mittwoch","Donnerstag","Freitag"]


del Arbeitstage[0]
Arbeitstage.append(Wochentage[-2])

print(Arbeitstage)
