from random import randint

def Craft(petals, rarity):
    success = 0

    if rarity==0:
       craftChance=64
    elif rarity==1:
        craftChance=32
    elif rarity==2:
        craftChance=16
    elif rarity==3:
        craftChance=8
    elif rarity==4:
        craftChance=4
    elif rarity==5:
        craftChance=2
    elif rarity==6:
        craftChance=1
    elif rarity==7:
        craftChance=0.1

    while petals >= 5:
        if randint(1, 1000) <= craftChance*10:
            success += 1
            petals -= 5
        else:
            petals -= randint(1, 4)
    return success, petals