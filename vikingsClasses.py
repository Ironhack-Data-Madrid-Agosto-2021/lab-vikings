
# Soldier
import random

class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= self.damage

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health, strength)
    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= self.damage

        if self.health > 0:
            return f"{self.name} has received {self.damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

    def battleCry(self):
        return "Odin Owns You All!"

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= self.damage

        if self.health > 0:
            return f"A Saxon has received {self.damage} points of damage"
        else:
            return f"A Saxon has died in combat"

# War


class War:

    def __init__(self):

        self.vikingArmy = []
        self.saxonArmy = []
        return None

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
        return None

    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)
        return None

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
        else :
            return None
        
