#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee
import random


class Character:
    def __init__(self, name,health, power):
        self.name = name
        self.health = health
        self.power = power

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def attack(self,enemy):

        if enemy.name=="zombie":
            self.health -= enemy.power
            your_damage = enemy.power
            enemy.health -= your_damage




        #generate 20% of chance:
        elif enemy.health >0:
            n = random.randint(0,1)
            if n<=1:
                P=1
            else:
                P=0

            your_damage = (1+P)*self.power



            
            if enemy.name=="medic":
                self.health += P*2
                your_damage = 0

            if enemy.name=="shadow":
                n = random.randint(0,10)
                # if m = 1:
                if n==1:
                    P=1
                else:
                    P=0
                your_damage = P*self.power
                enemy.health -= your_damage
                print(your_damage)

            else:
                enemy.health -= your_damage
            
            # self.health -= enemy.power



        elif enemy.health < 1:
            print(f"The {enemy.name} is dead.")

        print(f"You make {your_damage} damage to {enemy.name}.")
        print(f"The {enemy.name} does {enemy.power} damage to you.")
        
        if self.health < 1:
            print("You are dead")
    


class Hero(Character):
    def print_status(self):
        print(f"You have {self.health} health and {self.power} power.")

class Goblin(Character):
    def print_status(self):
        print(f"The {self.name} has {self.health} health and {self.power} power.")

class Zombie(Goblin):
    def __init__(self,name,health,power):
        self.name = name
        self.health = health
        self.power = power

class Medic(Goblin):
    def __init__(self,name,health,power):
        self.name = name
        self.health = health
        self.power = power

class Shadow(Goblin):
    def __init__(self,name,health,power):
        self.name = name
        self.health = health
        self.power = power


hero = Hero("hero",8,2)
goblin = Goblin("goblin",8,2)
zombie = Zombie("zombie",2,1)
medic = Medic("medic",8,0)
shadow = Shadow("shadow",1,4)

def main():

    while hero.alive() and (zombie.alive() or goblin.alive()):
        # print(f"You have {hero.health,} health and {hero.power} power.")
        hero.print_status()
        # print(f"The goblin has {goblin.health} health and {goblin.power} power.")
        goblin.print_status()
        zombie.print_status()
        medic.print_status()
        shadow.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. attack zombie")
        print("3. get medic")
        print("4. attack shadow")
        print("5. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
        # Hero attacks goblin
            if goblin.health <=0:
                print("The goblin is dead already, don't waste your energy!")
            else:
                hero.attack(goblin)

        elif raw_input == "2":
        # Hero attacks Zombie
            hero.attack(zombie)

        elif raw_input == "3":
            #get medic
            hero.attack(medic)

        elif raw_input == "4":
            if goblin.health <=0:
                print("The shadow is dead already, don't waste your energy!")
            else:
                hero.attack(shadow)

        elif raw_input == "5":
            print("Goodbye.")
            break

        else:
            print(f"Invalid input {raw_input}")



main()





