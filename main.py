import random

spelare1_liv = 100
spelare2_liv = 100


Karaktär = int(input(print(""""

Spelare 1 välg din karaktär

klicka 1 för Ninja som använder fötterna bara
klicka 2 för Brittisk ganskter med machete
klicka 3 för En stormtuper
klicka 4 för Joaquín Archibaldo Guzmán Loera, El Supremo 
""")))

if Karaktär == 1:
    Spelare1 = ("Ninja")

if Karaktär == 2:
    Spelare1 = ("Gangster")

if Karaktär == 3:
    Spelare1 = ("stormtroper")

if Karaktär == 4:
    Spelare1 = ("Joaquín")


Karaktär = int(input(print(""""

Spelare 2 välg din karaktär

klicka 1 för Ninja som använder fötterna bara
klicka 2 för Brittisk ganskter med machete
klicka 3 för En stormtuper
klicka 4 för Joaquín Archibaldo Guzmán Loera, El Supremo 
""")))

if Karaktär == 1:
    Spelare2 = ("Ninja")

if Karaktär == 2:
    Spelare2 = ("Gangster")

if Karaktär == 3:
    Spelare2 = ("stormtroper")

if Karaktär == 4:
    Spelare2 = ("Joaquín")


start_val = input(print("Okej spelare 1 är "+ Spelare1 + " och spelare 2 är "+ Spelare2 +" klicka 1 för att starta spelare 1 börjar"))
if start_val == "1":
        
        if Spelare1 == "Ninja": 
            ninja_val1 = input(print("""
              välj din attack
klicka 1 för Ninja spark 20-40 skada
klicka 2 för Kassta kastkärnor 50% att pricka och 30-80 skada
klicka 3 för Ninja GO 25% chans att lyckas och 85 skada"""))

#NINJAN

skada_ninja_kastkärnor = 13123
skada_ninja_spark = 14913

            
if ninja_val1 == "1":
                skada_ninja_spark = random.randint (20, 40)
                spelare2_liv -= skada_ninja_spark
                print((f"du tog {spelare2_liv} skada på spelare 2 har {spelare2_liv} liv kvar"))


if ninja_val1 == "2":
                for_ninja_kastkärnor = random.randint (1, 2)
                if for_ninja_kastkärnor == 1:
                    print("attacken mislyckades")
                if for_ninja_kastkärnor == 2:
                    skada_ninja_kastkärnor = random.randint (30, 80)
                    spelare2_liv -= skada_ninja_kastkärnor
                print(f"attacken lyckades du tog {skada_ninja_kastkärnor} skada spelare 2 har {spelare2_liv} liv kvar")


if ninja_val1 == "3":
                for_ninjaGO = random.randint (1, 4)
                if for_ninjaGO != 4:
                    print("attacken misslyckades")
                    
                else:
                        spelare2_liv -= 85
                        print("""
                        
                        attacken lyckades do tog 85 skada
                        spelare 2 har """ + str(spelare2_liv) + """ liv kvar
                        """)

#GANGSTER
skada_slåmedhand = 400
Gangster_val_attack=233
if Spelare1 == "Gangster":
    Gangster_val_attack = input(print("""
                Välj din attack
klicka 1 för slå med machete 75% chans at lyckas 30-45 skada
klicka 2 för ring roadman 10% chans att lyckas 100 skada
klicka 3 för slå med hand 15-30 skada"""))

    
    if Gangster_val_attack == "1":
        for_gangster_machete = random.randint (1,4)
        if for_gangster_machete == 1:
            print("attacken misslyckades")
        else:
            gangster_machete_skada = random.randint (30, 45)
            spelare2_liv -= gangster_machete_skada
            print("attacken lyckades du tog " + str(gangster_machete_skada) + " skada spelare 2 har " + str(spelare2_liv) + " kvar")


if Gangster_val_attack == "2":
    for_rodeman = random.randint (1, 10)
    if for_rodeman == 1:
        print("attacken lyckades spelare 1 van")
    else:
        print("attacken mislyckades")


if Gangster_val_attack == "3":
    skada_slåmedhand = random.randint (15, 30)
    spelare2_liv -= skada_slåmedhand
print((f"du tog {skada_slåmedhand} spelare 2 har {spelare2_liv} liv kvar"))


#STROMTROPER

stormtroper_val=333
if Spelare1 == "stormtroper": 
            stormtroper_val = input(print("""
              välj din attack
klicka 1 för att sjuta du har 1 i 100 att pricka
klicka 2 för att ge up"""))

if stormtroper_val == "1":
     stormtroper_chans = random.randint (1, 100)
     if stormtroper_chans == 67:
          print("Du lyckades pricka du van")
     else:
          print("Du missade")

elif stormtroper_val == "2":
     ge_up_stormtruper = random.randint (1, 2)
     if ge_up_stormtruper == 1:
        print("du försökte sjuta dig själv men du missa så du är fortfarande inne")
     else:
          print("du gav up")


#JOAQIM


joaquin_armbåghopp_skada = 113
joaquin_armbåg_skada = 222
joaquin_attack_val = 444
joaquin_sås_skada = 13
for_joaquin_armbågehopp = 123
for_joaquin_sås = 123123


if Spelare1 == "Joaquín":
     joaquin_attack_val = input(print("""
        välj din attack
klicka 1 för att slå med armbågen 20-40 skada
klicka 2 för att kassta stark sås 50% chans att lyckas 40-60 skada
klicka 3 för att hoppa från en byggnad med armbågen 25% chans att lyckas 45-100 skada"""))
     if joaquin_attack_val == "1":
          joaquin_armbåg_skada = random.randint (20, 40)
          spelare2_liv -= joaquin_armbåg_skada
          print("Du tog " + str(joaquin_armbåg_skada) + " skada på spelare 2 har " + str(spelare2_liv) + " liv kvar")


if joaquin_attack_val == "2":
        for_joaquin_sås = random.randint (1, 2)
        if for_joaquin_sås == 1:
             print("attacken misslyckades")
        else:
             joaquin_sås_skada = random.randint (40, 60)
        spelare2_liv -= joaquin_sås_skada
        print("du tog " + str(joaquin_sås_skada) + " skada på sperare 2 har " + str(spelare2_liv) + " liv kvar")

if joaquin_attack_val == "3":
     for_joaquin_armbågehopp = random.randint (1, 4)
     if for_joaquin_armbågehopp == 1:
          joaquin_armbåghopp_skada = random.randint (45, 100)
          spelare2_liv -= joaquin_armbåghopp_skada
          print("Du tog " + str(joaquin_armbåghopp_skada) + " skada på spelare 2 har " + str(spelare2_liv) + " liv kvar")
if for_joaquin_armbågehopp != 1:
        print("Attacken Misllyckades")
     
