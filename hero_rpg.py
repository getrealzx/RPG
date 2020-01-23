#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

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
        enemy.health -= self.power



class Hero(Character):
    # def __init__(self, health, power):
    #     self.health = health
    #     self.power = power
    
    def print_damage(self,enemy):
            print(f"You do {self.power} damage to the goblin.")
            if enemy.health <= 0:
                print("The goblin is dead.")

    def print_status(self):
        print(f"You have {self.health} health and {self.power} power.")


    

class Goblin(Character):
    # def __init__(self, health, power):
    #     self.health = health
    #     self.power = power

    def print_damage(self,enemy):
        print(f"{self.name} do {self.power} damage to the you.")
        if enemy.health <= 0:
            print("You are dead")

    def print_status(self):
        print(f"The {self.name} has {self.health} health and {self.power} power.")

class Zombie(Goblin):
    def __init__(self,name,health,power):
        self.name = name
        self.health = abs(health)


hero = Hero("hero",5,2)
goblin = Goblin("goblin",6,2)
zombie = Zombie("zombie",2,1)


def main():

    while goblin.alive() and hero.alive():
        # print(f"You have {hero.health,} health and {hero.power} power.")
        hero.print_status()
        # print(f"The goblin has {goblin.health} health and {goblin.power} power.")
        goblin.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. attach zombie")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # # Hero attacks goblin
            # goblin.health -= hero.power
            # print("You do {} damage to the goblin.".format(hero.power))
            # if goblin.health <= 0:
            #     print("The goblin is dead.")
            hero.attack(goblin)
            hero.print_damage(golblin)


        elif raw_input == "2":
            hero.attack(zombie)
            hero.print_damage(zombie)


        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print(f"Invalid input {raw_input}")

        if goblin.health > 0:
            # Goblin attacks hero
            hero.health -= goblin.power
            print(f"The goblin does {goblin.power} damage to you.")
            if hero.health <= 0:
                print("You are dead.")

main()





