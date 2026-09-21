days = ["Montag", "Dienstag", "Mittwoch", "Donnerstag"]
zahl = 0

for day in days:
    print(day, zahl)
    zahl += 1

#-----------------------------------------------------------#

days2 = ["Montag", "Dienstag", "Mittwoch", "Donnerstag"]

for zahl,day in enumerate(days):
    print(day, zahl)



Zahlen = [10 ,23 ,34 ,67]

for index, zahl in enumerate(Zahlen):
    if zahl % 2 == 0:
        print(zahl)



zahlen2 = [2, 11, 12, 24]

for index2, zahl in enumerate(zahlen2):
    if zahl % 2 == 0:
        print(zahl, index2)