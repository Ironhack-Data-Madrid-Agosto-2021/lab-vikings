from vikingsClasses import Soldier, Viking, Saxon, War
import random

# INTENCION: defino una nueva lista donde estan los saxon y los vikings juntos y pelean a todos contra todos y a ver quien gana

class FreeForAll():
    def __init__(self):
        self.all_soldiers = []

    def addVikingToAll(self, Viking):
        self.all_soldiers.append(Viking)
    def addSaxonToAll(self, Saxon):
        self.all_soldiers.append(Saxon)
    
    #ahora ya tenemos dentro de una misma lista a los Saxons y a los Vikings

    #ahora en base a cada ataque, random, contra random (como en el lab original), se enfrentaran hasta que solo quede uno en pie
    # por ello hago un while loop hasta que la len de la lista de todos sea 1, mientras sea mayor, los soldados se pegan en combate
    # en el momento que sea 1, me va a retornar quien es el ultimo que queda en pie, el ultimo de la lista de all_soldiers.

    def randomAttacks(self):
        attacker1 = random.choice(self.all_soldiers)
        attacker2 = random.choice(self.all_soldiers)
        while len(self.all_soldiers) > 1:
            if attacker1 is Viking and attacker2 is Saxon:
                Saxon.receiveDamage(Viking.attack())
                if Saxon.health is <= 0:
                    return 'A Saxon has died in combat'
                    self.all_soldiers.remove(Saxon)
                else:
                    return f'A Saxon has received {Viking.attack} points of damage'
            elif attacker1 is Viking and attacker2 is Viking:
                Viking.receiveDamage(Viking.attack())
                if Viking.health is <= 0:
                    return f'{Viking.name} has died in combat'
                    self.all_soldiers.remove(Viking)
                else:
                    return f'{Viking.name' received {Saxon.attack} points of damage'
            elif attacker1 is Saxon and attacker2 is Viking:
                Viking.receiveDamage(Saxon.attack())
                if Viking.health is <= 0:
                    return f'{Viking.name} has died in combat'
                    self.all_soldiers.remove(Viking)
                else:
                    return f'{Viking.name' received {Saxon.attack} points of damage'
            elif attacker1 is Saxon and attacker2 is Saxon:
                Saxon.receiveDamage(Saxon.attack())
                if Saxon.health is <= 0:
                    return 'A Saxon has died in combat'
                    self.all_soldiers.remove(Saxon)
                else:
                    return f'A Saxon has received {Viking.attack} points of damage'
        return f'The las man standing is {all_soldiers[0]}'
        

        

        # NO SE POR QUE SE ME QUEDA EL CODIGO DE ESTA MANERA A PARTIR DE LA LINEA 35 (aprox), CON LOS ERRORES QUE NO ENTIENDO 

        # Aun asi, la idea permanece, se pegan todos contra todos, si uno muere se quita de la lista, 
        # y siempre nos sale un return con el daño reibido
        


        

