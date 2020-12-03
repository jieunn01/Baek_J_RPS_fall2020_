from gameComponents import gameVars

# define win or lose function
def winOrlose(status):

	print("You", status, "! Would you like to try again?")
	choice = input("Y / N : ")

	if choice == "N" or choice == "n":
		print("You chose to quit! Better luck next time!")
		exit()

	elif choice == "Y" or choice == "y":
		# reset the player lives and the AI livves
		# and set player to False so that our loop will restart
		global player_lives
		global ai_lives
		global player

		gameVars.player_lives = 5
		gameVars.ai_lives = 5
		gameVars.player = False

	else:
		print("Make a valid choice - Y or N")
		# this will generate a bug that we need to fix later
		choice = input("Y / N : ")