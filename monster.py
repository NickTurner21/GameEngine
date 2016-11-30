# Monster.py
# Nicholas Turner
# 11/16/2016

'''Monster Package'''
from Character import *
from random import randint
class Monster(Character):
    def __init__(self, name = "Average Joe", maxHealth = 100,
                 speed = 25, stamina = 25, strength = 10,
                 intelligence = 10, dexterity = 10,
                 inventory = [["potion", 2],["Leather", 1]],
                 aggression = 50, awareness = 50, morale = 50):
        super(Monster, self).__init__(name, maxHealth, speed,
                  stamina, strength, intelligence, dexterity,
                  inventory)
        self.aggression = aggression
        self.awareness = awareness
        self.morale = morale

        self.attack_chance = randint(1,100) + aggression
        self.heal_chance = randint(1,100) + awareness
        self.flee_chance = randint(1,100) - morale
    def combat_choice(self):
        ac = self.attack_chance
        hc = self.heal_chance
        fc = self.flee_chance
        if ac > fc and hc:
            combatChoice = 'a'
        elif hc > ac and hc:
            combatChoice = 'h'
        elif fc > ac and hc:
            combatChoice = 'f'
        else:
            combatChoice = 'a'

        return combatChoice

        
if __name__ == "__main__":
    Grr = Monster()
