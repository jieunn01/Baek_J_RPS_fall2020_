#import packages to extend python just like we extend sublime, or Atom, or VSCode)
from random import randint
from gameComponents import gameVars, chooseWinner

# define a win or lose function

# this is the player choice
# player = input("Choose rock, paper or scissors: ")

while gameVars.player == False:
	print("===================*/ RPS GAME */=====================")
	print("computer Lives: ", gameVars.ai_lives,"/", gameVars.total_lives)
	print("Player Lives: ", gameVars.player_lives, "/", gameVars.total_lives)
	print("======================================================")

	print("Choose your weapon! or type quit to exit\n") #\n : New line

	gameVars.player = input("Choose rock, paper or scissors: \n")
	# player = True ( it has value rock, paper, scissors) False 

	# if the palyer chose to quit, then exit the game
	if gameVars.player =="quit":
		print("you chose to quit")
		exit()


	# this will be the Ai choice -> random 
	computer = gameVars.choices[randint(0,2)]

	# check to see what the users input

	# print outputs whatever is in the round brackets -> in this case it outputs player to the command prompt window
	print("user chose: " + gameVars.player)

	# validate thate the random choice worked
	print("AI chose: " + computer)


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

	if gameVars.player_lives == 0:
		chooseWinner.winOrlose("lost")

	if gameVars.ai_lives == 0:
		chooseWinner.winOrlose("won")

		# print("You won! Would you like to try again?")
		# choice = input("Y / N : ")

		# if choice == "N" or choice == "n":
		# 	print("You chose to quit! Better luck next time!")
		# 	exit()

		# elif choice == "Y" or choice == "y":
		# 	# reset the player lives and the AI livves
		# 	# and set player to False so that our loop will restart
		# 	player_lives = 5
		# 	ai_lives = 5
		# 	player = False

		# else:
		# 	print("Make a valid choice - Y or N")
		# 	# this will generate a bug that we need to fix later
		# 	choice = input("Y / N : ")


	print("player lives:", gameVars.player_lives, "lives left")
	print("ai lives", gameVars.ai_lives, "lives left")

	# make the loop kee runnibng by setting player vack to False
	# unset, so that our loop condition above will evaluate to True

	gameVars.player = False



