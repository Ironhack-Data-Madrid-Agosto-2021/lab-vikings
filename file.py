from vikingsClasses import Soldier,Viking,Saxon,War
import random

vikingos = ['alejandro','diego','iñigo','jaime']
sajones = ['maria','julian','sonia','sergio']

wars = War()

def teams(vikingos, sajones):
    for x in vikingos:
        x = Viking(x, random.randint(1,100), random.randint(1,50))
        wars.addViking(x)
    for x in sajones:
        x = Saxon(random.randint(1,100), random.randint(1,50))
        wars.addSaxon(x)

teams(vikingos, sajones)

def game():
    while len(wars.vikingArmy) > 0 and len(wars.saxonArmy) > 0:
            print(wars.vikingAttack())
            
            if len(wars.saxonArmy) > 0 :
                print(wars.saxonAttack())
            
            print(wars.showStatus())
        
game()
