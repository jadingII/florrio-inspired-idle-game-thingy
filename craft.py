from random import randint

def Craft(petals, rarity):
    success = 0

    if rarity==0:
       craftChance=64
    elif rarity==1:
        craftChance=32
    elif rarity==2:
        craftChance=0.16
    elif rarity==3:
        craftChance=0
    elif rarity==4:
        craftChance=0
    elif rarity==5:
        craftChance=0
    elif rarity==6:
        craftChance=0
    elif rarity==7:
        craftChance=0
    if petals < 10000:
        while petals >= 5:
            if randint(1, 1000) <= craftChance*10:
                success += 1
                petals -= 5
            else:
                petals -= randint(1, 4)
    else: # dont want to crash my game from trying to do 2.1e+25b iterations of a while loop
        if rarity == 0:
            success = petals // 7
            petals = randint(1,4)
        elif rarity == 1:
            success = petals // 11
            petals = randint(1,4)
        elif rarity == 2:
            success = petals // 1.9e+3 
            petals = randint(1,4)
        elif rarity == 3:
            success = petals // 3.4e+45
            petals = randint(1,4)
        elif rarity == 4:
            success = petals // 6.5e+90
            petals = randint(1,4)
        elif rarity == 5:
            success = petals // 1.28e+150
            petals = randint(1,4)
        elif rarity == 6:
            success = petals // 2.65e+200
            petals = randint(1,4)
        elif rarity == 7:
            success = petals // 2503e+300
            petals = randint(1,4)
    return success, petals
print(Craft(9999999999999,0))