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

