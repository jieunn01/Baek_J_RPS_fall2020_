from gameComponents import gameVars, chooseWinner

def compareOptions(choice):

	if (computer == gameVars.player):
		print("tie")

	# alaways check for negative conditions first (the losing case)
	elif (computer == "rock"):
		if (gameVars.player == "scissors"):
			print("you lose!")
			gameVars.player_lives -= 1
		else:
			print("you win!")
			gameVars.ai_lives -= 1

	elif (computer == "paper"):
		if (gameVars.player == "rock"):
			print("you lose!")
			gameVars.player_lives -= 1
		else:
			print("you win!")
			gameVars.ai_lives -= 1

	elif (computer == "scissors"):
		if (gameVars.player == "paper"):
			print("you lose!")
			gameVars.player_lives -= 1
		else:
			print("you win")
			gameVars.ai_lives -= 1

