#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee
from random import randint


class Character:
    def __init__(self,health, power):
        self.health = health
        self.power = power

    def alive(self):
        return self.health > 0

        


    def attack(self,enemy):
        # generate increase of probability with evade points, close to 100%

        e = self.evade
        n = randint(0,e+20)
        if n < e:
            evade_p=0
            print("Luckily, you just avoided enemy's attack")
        else:
            evade_p=1
        
        your_injury = enemy.power-self.armor



        #20% chance of double damage
        n = randint(0,10)
        if n<=1:
            P=1
            print("Luckily, you just made DOUBLE DAMGE this round")
        else:
            P=0

        your_damage = (1+P)*self.power        

        if enemy.name=="zombie":

            enemy.health -= your_damage
            self.health -= (your_injury*evade_p)

        #generate 20% of chance:
        elif enemy.health >0:
            n = randint(0,10)
            if n<=1:
                P=1
            else:
                P=0

            if enemy.name=="medic":
                n = randint(0,10)
                if n<=1:
                    P=1
                    print("Your health just increased 2 by the medic")
                else:
                    P=0
                self.health += P*2
                your_damage = 0
                print("The medic is your friend, you don't want hurt him")

            if enemy.name=="shadow":
                n = randint(0,10)
                if n==1:
                    P=1
                    print("You hit shadow, which is not easy!")
                else:
                    P=0
                    print("The shadow just dodged your attack!")
                your_damage = P*your_damage
                enemy.health -= your_damage
                self.health -= (your_injury*evade_p)

            if enemy.name=="backhole":
                n = randint(0,10)
                if n<=5:
                    enemy.health += your_damage
                    print(f"The {enemy.name} increased health by {your_damage}.")
                if n>=6:
                    enemy.health -= 2*your_damage
                    print(f"The {enemy.name} got doubled {your_damage}.")
                else:
                    enemy.health -= your_damage
                self.health -= (your_injury*evade_p)
            
            if enemy.name=="master":
                n = randint(0,100)
                if n<=4:
                    self.health -= (your_injury*evade_p)
                self.power = 1.2*self.power
    
            else:
                enemy.health -= your_damage


            if enemy.health < 1:
                self.coin += enemy.bounty
                print(f"The {enemy.name} is dead, you get {enemy.bounty} coins.")

        print(f"\nYou make {your_damage} damage to {enemy.name}.")
        print(f"The {enemy.name} does {your_injury} damage to you.")
        
        if self.health < 1:
            print("You are DEAD!! :'( )")
    
    def print_status(self):
        if self.name == "hero":
            print(f"You have {self.health} health and {self.power} power with {self.armor} armor and {self.evade} evade .You have {self.coin} coins. ")
        else:
            print(f"The {self.name} has {self.health} health and {self.power} power, the bounty is {self.bounty}")            


class Hero(Character):
    def __init__(self, health, power):
        self.name = "hero"
        self.coin = 5
        self.armor = 0
        self.evade = 2
        super(Hero, self).__init__(health, power)

    def buy(self,item):
        if hero.coin <= 0:
            print("You don't have enough coins to make any purchase. ")
        else:
            self.coin -=item.cost
            item.apply(self)

class Goblin(Character):
    def __init__(self, health, power):
        self.name = "goblin"
        self.bounty = 2
        super(Goblin, self).__init__(health, power)
class Zombie(Character):
    def __init__(self,health,power):
        self.name = "zombie"
        self.bounty =10
        super(Zombie, self).__init__(health, power)
class Medic(Character):
    def __init__(self,health,power):
        self.name = "medic"
        self.bounty = 0
        super(Medic, self).__init__(health, power)
class Shadow(Character):
    def __init__(self,health,power):
        self.name = "shadow"
        self.bounty =5
        super(Shadow, self).__init__(health, power)
class Blackhole(Character): # it has 60% of chance to convert attack to its health, and 40% chance recieve double damage
    def __init__(self,health,power):
        self.name = "blackhole"
        self.bounty = 3
        super(Blackhole, self).__init__(health, power)
class Master(Character): # you chance of getting hurt is 5%, but gain power 20% each time
    def __init__(self,health,power):
        self.name = "master"
        self.bounty = 0
        super(Master, self).__init__(health, power)   

hero = Hero(8,2)
goblin = Goblin(8,2)
zombie = Zombie(2,1)
medic = Medic(8,0)
shadow = Shadow(1,4)
blackhole = Blackhole(5,2)
master = Master(7,9)

class SuperTonic:
    def __init__(self):
        self.cost = 5
        self.name = "tonic"
    def apply(self, character):
        character.health += 10
        print(f"{hero.name}'s health increased to {hero.health}.")

class Sword:
    def __init__(self):
        self.cost = 10
        self.name = 'sword'
    def apply(self, hero):
        hero.power += 2
        print(f"{hero.name}'s power increased to {hero.power}.")

class Armor:
    def __init__(self):
        self.cost = 2
        self.name = 'armor'
    def apply(self,hero):
        hero.armor += 2
        print(f"{hero.name}'s armor increased to {hero.armor}.")

class Evade:
    def __init__(self):
        self.cost = 2
        self.name = 'evade'
    def apply(self,hero):
        hero.evade += 2
        print(f"{hero.name}'s evade increased to {hero.evade}.")


class Store:
    tonic = SuperTonic()
    evade = Evade()
    sword = Sword()
    armor = Armor()
    items = [tonic, sword, armor, evade]


    def do_shopping(self, hero):

        while True:
            print("=====================")
            print("Welcome to the store!")
            print("=====================")
            print(f"You have {hero.coin} coins.")
            print("What do you want to do?")
            for i in range(len(Store.items)):
                item = Store.items[i]
                print(f"{i + 1,}. buy {item.name} for ({item.cost}) coins. ")
            print("10. leave")
            # print(Store.items[0].name)
            raw_input = int(input("> "))
            if raw_input == 10:
                break
            else:
                hero.buy(Store.items[raw_input - 1])
    

def main():
    store = Store()
    while hero.alive() and (zombie.alive() or goblin.alive() or shadow.alive() or blackhole.alive() or master.alvie()):
        hero.print_status()
        goblin.print_status()
        zombie.print_status()
        medic.print_status()
        shadow.print_status()
        blackhole.print_status()
        print()
        print("What do you want to do?\n\n"
        "1. fight goblin\n"
        "2. attack zombie\n"
        "3. attack shadow\n"
        "4. attack blackhole\n"
        "m. get medic\n"
        "s. go to store to purchase\n"
        "f. flee\n"
        "> ", end=' ')
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
            if goblin.health <=0:
                print("The shadow is dead already, don't waste your energy!")
            else:
                hero.attack(shadow)

        elif raw_input == "4":
            if blackhole.health <=0:
                print("The blackhole is dead already, don't waste your energy!")
            else:
                hero.attack(blackhole)

        elif raw_input == "m":
            #get medic
            hero.attack(medic)

        elif raw_input == "s":
            #purchase item
            store.do_shopping(hero)

        elif raw_input == "f":
            print("Goodbye.")
            break

        else:
            print(f"Invalid input {raw_input}")



main()





