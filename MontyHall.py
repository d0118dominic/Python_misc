# Monty Hall Problem Game
# Use to play out the monty hall problem in the terminal

import numpy as np
import random
import time

doors = [1,2,3]
door_win = random.randint(1,3)


print( 
"""     
               ________     ________     ________
              |        |   |        |   |        |
	      |    1   |   |    2   |   |    3   |
	      |        |   |        |   |        |
	      |      o |   |      o |   |      o | 
	      |        |   |        |   |        |
	      |	       |   |        |   |        |



"""
)


Choice = input("Which door do you choose?       ")

if (((Choice.isnumeric() == True) and (int(Choice) == 1)) or 
   ((Choice.isnumeric() == False) and (str(Choice).lower() == "one"))):
	print("\nYou chose door #" + Choice + ". I will not yet reveal if this is correct!\n")
elif (((Choice.isnumeric() == True) and (int(Choice) == 2)) or 
     ((Choice.isnumeric() == False) and (str(Choice).lower() == "two"))):
 	print("\nYou chose door #" + Choice + ". I will not yet reveal if this is correct!\n")
elif (((Choice.isnumeric() == True) and (int(Choice) == 3)) or 
     ((Choice.isnumeric() == False) and (str(Choice).lower() == "three"))):
 	print("\nYou chose door #" + Choice + ". I will not yet reveal if this is correct!\n")
else:
	print("\nYour answer is invalid. Therefore, you lose. Too bad.\n")


print("I will now reveal one of the doors you didn't choose...\n")

time.sleep(1)



def reveal(n):
	if (n == 1):
		print( 
"""     
              \________/    ________     ________
              |        |   |        |   |        |
	      |        |   |    2   |   |    3   |
	      |        |   |        |   |        |
	      |        |   |      o |   |      o | 
	      |        |   |        |   |        |
	      |________|   |        |   |        |
              /        \    
\n

"""
)
	if (n == 2):
		print( 
"""     
               ________    \________/    ________
              |        |   |        |   |        |
	      |    1   |   |        |   |    3   |
	      |        |   |        |   |        |
	      |      o |   |        |   |      o | 
	      |        |   |        |   |        |
	      |        |   |________|   |        |
                           /        \ 
\n

"""
)
	

	if (n == 3):
		print( 
"""     
               ________     ________    \________/
              |        |   |        |   |        |
	      |    1   |   |    2   |   |        |
	      |        |   |        |   |        |
	      |      o |   |      o |   |        | 
	      |        |   |        |   |        |
	      |        |   |        |   |________|
                                        /        \ 
\n

"""
)



doors.remove(door_win)
if int(Choice) in doors:
	doors.remove(int(Choice))

revealed_door = random.choice(doors)
doors.remove(revealed_door)
reveal(revealed_door)
rev = str(revealed_door)
#norev = str(doors[0])


print("You chose door #" + Choice)
print("We revealed door #" + rev + " was empty")


doors = [1,2,3]
doors = [i for i in doors if (i != revealed_door and  i != int(Choice))]

rem = int(doors[0])
rev = int(rev)
Choice = int(Choice)

# Sanity Check of door variables
#print("Winning door " + str(door_win))
#print("Revealed door " + str(rev))
#print("Choice door " + str(Choice))
#print("Remaining door " + str(rem))

time.sleep(2)

print("\n\n\nIf you'd like, you can change your answer or stick with your original choice.")

time.sleep(2)
switch = input("\n\n\n Do you want to change your answer to door #" + str(rem) + "?           ")
print("\n\n\n")

if ((switch == 'yes' or switch == 'y')):
	print(("You've changed your answer to door #" + str(rem)) + ".")
	switch_choice = rem
elif ((switch == 'no' or switch == 'n')):
	print("Original choice it is, then.")
	switch_choice = Choice
else:
	print("Your answer doesn't compute.  Defaulting to original choice.")
	switch_choice = Choice

time.sleep(1)
print("\n.")
time.sleep(1)
print("\n..")
time.sleep(1)
print("\n...")
time.sleep(1)

if (switch_choice == door_win):
	print("\nYou won!\n")
else:
	print("\nYou lost.\n")




# More later #


# Simulating many rounds #
