from skill import Skill
import random

leveldict = {1: 100, 2: 150, 3: 250, 4: 400, 5: 600, 6: 850, 7: 1150, 8: 1500, 9: 2000, 10: 3000}
class Player:
    def __init__(self):
        self.naam = input("Type your name: ")
        self.level = 1
        self.health = 100
        self.mana = 100
        self.totalHealth = 100
        self.totalMana = 100
        self.xp = 0
        self.skillset = []
        self.inventory = []
    def showName(self):
        return self.naam
    def showLevel(self):
        return self.level
    def showHealth(self):
        return self.health
    def showMana(self):
        return self.mana
    def showXp(self):
        return self.xp
    def addXP(self, xpint):
        self.xp = self.xp + xpint
    def getInventory(self):
        return self.inventory
    def getItemStringFromInventory(self, itemstringname):
        for i in self.inventory:
            if itemstringname == i.getName():
                return i.getName()
    def getItemByStringNameFromInventory(self, itemstringname):
        for i in self.inventory:
            if itemstringname == i.getName():
                return i
    def addItemToInventory(self, item):
        self.inventory.append(item)
    def removeFromInventory(self, itemname):
        for i in self.inventory:
            if i.getName() == itemname:
                self.inventory.remove(i)
    def checkLevelUp(self):
        for key, value in leveldict.items():
            if self.showLevel() == key:
                if self.showXp() >= value:
                    xp = self.showXp()
                    remainder = xp - value
                    self.level = self.level +1
                    self.totalHealth = self.totalHealth*1.5
                    self.totalMana = self.totalMana*1.5
                    self.regenToMax()
                    self.xp = 0
                    self.addXP(remainder)
                    print(f"Congratulations you have leveled up to level {self.showLevel()}")
                    print(f"Your level up revitalizes your health and mana! Your health is now {self.showHealth()} and your mana is now {self.showMana()}")
                    break
    def regenToMax(self):
        self.health = round(self.totalHealth)
        self.mana = round(self.totalMana)
    def addSkill(self, skill):
        self.skillset.append(skill)
    def showSkill(self):
        skills = []
        for i in self.skillset:
            skills.append(i.getSkillName())
        return skills
    def useSkill(self):
        skillslist = self.showSkill() # array with all the skills
        skillToUse = input("Which skill do you want to use? ")
        if skillToUse not in skillslist:
            print("Please type a valid skill")
        elif skillToUse in skillslist:
            for i in self.skillset:
                if i.getSkillName() == skillToUse and i.getActiveCD() == 0 and self.showLevel() >= i.getSkillLevel():
                        skilldamage = i.getSkillDamage()
                        attackpower = random.randint(10, skilldamage)
                        if i.getSkillCD() > 0:
                            i.activeCDIsSkillCD()
                        self.mana = self.mana - i.getSkillManaUse()
                        return attackpower
                        break
                elif i.getSkillName() == skillToUse and i.getActiveCD() == 1:
                    print(f"{skillToUse} is on cooldown for {i.getActiveCD()} more turn")
                elif i.getSkillName() == skillToUse and i.getActiveCD() > 1:
                    print(f"{skillToUse} is on cooldown for {i.getActiveCD()} more turns")
                elif self.showLevel() < i.getSkillLevel(): 
                    print(f"Your current level is not high enough to use this abillity")
    def reduceHealth(self, dmg):
        if dmg == None:
            self.health = self.health
        else:
            self.health = self.health - dmg
    def deminishCDs(self):
        for i in self.skillset:
            if i.getSkillCD() > 0 and i.getActiveCD() >= 1:
                i.reduceActiveCD()
