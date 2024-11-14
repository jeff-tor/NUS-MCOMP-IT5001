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

    def gotRev(self):
        self.alive = True
        self.hp = self.maxhp // 2
        dprint(f'Reviving member {self.name} with hp {self.hp}.')


class Fighter(Character):
    def __init__(self):
        super().__init__() ##character variables will be overwritten with parent variables after this line
        self.name = 'Fighter' ##overwrite them as follow
        self.maxhp = 1200
        self.hp = 1200
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
        if self.hp <= (self.maxhp//2):
            self.str *= 2
            dprint('Berserk mode! Attack double!')
            super().act(myTeam,enemy)
        else:
            self.str = 100
            super().act(myTeam,enemy)

class ArchMage(Mage):
    def __init__(self):
        super().__init__()
        self.name = 'ArchMage'
        self.cost = 600

    def cast(self,myTeam,enemy):
        if allDead(myTeam):
            self.int *= 2
            for i in enemy:
                if allAlive(i):
                    dprint(f'Cast KABOOOOOOM ! (Damage {self.int}) to every enemy!')
                    enemy[i].gotHurt(self.int)
        else:
            super().cast(myTeam,enemy)

    def act(self,myTeam,enemy):
        super().act(myTeam,enemy)

class Necromancer(Mage):
    def __init__(self):
        super().__init__()
        self.name = 'Necromancer'
        self.cost = 400

    def cast(self, myTeam, enemy):
        if not allAlive(myTeam):
            self.mana -= manaCost
            target = randDeath(myTeam)
            myTeam[target].gotRev()

    def act(self,myTeam,enemy):
        super().act(myTeam,enemy)