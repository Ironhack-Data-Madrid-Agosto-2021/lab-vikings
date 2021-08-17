import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    def attack(self):
        return self.strength
    def receiveDamage(self, damage):
        self.damage = damage
        self.health = health - damage
        


# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name
    def receiveDamage(self, damage):
        self.damage = damage
        self.health = self.health - damage

        if self.health > 0:
            return f"{self.name} has received {self.damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    def battleCry(self):
        return f"Odin Owns You All!"

        


# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health,strength)
    def receiveDamage(self, damage):
        self.damage = damage
        self.health = self.health-damage

        if self.health > 0:
            return f"A Saxon has received {self.damage} points of damage"
        else:
            return f"A Saxon has died in combat"

    

# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
        return None

    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)
        return None

    def vikingAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        Action = saxon.receiveDamage(viking.strength)

        if saxon.health >= 0:
            self.saxonArmy.remove(saxon)
            return Action
    
    def saxonAttack(self):
        Viking_1 = random.choice(self.vikingArmy)
        Saxon_1 = random.choice(self.saxonArmy)
        Action_1 = Viking_1.receiveDamage(saxon.strength)

        if viking.health >= 0:
            self.vikingArmy.remove(viking_1)
            return Action_1

    def showStatus(self):
        if len(self.vikingArmy) == 0:
            return f"Saxons have fought for their lives and survive another day..."
        elif len(self.saxonArmy) == 0:
            return f"Vikings have won the war of the century!"
        else:
            return f"Vikings and Saxons are still in the thick of battle."




    

    




