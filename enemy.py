import random
class Enemy:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.health = self.level + random.randint(10, 50) * self.level
        self.attackdmg = random.randint(0, round(self.health/10))
        self.xp = random.randint(0, self.health*4)
    def getName(self):
        return self.name
    def getHealth(self):
        return self.health
    def getAttackdmg(self):
        return attackdmg
    def getXP(self):
        return self.xp
    def getLevel(self):
        return self.level
    def attack(self):
        a = random.randint(0, self.attackdmg)*self.level
        print(f"{self.getName()} attacks you for {a} damage!")
        return a
    def reduceHealth(self, dmg):
        if dmg == None:
            self.health = self.health
        else:
            self.health = self.health - dmg
    def die(self):
        print("UGHHHH")


