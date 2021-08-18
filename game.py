import random
from vikingsClasses import War, Viking, Saxon
#import vikingsClasses

# NO EJECUTAR, LOOP INFINITO
# NO EJECUTAR, LOOP INFINITO


names=["Ubin","Hakorn","Iver","Fassolt","Gunnulf","Morg","Krumr"]

def generateViking(x):
    name = random.choice(names)
    strength = random.randint(2,10)
    health = random.randint(9,20)
    x=str(x)
    x =Viking(name,health,strength)
    return x

def generateSaxon(x):
    strength = random.randint(2,10)
    health = random.randint(9,20)
    x= str(x)
    
    x =Saxon(health,strength)
    return x


def battle():
    war = War()
    vikarmy=int(input("How many vikings? "))
    sxsarmy=int(input("How many saxons? "))
    iniciative = input("Who starts attacking? (vikings/saxons)")

    for x in range(vikarmy):
        war.addViking(generateViking(x))
    for x in range(sxsarmy):
        war.addSaxon(generateSaxon(x))
    if iniciative == "vikings":
        f_1 = war.vikingAttack()
        f_2 = war.saxonAttack()
    elif iniciative == "saxons":
        f_1 = war.saxonAttack()
        f_2 = war.vikingAttack()


    while len(war.vikingArmy) >0 and len(war.saxonArmy) >0:
        k=len(war.vikingArmy); s=len(war.saxonArmy)
        print(f_1)
        if len(war.vikingArmy)< k or len(war.saxonArmy) < s:
            print(war.showStatus())
            
        print(f_2)
        if len(war.vikingArmy)< k or len(war.saxonArmy) < s:
            print(war.showStatus())
                    
battle()