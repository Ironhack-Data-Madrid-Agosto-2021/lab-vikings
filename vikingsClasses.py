import random
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    def attack(self):
        return self.strength
    def receiveDamage(self, damage):
        self.health -= damage
        return None

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name
    def receiveDamage(self, damage):
        self.health -= damage
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
    def receiveDamage(self, damage):
        self.health -= damage
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
        return None
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)
        return None
    def vikingAttack(self):
        sajon = random.choice(self.saxonArmy)
        vikingo = random.choice(self.vikingArmy)
        accion = sajon.receiveDamage(vikingo.strength)
        if sajon.health <= 0:
            self.saxonArmy.remove(sajon)
        return accion
    def saxonAttack(self):
        sajon2 = random.choice(self.saxonArmy)
        vikingo2 = random.choice(self.vikingArmy)
        accion2 = vikingo2.receiveDamage(sajon2.strength)
        if vikingo2.health <= 0:
            self.vikingArmy.remove(vikingo2)
        return accion2
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.saxonArmy) > 0 and len(self.vikingArmy) > 0:
            return "Vikings and Saxons are still in the thick of battle."

