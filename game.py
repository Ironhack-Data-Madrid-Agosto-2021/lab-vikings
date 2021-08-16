import random
#from vikingsClasses import Viking
import vikingsClasses
# NO EJECUTAR, LOOP INFINITO

names=["Ubin","Hakorn","Iver","Fassolt","Gunnulf","Morg"]

def generateViking(x):
    vk="viking_"+str(x)
    name = random.choice(names)
    strength = random.randint(2,10)
    health = random.randint(9,20)

    vk=vikingsClasses.Viking(name,health,strength)
    return vk

def generateSaxon(x):
    sx="saxon_"+str(x)
    strength = random.randint(2,10)
    health = random.randint(9,20)

    sx=vikingsClasses.Saxon(health,strength)
    return sx

def battle():
    war = vikingsClasses.War()
    vikarmy=int(input("How many vikings? "))
    sxsarmy=int(input("How many saxons? "))
    iniciative = input("How starts attacking? (vikings/saxons)")

    for x in range(vikarmy):
        war.addViking(generateViking(x))
    for x in range(sxsarmy):
        war.addSaxon(generateSaxon(x))
    if iniciative == "vikings":
        f_1 = vikingsClasses.War.vikingAttack
        f_2 = vikingsClasses.War.saxonAttack
    elif iniciative == "saxons":
        f_1 = vikingsClasses.War.saxonAttack
        f_2 = vikingsClasses.War.vikingAttack


    while len(war.vikingArmy) >0 and len(war.saxonArmy):
        k=len(war.vikingArmy); s=len(war.saxonArmy)
        print(f_1)
        print(f_2)
        if len(war.vikingArmy)< k or len(war.saxonArmy) < s:
            print(vikingsClasses.War.showStatus)
        

battle()