from vikingsClasses import Soldier, Viking, Saxon, War
import random as rn

max_health_viking = 10
max_strength_vikings = 3
number_vikings = 10

# Saxon are weakers, but there are more of them
max_health_saxon = 8
max_strength_saxon = 2
number_saxons = 11

my_war = War()
def createTeams():
    for i in range(number_vikings):
        #name, health, strength
        my_war.addViking( Viking(f"name {i}", rn.randint(1,max_health_viking), rn.randint(1,max_strength_vikings)))
       
    for i in range(number_saxons):
        #health, strength
        my_war.addSaxon(Saxon( rn.randint(1,max_health_saxon), rn.randint(1,number_saxons)))


def play():
    end = False
    fight = 0 
    while(not end):
        fight += 1
        #Viking attack 
        print(f"Battle number {fight}")
        my_war.vikingAttack()
        print("Vikings Atacking!!")
        

        if len(my_war.saxonArmy) == 0:
            print("vikings win!!!")
            end =True
        else:
            my_war.saxonAttack()
            print("Saxons Atacking!!")
            
            if len(my_war.vikingArmy) == 0:
                print("Saxons win!!!")
                end =True
        print(my_war.showStatus())
        #We only write how are the armys going if it is not the end
        if (not end):
            print(f"------Saxon   are {len(my_war.saxonArmy)}----")
            print(f"------Vikings are {len(my_war.vikingArmy)}----")
#This function will run the game
def run_game():
    createTeams()
    play()


# We ask to the user if he/she wants to play
input_play = input ("Do you wanna play? (y/n):  ")

#We keep asking while we are not receiving an yes(y) or no(no)
while (input_play!= "y" and input_play != "n"  ):
    input_play = input("Pleae insert y or n ")

#If we receive a 'y', we call run_game() function created previously 
if input_play == 'y':
    run_game()
elif input_play == 'n':
    print("You are a coward!!!, When you are ready for the war,just Let me know")


