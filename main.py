# A text based Adventure Game
# Made by 3 Nerds slapping at a keyboard
# Start Date 09/08/2019

# Imports - Many will be added overtime
import time
import random
# <---------------------------->
# <         IMPORTANT          >
# <---------------------------->
# For testing purposes, use the given slp() function
# You can then inside the method change it to always sleep
# for 0 seconds by setting bypassTimesleep to True

def slp(timetoSleepInSeconds):

	# change this to True to enable developer mode
	bypassTimesleep = False
	if bypassTimesleep:
		time.sleep(0)
	else:
		time.sleep(timetoSleepInSeconds)
	

# Global Variables
Name = str(0)
enemy = None
enemy_health = None
enemy_damage = None
#player data
class player:
	health = 100
	maxhealth = 100
	stamina = 100
	maxstamina = 100
	mana = 50
	maxmana = 50 
	level = 0
	strength = 0


#Weapon stats

#Melee weapon stats 
class Generic1stsword:
	mid = 1
	name = "Generic Sword"
	damage = 2 
	stamina = 1
#Magic weapon stats 
class Generic1stspell:
	sid = 1
	name = "Generic Spell"
	damage = 5
	mana = 2
#Ranged weapon stats

#Misc weapon stats

#enemy Stats



#starting area
class slime:
	eid = 1
	name = "GenericSlime"
	health = 6
	damage = 12

class skeleton:
	eid = 2
	name = "GenericSkeleton" 
	health = 10
	damage = 9


print("Welcome to another...")
slp(2)
print("""
   _____                      _                    
  / ____|                    (_)                   
 | |  __  ___ _ __   ___ _ __ _  ___               
 | | |_ |/ _ \ '_ \ / _ \ '__| |/ __|              
 | |__| |  __/ | | |  __/ |  | | (__               
  \_____|\___|_| |_|\___|_|  |_|\___|              
     /\      | |               | |                 
    /  \   __| |_   _____ _ __ | |_ _   _ _ __ ___ 
   / /\ \ / _` \ \ / / _ \ '_ \| __| | | | '__/ _ \\
  / ____ \ (_| |\ V /  __/ | | | |_| |_| | | |  __/
 /_/____\_\__,_| \_/ \___|_| |_|\__|\__,_|_|  \___|
  / ____|                                          
 | |  __  __ _ _ __ ___   ___                      
 | | |_ |/ _` | '_ ` _ \ / _ \                     
 | |__| | (_| | | | | | |  __/                     
  \_____|\__,_|_| |_| |_|\___|
""")
slp(3)
# Notes about how a story works
# Have some dialog, dont jump to asking name n such
# e.g. "Welcome adventurer!"
# "My memory seems to be failing me, what is your name?"
# Something like that

print("Welcome Adventurer!")
slp(2)
print("\nYou emerge from a dreamy sleep in a plain, open field with no memory of how you got there")
slp(2)
Name = input("\nWith this clean slate pick a name to go by \n>>> ")
slp(1)
print("\nBrilliant! fantastic name", Name + "!")

slp(0.5)



















































# Yonas Ugly ass code

"""
startingWeapon = 0
Generic1stChoice = str(input("You see a SWORD and a magic BOOK lying on the ground, which do you choose to pick up? ")).upper()
slp(1)
if Generic1stChoice == "SWORD":
	Generic1stWeapon = Generic1stsword
	print("a good choice you have chosen",Generic1stWeapon.name)
	startingWeapon = 1
if Generic1stChoice == "BOOK":
	Generic1stWeapon = Generic1stspell
	print("ooh a wise choice! you have chosen",Generic1stWeapon.name)
	startingWeapon = 1
while startingWeapon == 0:
	slp(1)
	Generic1stChoice = str(input("You Must chose either SWORD or BOOK! ")).upper()
	if Generic1stChoice == "SWORD":
		slp(1)
		Generic1stWeapon = Generic1stsword
		print("a good choice you have chosen",Generic1stWeapon.name)
		startingWeapon = 1
	if Generic1stChoice == "BOOK":
		slp(1)
		Generic1stWeapon = Generic1stspell
		print("ooh a wise choice! you have chosen",Generic1stWeapon.name)
		startingWeapon = 1		
slp(1)

print("now equip your weapon! you can do this by typing equip (weapon name)!")
command = input()
command = ""

#enemy pool script
enemy = 0
enemy_health = 0
enemy = random.randint(1,2)
if enemy == slime.eid :
	enemy = slime
	enemy_health = enemy.health
	enemy_damage = enemy.damage
elif enemy == skeleton.eid :
	enemy = skeleton
	enemy_health = enemy.health
	enemy_damage = enemy.damage

#battle script
weaponselect = 0 
player_health = player.health
while enemy_health > 0:
	print("\nLookout a", enemy.name , "is coming towards you!")
	slp(1)
	print("\nYou ready your",Generic1stWeapon.name)
	while weaponselect == 0:
		slot1 = str(input("\nweapon name: "))
		if slot1 == Generic1stWeapon.name:
			weaponselect = 1
		else:
			print("\n",slot1, "nis not a valid weapon!")
	slp(1)
	print(enemy.name,"took", Generic1stWeapon.damage , "damage! It now has", enemy_health-Generic1stWeapon.damage , "health left!")
	enemy_health = enemy_health-Generic1stWeapon.damage
	slp(1)
	print(enemy.name, "attacks! you took", enemy_damage, "damage! you now have",player_health-enemy_damage,"health left!")
	player_health = player_health-enemy_damage
	setattr(player,"health",player_health)
weaponselect = 0 
enemy_health = 0
enemy = str(0)
player_health = player.health
print("you leave the battle with",player.health,"health left.")
"""