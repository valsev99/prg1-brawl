import random

spelare1_liv = 100
spelare2_liv = 100


Karaktär = int(input(print(""""
Spelare 1 välg din karaktär

klicka 1 för Ninja som använder fötterna bara
klicka 2 för En tjok sumobrottare
klicka 3 för En norsk Viking som hoppar i vatten 
klicka 4 för Brittisk ganskter med machete
klicka 5 för En stormtuper
klicka 6 för Joaquín Archibaldo Guzmán Loera, El Supremo 
""")))

if Karaktär == 1:
    Spelare1 = ("Ninja")

if Karaktär == 2:
    Spelare1 = ("sumobrottare")

if Karaktär == 3:
    Spelare1 = ("Viking")

if Karaktär == 4:
    Spelare1 = ("Gangster")

if Karaktär == 5:
    Spelare1 = ("stormtroper")

if Karaktär == 6:
    Spelare1 = ("Joaquín")


Karaktär = int(input(print(""""
Spelare 2 välg din karaktär

klicka 1 för Ninja som använder fötterna bara
klicka 2 för En tjok sumobrottare
klicka 3 för En norsk Viking som hoppar i vatten 
klicka 4 för Brittisk ganskter med machete
klicka 5 för En stormtuper
klicka 6 för Joaquín Archibaldo Guzmán Loera, El Supremo 
""")))

if Karaktär == 1:
    Spelare2 = ("Ninja")

if Karaktär == 2:
    Spelare2 = ("sumobrottare")

if Karaktär == 3:
    Spelare2 = ("Viking")

if Karaktär == 4:
    Spelare2 = ("Gangster")

if Karaktär == 5:
    Spelare2 = ("stormtroper")

if Karaktär == 6:
    Spelare2 = ("Joaquín")


start_val = input(print("Okej spelare 1 är "+ Spelare1 + " och spelare 2 är "+ Spelare2 +" klicka 1 för att starta spelare 1 börjar"))
if start_val == "1":
        
        if Spelare1 == "Ninja": 
            ninja_val1 = input(print("""
              välj din attack
klicka 1 för Ninja spark 20-40 skada
klicka 2 för Kassta kastkärnor 50 att pricka och 30-80 skada
klicka 3 för Ninja GO 25 chans att lyckas och 85 skada"""))
            if ninja_val1 == "1":
                skada_ninja_spark = random.randint (20, 40)
                spelare2_liv - skada_ninja_spark
                print (spelare2_liv)

            


        
