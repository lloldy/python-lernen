number  = [number for number in range(1000)] # Viel kürzer als "for loop" Variante und einfacher zu lesen

#---for loop Variante---#
quadratzahlen = []
for zahl in range (1, 8):
    quadratzahlen.append(zahl**2)

print(quadratzahlen)

#---Comprehension Variante----#

quadratzahlen2 = [zahl**2 for zahl in range(1, 8)]

#--- Bsp mit erklärung ---#

zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# gerade_zahlen = [ was rein soll   for  Name in  Liste   if  Bedingung   ]
gerade_zahlen = [zahl for zahl in zahlen if zahl % 2 == 0]
#                 ↑        ↑         ↑         ↑
#                 |        |         |         Rest der Division durch 2 muss 0 sein (= gerade)
#                 |        |         Liste, die durchlaufen wird
#                 |        selbst gewählter Name, überall gleich verwendet
#                 was in die neue Liste kommt (hier unverändert die Zahl selbst)

print(gerade_zahlen)