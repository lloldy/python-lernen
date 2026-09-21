MIN_PASSWORD_LEN = 8

password = input("Gib hier dein Passwort ein:\n") 

password_len = len(password)

if password_len >= MIN_PASSWORD_LEN:
    print("Erfolgreich Registriert")
else:
    print("Dein Password ist zu kurz")


NOTE = 70
gut = 80
bestanden = 50

if NOTE >= gut:
    print("Deine Note ist gut")
elif NOTE >= bestanden:
    print("Du hast bestanden")
else:
    print("Du bist leider durchgefallen")