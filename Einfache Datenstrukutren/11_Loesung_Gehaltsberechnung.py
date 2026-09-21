gehalt = 3500
bonus_prozentsatz_ = 10

bonus = (bonus_prozentsatz_ / 100) 
grundgehalt = gehalt * bonus
gesamtgehalt = gehalt + grundgehalt

print(f"Dein Gehalt betraegt: {gesamtgehalt} Euro")