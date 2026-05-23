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
def craft(petals, success_chance):
    success = 0

    while petals >= 5:
        if randint(1, 1000) <= success_chance*10:
            success += 1
            petals -= 5
        else:
            petals -= randint(1, 4)
    return success, petals
print(craft(2503,.1))