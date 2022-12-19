from math import *
from tkinter import Pack

#3.

#nimi=input("Sisestage oma nimi: ")
#try:
#    if nimi.upper()== "JUKU":
#        print("lähme kinno")
#        vanus=int(input("Kui vana sa oled? "))
#        if vanus <=0 or vanus >=100:
#            print("Viga andmetega")
#        elif vanus<=5:
#            print("tasuta")
#        elif vanus >=6 and vanus <=14:
#            print("lastepilet")
#        elif vanus >=15 and vanus <=64:
#            print("täispilet")
#        elif vanus >= 65:
#            print("sooduspilet")
#    else:
#        print("Otsime Juku")
#except:
#    ValueError

#2.

#nimi1=input("Mis sinu nimi on? ")
#nimi2=input("Mis sinu nimi on aaaah? ")
#if nimi1.isalpha() and nimi2.isalpha():
#    if nimi1.lower()== "martin" and nimi2.lower()== "oleksandr":
#        print(f"{nimi1} ja {nimi2} olete täna naabrid")
#    else:
#        print()
#else:
#    print("Vale Andmetüüp")

#3.

#try:
#    a=float(input("kirjutage esimene seina pikkus: "))
#    b=float(input("kirjutage teine seina pikkus: "))
#    if a>=0 and b>=0:
#        print("Lean pindala")
#        P=a*b
#        print(f"Pindala on: {P}")
#        print("Kas teeme remondi või ei? ")
#        vastus=input("")
#        if vastus.lower()=="jah":
#            hind=float(input("kui palju maksab ruutmeeter? "))
#            if hind<0:
#                print("Vale vastus, palun siseta positiivne arv.")
#            else:
#                põrand=hind*P
#                print(f"remondi summa on: {põrand}")
#except:
#    print("vale Andmetüüp")

#4

try:
    hind=float(input("mis on hind? (suurem kui 700) "))
    if hind >=700:
        hind=round(hind*0.7,2)
        print(f"hind soodusega on {hind}")
    else:
        ("hind on vähem kui 700")
except:
    print("Vale andmetüüp")