print("Výtej ve hře s čísli")
print("chceš zobrazit pravidla?")
pravidlazobrazit=input()
if pravidlazobrazit=="ano":
    print("Hra vygeneruje číslo, které poté musíš uhádnout.")
import random
n=random.randint(1,30)
print("kolik chceš pokusů?")
pokus=int(input())
for i in range(pokus):
    print("Napiš číslo:")
    guestnum=int(input())
    if guestnum==n:
        print("správná odpověď")
        break
    else:
        print("špatné číslo")
print("zmáčkni enter pro ukončení hry")
konec=input()