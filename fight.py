from colorama import Fore, Back, Style
class Fight:
    def __init__(self, Player, Enemy):
        self.player = Player
        self.enemy = Enemy
    def encounterMessage(self):
        encounterstring = f"Uh oh! You encountered a level {self.enemy.getLevel()} {self.enemy.getName()} with {self.enemy.getHealth()} health! \n"
        return encounterstring
    def showHealth(self):
        healthstring = f"Your health is: {Fore.GREEN}{self.player.showHealth()}{Style.RESET_ALL}, your mana is: {Fore.BLUE}{self.player.showMana()}{Style.RESET_ALL}, the health of your opponent: {self.enemy.getName()} is: {Fore.RED}{self.enemy.getHealth()}{Style.RESET_ALL} \n"
        return healthstring
    def turnFight(self):

        while self.enemy.getHealth() >=0 and self.player.showHealth() >=0: #while both player and enemy are alive
            dmg = self.player.useSkill()
            if dmg != None:
                self.enemy.reduceHealth(dmg)
                print(f"You attack {self.enemy.getName()} for {Fore.RED}{dmg}{Style.RESET_ALL} damage! \n")
                self.player.deminishCDs()
                enemyhealth = self.enemy.getHealth()
                print(self.showHealth())
                edmg = self.enemy.attack()
                self.player.reduceHealth(edmg)
                playerhealth = self.player.showHealth()
                print(self.showHealth())
            #If enemy dies
            if self.enemy.getHealth() <=0:
                print(f"You have defeated {self.enemy.getName()}")
                print(f"{self.player.showName()} gained {Fore.YELLOW}{self.enemy.getXP()}{Style.RESET_ALL} experience points")
                self.player.addXP(self.enemy.getXP())
                self.player.checkLevelUp()
                print(f"Your total experience on level {self.player.showLevel()} is now {Fore.YELLOW}{self.player.showXp()}{Style.RESET_ALL}")
                self.player.deminishCDs()
                break
            #if player dies
            if self.player.showHealth() <= 0:
                print(f"{Fore.RED}You have died... This is where your journey ends{Style.RESET_ALL}")
                break
        


            

