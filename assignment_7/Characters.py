from random  import randint
from Team import *

printActionDescription = True

def dprint(s):
    if printActionDescription:
        print(s)

#Constants for Mage Type        
manaCost = 20
manaRecovery = 30


class Character(object):
    def __init__(self):
        self.name = ''
        self.maxhp = 1000
        self.hp = 1000
        self.str = 0
        self.maxmana = 0
        self.mana = 0
        self.cost = 9999999999
        self.alive = True

    def act(self,myTeam,enemy):
        return

    def gotHurt(self,damage):
        if damage >= self.hp:
            self.hp = 0
            self.alive = False
            dprint(self.name + ' died!')
        else:
            self.hp -= damage
            dprint(self.name +
                   f' hurt with remaining hp {self.hp}.')


class Fighter(Character):
    def __init__(self):
        super().__init__() ##character variables will be overwritten with parent variables after this line
        self.name = 'Fighter' ##overwrite them as follow
        self.maxhp = 100
        self.hp = 100
        self.str = 100
        self.cost = 100

    def act(self,myTeam,enemy):
        target = randAlive(enemy)
        dprint(f'Hurt enemy {target} by damage {self.str}.')
        enemy[target].gotHurt(self.str)
  

class Mage(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Mage'
        self.maxmana = 50
        self.mana = 50
        self.maxhp = 800
        self.hp = 800
        self.cost = 200
        self.int = 400

    def cast(self,myTeam,enemy):
        self.mana -= manaCost
        target = randAlive(enemy)
        dprint(f'Strike enemy {target} with spell')
        enemy[target].gotHurt(self.int)
        
    def act(self,myTeam,enemy):
        if self.mana < manaCost:
            self.mana += manaRecovery
            dprint(f'Mana recover to {self.mana}.')
        else:
            self.cast(myTeam,enemy)
   
    ## create more classes in here

class Berserker(Fighter):
    def __init__(self):
        super().__init__()
        self.name = 'Berserker'
        self.cost = 200

    def act(self,myTeam,enemy):
        if self.hp <= (self.maxhp//2):                          # if current HP is < 50% of maxHP
            self.str *= 2                                       # double str
            dprint('Berserk mode! Attack double!')
            super().act(myTeam,enemy)                           # normal attack
        else:
            self.str = 100
            super().act(myTeam,enemy)                           #else, str = 100 and normal attack


class ArchMage(Mage):
    def __init__(self):
        super().__init__()
        self.name = 'ArchMage'
        self.cost = 600

    def cast(self,myTeam,enemy):
        dead_members = 0afvgfa
        for i in myTeam:
            if not i.alive:                                     # check how many team members are dead
                dead_members += 1                               # add dead_member counter
        if len(myTeam) - dead_members == 1:                     # if there is only 1 alive team member
            if myTeam[randAlive(myTeam)].name == 'ArchMage':    # check if the member name is Archmage
                self.int *= 2
                for index, foe in enumerate(enemy):
                    if foe.alive == True:                       # if foe is alive, inflict massive damage !
                        dprint(f'Cast KABOOOOOOM ! (Damage {self.int}) to every enemy!')
                        enemy[index].gotHurt(self.int)
        else:                                                   # normal casting if there is at least > 1 Alive
            super().cast(myTeam,enemy)

    def act(self,myTeam,enemy):
        if self.mana < manaCost:
            self.mana += manaRecovery
            dprint(f'Mana recover to {self.mana}.')
        else:
            self.cast(myTeam,enemy)


class Necromancer(Mage):
    def __init__(self):
        super().__init__()
        self.name = 'Necromancer'
        self.cost = 400

    def cast(self, myTeam, enemy):
        if not allAlive(myTeam):                                # check allAlive returns False
            self.mana -= manaCost
            target = randDeath(myTeam)                          # returns the random dead member
            myTeam[target].alive = True                          # set the target's Alive = True
            myTeam[target].hp = myTeam[target].maxhp // 2       # set the target's HP to 50% of maxHP
            dprint(f'Reviving member {myTeam[target].name} with hp {myTeam[target].hp}.')
        else:
            super().cast(myTeam,enemy)                          # if allAlive is True, normal casting

    def act(self,myTeam,enemy):
        if self.mana < manaCost:
            self.mana += manaRecovery
            dprint(f'Mana recover to {self.mana}.')
        else:
            self.cast(myTeam,enemy)