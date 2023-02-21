#Specifikācija nav doti visi svarīgie punkti.
#Kāda valūta ir norādītās cenas? Un kādas ir piegādes iespējas.
#Kādā valūtā tiks norādītas cenas un kā tiks uzglabāta pasūtījumu informācija un kā varēs pārbaudīt tās statusu?
import time
import os
def notirit():
    os.system('cls' if os.name=='nt' else 'clear')
def tkrekli():
    notirit()
    time.sleep(0.3)
    cena = 0
    skaits = int(input("Cik daudz kreklu jūs pirksiet?"))
    for i in range(skaits):
        time.sleep(0.3)
        notirit()
        time.sleep(0.5)
        print("Kādu dizainu uz {} kreklu jūs gribat?".format(i+1))
        time.sleep (0.3)
        print("1.Tekstu")
        time.sleep (0.3)
        print("2.Foto")
        time.sleep (0.3)
        print("3.Zime")
        time.sleep (0.3)
        a = 0
        while a not in [1,2,3]:
            try:
                a = int(input("Rakstiet ciparu šeit: "))
                if a not in [1,2,3]:
                    print("Ievadiet pareizi ciparu.")
            except ValueError:
                print("Lūdzu, pareizi ievadiet ciparu.")
        if a == 1:
            cena += 5
        elif a == 2:
            cena += 20
        elif a == 3:
            cena += 7
        dizains = input("Vai jūs vēlaties pievienot vēlvienu dizainu {} kreklam? Atbildiet ar Jā vai Nē. ".format(i+1))
        while dizains == "Jā":
            time.sleep (0.3)
            print("1.Tekstu")
            time.sleep (0.3)
            print("2.Foto")  
            time.sleep (0.3)  
            print("3.Zime")
            time.sleep (0.3)
            b = 0
            while b not in [1,2,3]:
                try:
                    b = int(input("Rakstiet ciparu šeit: "))
                    if b not in [1,2,3]:
                        print("Ievadiet pareizi ciparu.")
                except ValueError:
                    print("Lūdzu, pareizi ievadiet ciparu.")
            time.sleep(0.3)
            if b == 1:
                cena+=5
            elif b == 2:
                 cena += 20
            elif b == 3:
                cena += 7
            dizains = input("Vai jūs vēlaties pievienot vēlvienu dizainu {} kreklam?".format(i+1))
    return cena
cena = tkrekli()
notirit()
piegade = 0
while piegade not in ["Jā","Nē"]:
    try:
        piegade = input("Vai jums ir vajadzīga piegāde. Atbildiet ar tikai Jā vai Nē. ")
        if piegade not in ["Jā","Nē"]:
            print("Ievadiet pareizi atbildi.")
    except ValueError:
        print("Lūdzu, pareizi ievadiet atbildi.")
if piegade == "Jā":
    if cena >= 100:
        print("Tādēļ ka jūsu prece ir virs 100 Eiro, jums ir 5% atlaide")
        time.sleep(0.5)
        print("Jums jāmaksā ir",cena* 0.95)
        exit()
    elif cena <= 50:
        print("Tādēļ ka jūsu prece ir zem 50 Eiro, jums jāmaksā klāt ir 15 Eiro" )
        time.sleep(0.5)
        print("Kopa tas maksās",cena+15,"Eiro")
        exit()
    else:
        print("Jums viss kopa maksās",cena,"EIRO")
        exit()
else:
    print("Jums viss kopa maksās",cena,"Eiro")