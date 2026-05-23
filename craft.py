from random import randint
rar=int(input('what rarity would you wish to craft? '))
if rar > 7:
    print("invalid rarity!")
    print("0:common")
    print("1:unusual")
    print("2:rare")
    print("3:epic")
    print("4:legendary")
    print("5:mythic")
    print("6:ultra")
    print("7:super")
amuont=int(input('how many would you with to craft? '))
if rar==0:
    craftChance=64
elif rar==1:
    craftChance=32
elif rar==2:
    craftChance=16
elif rar==3:
    craftChance=8
elif rar==4:
    craftChance=4
elif rar==5:
    craftChance=2
elif rar==6:
    craftChance=1
elif rar==7:
    craftChance=0.1
else:
    craftChance=0
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
print(Craft(amuont, rar))