# Simple choice between 2 doors.  User chooses.  There's only ONE correct answer for no particular reason.

#print ("Which door do you choose?")



print( 
"""     
               _________     ________
              |         |   |        |
	      |   1     |   |  2     |
	      |         |   |        |
	      |       o |   |      o |
	      |         |   |        |
	      |	        |   |        |



"""
)

Choice = input("Which door do you choose?       ")
if (((Choice.isnumeric() == True) and (int(Choice) == 1)) or 
   ((Choice.isnumeric() == False) and (str(Choice).lower() == "one"))):
	print("You win.  Good job!")

elif (((Choice.isnumeric() == True) and (int(Choice) == 2)) or 
     ((Choice.isnumeric() == False) and (str(Choice).lower() == "two"))):
 	print("You lose, loser.")
else:
	print("Your answer is invalid. Therefore, you lose. Too bad.")

