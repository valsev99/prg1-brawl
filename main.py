import random

# Startvärdena väljer du själv.
spelare1_hp = 100
spelare2_hp = 100

# Ditt första kort börjar här.

Karaktär = int(input(print(""""
Spelare 1 välg din karaktär

klicka 1 för Ninja som använder fötterna bara
klicka 2 för En tjok sumobrottare
klicka 3 för En norsk Viking som hoppar i vatten 
klicka 4 för En Gladiator 
klicka 5 för Brittisk ganskter med machete
klicka 6 för En stormtuper
klicka 7 för Joaquín Archibaldo Guzmán Loera, El Supremo 
""")))

if Karaktär == 1:
    Spelare1 = ("Ninja")

if Karaktär == 2:
    Spelare1 = ("sumobrottare")

if Karaktär == 3:
    Spelare1 = ("Viking")

if Karaktär == 4:
    Spelare1 = ("Gladiator")

if Karaktär == 5:
    Spelare1 = ("Gangster")

if Karaktär == 6:
    Spelare1 = ("stormtroper")

if Karaktär == 7:
    Spelare1 = ("Joaquín")


Karaktär = int(input(print(""""
Spelare 2 välg din karaktär

klicka 1 för Ninja som använder fötterna bara
klicka 2 för En tjok sumobrottare
klicka 3 för En norsk Viking som hoppar i vatten 
klicka 4 för En Gladiator 
klicka 5 för Brittisk ganskter med machete
klicka 6 för En stormtuper
klicka 7 för Joaquín Archibaldo Guzmán Loera, El Supremo 
""")))

if Karaktär == 1:
    Spelare2 = ("Ninja")

if Karaktär == 2:
    Spelare2 = ("sumobrottare")

if Karaktär == 3:
    Spelare2 = ("Viking")

if Karaktär == 4:
    Spelare2 = ("Gladiator")

if Karaktär == 5:
    Spelare2 = ("Gangster")

if Karaktär == 6:
    Spelare2 = ("stormtroper")

if Karaktär == 7:
    Spelare2 = ("Joaquín")


start_val = input(print("Okej spelare 1 är "+ Spelare1 +"och spelare 2 är "+ Spelare2 +" klicka 1 för att starta"))
if start_val == 1:
    vem_som_börjar = 