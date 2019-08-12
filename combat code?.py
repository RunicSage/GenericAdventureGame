#yonas shitty combat code

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