print("Výtej ve hře s čísli")
print("chceš zobrazit pravidla?")
pravidlazobrazit=input()
if pravidlazobrazit=="ano":
    print("Hra vygeneruje číslo, které poté musíš uhádnout.")
import random
n=random.randint(1,10)
for i in range(10):
    print("Napiš číslo:")
    guestnum=int(input())
    if guestnum==n:
        print("správná odpověď")
        break
    else:
        print("špatné číslo zkus to znovu")
print("zmáčkni enter pro ukončení hry")
konec=input()