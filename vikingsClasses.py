

import random as rn
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    def attack(self):
        return self.strength
    def receiveDamage(self, damage):
        self.health -= damage


# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name
    def attack(self):
        return super().attack()
    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    def battleCry(self):
        return "Odin Owns You All!"
    

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
    def attack(self):
        return super().attack()
    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if self.health > 0:
                return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"

# War


class War():
    def __init__(self):
        self.vikingArmy = [] 
        self.saxonArmy = []
    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        saxon_aleatory = rn.choice(self.saxonArmy)
        vinking_aleatory =  rn.choice(self.vikingArmy)
        string_return =  saxon_aleatory.receiveDamage(vinking_aleatory.strength)
        if saxon_aleatory.health <= 0:
            self.saxonArmy.remove(saxon_aleatory)
        return string_return
    def saxonAttack(self):
        saxon_aleatory = rn.choice(self.saxonArmy)
        vinking_aleatory =  rn.choice(self.vikingArmy)
        string_return =  vinking_aleatory.receiveDamage(saxon_aleatory.strength)
        if vinking_aleatory.health <= 0:
                self.vikingArmy.remove(vinking_aleatory)
        return string_return
        
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        if len(self.vikingArmy) == 0:
           return  "Saxons have fought for their lives and survive another day..."
        if len(self.saxonArmy) > 0 and len(self.vikingArmy) >0:
            return "Vikings and Saxons are still in the thick of battle."

