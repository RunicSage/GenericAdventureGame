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