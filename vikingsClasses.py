import random
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, the_damage):
        self.health = self.health - the_damage

    

# Viking


class Viking(Soldier):
    def __init__(self,name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def attack(self):
        return super().attack()

    def receiveDamage(self, the_damage):
         self.health = self.health - the_damage
         if self.health > 0:
             return print(f"{self.name} has received {damage} points of damage")
         else:
             return print(f"{self.name} has died in act of combat")
    def battlecry():
        return print('Odin Owns You All!')
    

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def attack(self):
        return super().attack()

    def receiveDamage(self, the_damage):
        self.health = self.health - the_damage
        if self.health > 0:
            return print(f"A Saxon has received {the_damage} points of damage")
        else:
            return print("A Saxon has died in combat")

        

# War


class War(): 
    def __init__(self):
        self.vikingArmy =[]
        self.Armyaxon = []

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self, Saxon):
        self.Armyaxon.append(Saxon)

    def vikingAttack(self):
        sajon_elegido = random.choice(self.Armyaxon) 
        vikingo_elegido = random.choice(self.vikingArmy)
        resultado_ataque =sajon_elegido.receiveDamage(vikingo_elegido.strength)
        if sajon_elegido.health <= 0:
            self.saxonArmy.remove(sajon_elegido)

        return resultado_ataque

    def saxonAttack(self):
        sajon_elegido = random.choice(self.Armyaxon) 
        vikingo_elegido = random.choice(self.vikingArmy)
        resultado_ataque =vikingo_elegido.receiveDamage(sajon_elegido.strength)
        if vikingo_elegido.health <= 0:
            self.vikingArmy.remove(vikingo_elegido)

        return resultado_ataque

    def showStatus(self):
        saxon_count = self.Armyaxon.count()
        vikingo_count = self.vikingArmy.count()
        if saxon_count == 0:
            return print('Vikings have won the war of the century')
        if vikingo_count == 0:
            return print("Saxons have fought for their lives and survive another day...")
        if saxon_count > 0 or vikingo_count > 0:
            return print('Vikings and Saxons are still in the thick of battle')
    

