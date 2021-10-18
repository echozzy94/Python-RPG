from skill import Skill
from player import Player
from enemy import Enemy
from fight import Fight
from item import Item
import random
from colorama import init, Fore, Back, Style

gameisfinished = False

# while gameisfinished == False:

enemylist = ["Goblin", "Ghoul", "Roach", "Deathclaw", "Raider", "Glowing ghoul"]
def select_random_enemy(llist):
    y = len(llist)-1
    number = random.randint(0, y)
    return llist[number]

player = Player()
print(Fore.GREEN + "Welcome " + player.showName() + " to you in the future!" + Style.RESET_ALL)
skill = Skill("bite", "bite the opponent", 30, 5, 0, 0)
skill1 = Skill("punch", "punch the opponent", 20, 5, 0, 0)
skill2 = Skill("fireball", "Conjure a fireball and launch it at the opponent", 75, 30, 2, 0)
skill3 = Skill("chaos fireball", "Conjure a chaos fireball and launch it at the opponent", 120, 75, 5, 2)
item = Item("hp potion", "restores 50 hp when used", 50, 0, 0, 0)
player.addItemToInventory(item)
print(player.getItemStringFromInventory("hp potion"))
player.addSkill(skill)
player.addSkill(skill1)
player.addSkill(skill2)
player.addSkill(skill3)
print(player.showSkill())
enemy = Enemy(select_random_enemy(enemylist), random.randint(1,5))
enemy1 = Enemy(select_random_enemy(enemylist), random.randint(1,5))
enemy2 = Enemy(select_random_enemy(enemylist), random.randint(1,5))
fight = Fight(player, enemy)
fight1 = Fight(player, enemy1)
fight2 = Fight(player, enemy2)
print(fight.encounterMessage())
fight.turnFight()
print(fight1.encounterMessage())
fight2.turnFight()
print(fight2.encounterMessage())
