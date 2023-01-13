import random

print("Výtej ve hře s čísly")
print("Chceš zobrazit pravidla?")
pravidlazobrazit=input()

if pravidlazobrazit=="ano":
    print("Hra vygeneruje číslo, které poté musíš uhádnout.")

print("vyber náročnost (lehká,střední,těžka):")
odpoved=input()
pocet_cisel = 5

if odpoved == "těžká":
    pocet_cisel = 30

elif odpoved == "střední":
    pocet_cisel = 15

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
        if guestnum<n:
            print("Číslo je větší")

        if guestnum>n:
            print("Číslo je menší")

print("správné číslo je:")
print(n)
print("pro ukončení hry zmáčkni enter")
konec=input()
