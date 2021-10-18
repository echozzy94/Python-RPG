class Item:
    def __init__(self, name, description, hp, mana, cd, attack):
        self.name = name
        self.description = description
        self.hp = hp
        self.mana = mana
        self.cd = cd
        self.attack = attack
    def getName(self):
        return self.name
    def getDescription(self):
        return self.description
    def getHP(self):
        return self.hp
    def getMana(self):
        return self.mana
    def getCD(self): # reduce cd of player when item is used
        return self.cd
    def getAttack(self):
        return self.attack
    def useItem(self):
        print(f"You used {self.getName()}")
        