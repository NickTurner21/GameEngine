# Character.py
# Thorin Schmidt
# 11/16/2016

'''module that contains classes and functions to run a game'''
<<<<<<< HEAD
import random
from Character import *
from Monster import *

def combat(one, two):
    ''' runs combat bewtween two Characters, one and two'''

    done = False
    while not done:
        # User Actions
        choice = input("""
                  YOU ARE IN COMBAT!
                  What do you want to do?
                  You can:
                     A)ttack
                     H)eal
                     F)lee
                Your Choice: [A/h/f]: """)
        if choice.lower() == "f":
            if one.flee():
                done = True
                print(one.name, "Flees in terror!")
            else:
                print(one.name, "cannot flee!")
        elif choice.lower() == "h":
            one.heal()
        else:
            one.attack(two)

        #Computer AI
        twoChoice = two.combat_choice()
        if twoChoice == 'a':
            two.attack(one)
        if twoChoice == 'h':
            two.heal()
        else:
            two.flee()

        if one.health <= 0 or two.health <= 0:
            done = True

if __name__ == "__main__":
    hero = Character(name = "Mr Something")
    orc = Monster(name='Orcccc')
    combat(hero, orc)
    
'''
    hero.attack(orc)
    orc.attack(hero)

    print(hero.health)
    print(orc.health)

    hero.heal()
    orc.heal()

    print(hero.health)
    print(orc.health)
   ''' 
=======
from random import randint
from character import *
from monster import *

def combat(one, two):
    ''' runs combat between two Characters, named one and two'''

    def take_action(current, target, choice):
        '''handle the current active character's choice

            current is the one doing the action, choice is the chosen action,
            target is the opponent who could be attacked. The function returns
            a Boolean, which indicates whether to end the combat loop.'''
        
        isOver = False
        
        if choice == "f":
            isOver, message = current.flee() #Fleeing ends combat
            
        elif choice == "h":
            success, message = current.heal() #This has no effect on the loop
            
        else:
            success, message = current.attack(target)
            if target.health <= 0:  #combat ends if the enemy dies
                isOver = True
                message += "\n" + target.name + " is Dead!"

        print(message)

        return isOver
        #end of internal function
    
    ''' combat function begins here'''    
    combatIsOver = False
    rounds = 0
    while not combatIsOver:
        rounds +=1
        print("\nRound", rounds, "begins...")
        # 'Init' is short for 'Initiative', got tired of typos - TMS
        oneInit = randint(1, 20) + one.speed
        twoInit = randint(1, 20) + two.speed
        if oneInit >= twoInit:
            combatIsOver = take_action(one, two, one.combat_choice())
            if combatIsOver:
                continue # go directly to beginning of loop
            combatIsOver = take_action(two, one, two.combat_choice())
        else:
            combatIsOver = take_action(two, one, two.combat_choice())
            if combatIsOver:
                continue # go directly to beginning of loop
            combatIsOver = take_action(one, two, one.combat_choice())

def create_player():
    '''  generate a character based on user input

        This function contains several local functions, each using a different
        method of chaaracter creation:
            simple - the user is asked which stat(str, dex, con, int, wis, cha)
                is most important, and which is least.  most important gets
                a value of 17, least gets a 9, and the rest get 12. This method
                is suitable for a 20-point character build using Pathfinder d20
                rules.  This method has only a few choices, and results in
                moderate satisfaction for the user.
            hardcore - results are generated randomly using the 3d6 method, in
                standard stat block sequence: (str, dex, con, int, wis, cha).
                if none of the stats are over 13, then the entire set is re-
                rolled until it does. The user has no control over ability
                scores. This method is the easiest, but usually has the least
                satisfaction for the user.
            4d6, keep best three, arrange to suit - 6 sets of 4d6 are rolled,
                in each set, the top three dice are kept and added together.
                Then these scores are assigned by the user. This method usually
                has the highest satisfaction for the player, but is also the
                most complicated, due to the many choices required.'''

    def simple():
        return Character()

    def hardcore():
        return Character()

    def four_d_six():
        return Character()

    #main menu
    satisfied = False
    while not satisfied:
        valid = False
        while not valid:
            choice = input('''
                             Character Creation Menu
                            -------------------------
                               1) Hardcore
                               2) Simple
                               3) 4d6, Arrange to suit
                               4) Method Descriptions
                            --------------------------
                            Choose [1-4]: ''')
            if choice in ('1','2','3','4'):
                valid = True
            else:
                print("*** Invalid Input! ***\n\n")
        if choice == '4':
            help(create_player)
            continue
        elif choice == '3':
            player = four_d_six()
        elif choice == '2':
            player = simple()
        elif choice == '1':
            player = hardcore()
        else:
            print("***  ERROR - something went wrong here! ***")
        valid = False
        while not valid:
            print(player)
            happyNow = input("Do you wish to play this character?[y/n]? ")
            if happyNow.lower() in ('y', 'n'):
                valid = True
            else:
                print("*** y or n only! ***\n")
        if happyNow == 'y':
            satisfied = True

    return player

if __name__ == "__main__":
    hero = create_player()
    #hero = Character()
    #orc = Monster(name = "Dorque da Orc")

    #combat(hero, orc)

    
>>>>>>> 6e9f6fb52f8a7151af5a2b799990fedaf24c0147
