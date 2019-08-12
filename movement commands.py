#player movement script

#player stats
stamina = 10
#current player location
x = 0
y = 0

#movement commands
north = y + 1
south = y - 1
east = x + 1
west = x - 1
while 
    command = input("what way to you want to move? ")
    if command == "north":
        north
        stamina = stamina - 1
    if command == "south":
        south
        stamina = stamina - 1
    if command == "east":
        east
        stamina = stamina - 1
    if command == "west":
        west
        stamina = stamina - 1
    else:
        print(command, "is not a valid option. valid options are north south east and west.")
    print("you are now at location",x,y)