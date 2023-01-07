print("Výtej ve hře s čísli")
print("chceš zobrazit pravidla?")
pravidlazobrazit=input()
if pravidlazobrazit=="ano":
    print("Hra vygeneruje číslo, které poté musíš uhádnout.")
import random
print("vyber náročnost (lehká,střední,těžka):")
odpoved=input()
if odpoved=="těžká":
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
if odpoved=="lehká":
    n=random.randint(1,5)
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
if odpoved=="střední":
    n=random.randint(1,15)
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