class Skill:
    def __init__(self, skillname, skilldescription, skilldamage, skillmanause, cdturns, skilllevel):
        self.skillname = skillname
        self.skilldescription = skilldescription
        self.skilldamage = skilldamage
        self.skillmanause = skillmanause
        self.skillcooldown = cdturns
        self.activecooldown = 0
        self.skilllevel =  skilllevel
    def getSkillName(self):
        return self.skillname
    def getSkillDescription(self):
        return self.skilldescription
    def getSkillDamage(self):
        return self.skilldamage
    def getSkillManaUse(self):
        return self.skillmanause
    def getSkillCD(self):
        return self.skillcooldown
    def getSkillLevel(self):
        return self.skilllevel
    def reduceActiveCD(self):
        if self.activecooldown != 0:
            self.activecooldown = self.activecooldown -1
    def activeCDIsSkillCD(self):
        self.activecooldown = self.skillcooldown
    def getActiveCD(self):
        return self.activecooldown


    

