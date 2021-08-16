
# Soldier


import random


class Soldier():
    def __init__ (self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength
   
    def receiveDamage(self,damage):
        self.damage = damage
        self.health -= damage

        

# Viking


class Viking(Soldier):

    def __init__ (self, name, health, strength):
        super().__init__ (health, strength)
        self.name = name 
    
    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= damage

        if self.health <= 0:
            return f'{self.name} has died in act of combat'
        elif self.health > 0:
            return f'{self.name} has received {self.damage} points of damage'
    
    def battleCry(self):
        return 'Odin Owns You All!'


# Saxon


class Saxon(Soldier):
    def __init__ (self, health, strength):
        super().__init__ (health, strength)

    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= damage

        if self.health <= 0:
            return 'A Saxon has died in combat'
        elif self.health > 0:
            return f'A Saxon has received {self.damage} points of damage'

        

# War


class War():
    def __init__ (self):
        self.vikingArmy = []
        self.saxonArmy = []
    
    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        damageToSaxon = saxon.receiveDamage(viking.attack())
        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
            return 'A Saxon has died in combat'
        else:
            return f'A Saxon has received {viking.attack()} points of damage'
            
    def saxonAttack(self):
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        damageToViking = viking.receiveDamage(saxon.attack())
        if viking.health <= 0:
            self.vikingArmy.remove(viking)
            return f'{viking.name} has died in combat'
        else:
            return f'{viking.name} has received {saxon.attack()} points of damage'

    def showStatus(self):
        if len(self.vikingArmy) == 0:
            return 'Saxons have fought for their lives and survive another day...'
        elif len(self.saxonArmy) == 0:
            return 'Vikings have won the war of the century!'
        else:
            return 'Vikings and Saxons are still in the thick of battle.'
