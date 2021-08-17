import random
from vikingsClasses import Soldier
from vikingsClasses import Viking
from vikingsClasses import Saxon
from vikingsClasses import War

def __init__(self):
    self.vikingArmy = []
    self.saxonArmy = []
    return None

def addViking(self, Viking):
    self.vikingArmy.append(Viking)
    return vikingArmy

def addSaxon(self, Saxon):
    self.saxonArmy.append(Saxon)
    return saxonArmy

def vikingAttack(self):
    self.saxon_rand = random.choice(self.saxonArmy)
        
    self.viking_rand = random.choice(self.vikingArmy)
        
    self.viking_damage = self.saxon_rand.receiveDamage(self.viking_rand.strength)
        
    if self.saxon_rand.health <= 0:
        self.saxonArmy.remove(self.saxon_rand)
        
    return self.viking_damage

def saxonAttack(self):
        
    self.saxon_rand = random.choice(self.saxonArmy)
        
    self.viking_rand = random.choice(self.vikingArmy)
        
    self.saxon_damage = self.viking_rand.receiveDamage(self.saxon_rand.strength)
        
    if self.viking_rand.health <= 0:
        self.vikingArmy.remove(self.viking_rand)
        
    return self.saxon_damage

def showStatus(self):

    if len(self.saxonArmy) == 0:
        return "Vikings have won the war of the century!"
    elif len(self.vikingArmy) == 0:
        return "Saxons have fought for their lives and survive another day..."
    elif len(self.saxonArmy) != 0 and len(self.vikingArmy) != 0:
        return "Vikings and Saxons are still in the thick of battle."
    else:
        return None
